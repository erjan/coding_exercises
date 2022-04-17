'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects 
inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, 
schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't 
include intervals like [5, 5] in our answer, as they have zero length.
'''


The basic ideas here:

Sort our intervals by starting time.
Merge overlapping busy intervals.
Find the times between these intervals.
eg. [[[1,2],[5,6]],[[1,3]],[[4,10]]]
After sort:
[[1,2], [1,3], [4,10], [5,6]]
After merge:
[[1,3], [4,10]]
Now we find the diff. between these using the end time of [i-1] and start time of [i]
[[3, 4]]

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
		# Flatten the given intervals.
        ints = []
        for i in schedule:
            [ints.append(x) for x in i]
        
		# Sort the intervals by starting time which is a key part of this soln. and indentifying overlap.
        ints.sort(key = lambda x:x.start)
        
		# Now we want to merge intervals (the continuous periods of being busy).
        merged = []
        for i in ints:
		    # If we have no intervals in our list or the current task starts after the previous one ends.
            if not merged or i.start > merged[-1].end:
                merged.append(i)
            else:
			    # We know that the start time intersects the start,end of the previous task, so we take the max ending time.
				# As this will be a merged, continuous busy period.
                merged[-1].end = max(i.end, merged[-1].end)

        # Now we have our merged intervals we can look at the time between the merged 
		# intervals as these will be the free time for the employee. 
        free = []
        for i in range(1, len(merged)):
            free.append(Interval(start=merged[i-1].end, end=merged[i].start))
			
		# Now we're left with intervals of free time.
        return free
    
-------------------------------------------------------------------------------------
All solutions iterate over the flatten and sorted schedule of all employees and compare event[i].start with prev_end = max(event[:i].end). It gives the resulting interval Interval(prev_end, event[i].start)

This first solution flattens and sorts schedule manually.

# T: O(n*log(n)), n is the number of intervals across all employees
# S: O(n)
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # flatten schedule
        events = []
        for employee in schedule:
            for event in employee:
                events.append(event)

        # sort events by start
        events.sort(key=operator.attrgetter('start'))

        # collect result
        res = []
        iterator = iter(events)
        prev_end = next(iterator).end
        for event in iterator:
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return res
Second solution takes into account that all emploees lists are already sorted. heap helps to iterate schedule in a sorted manner for O(n*log(k)).

# T: O(n*log(k)), n is the number of intervals across all employees
#                 k is the number of employees
# S: O(k)
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # collect first events of all employees
        heap = []
        for i, employee in enumerate(schedule):
            # (event.start, employee index, event index)
            heapq.heappush(heap, (employee[0].start, i, 0))

        res = []
        _, i, j = heap[0]
        prev_end = schedule[i][j].end
        while heap:
            _, i, j = heapq.heappop(heap)
            # check for next employee event and push it
            if j + 1 < len(schedule[i]):
                heapq.heappush(heap, (schedule[i][j + 1].start, i, j + 1))

            event = schedule[i][j]
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return res
The fastest and shortest solution would be to use heapq.merge. According to its doc it does exactly what is needed:

'''Merge multiple sorted inputs into a single sorted output.

Similar to sorted(itertools.chain(*iterables)) but returns a generator,
does not pull the data into memory all at once, and assumes that each of
the input streams is already sorted (smallest to largest).

>>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
[0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]
'''
# T: O(n*log(k)), n is the number of intervals across all employees
#                 k is the number of employees
# S: O(k)
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        iterator = heapq.merge(*schedule, key=operator.attrgetter('start'))
        res, prev_end = [], next(iterator).end
        for event in iterator:
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return res
      
----------------------------------------------------------------------
def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
    result = []
    heap = [ (emp[0].start, idx, 0) for idx, emp in enumerate(schedule) ]
    heapq.heapify(heap)
    
    # either take end or the start of the starting interval
    # minStart = schedule[heap[0][1]][0].end
    minStart = heap[0][0]
    
    while heap:
        t, e_id, colIdx = heapq.heappop(heap)
        
        if minStart < t:
            result.append(Interval(minStart, t))
            
        minStart = max(minStart, schedule[e_id][colIdx].end)
        
        if colIdx + 1 < len(schedule[e_id]):
            colIdx += 1
            heapq.heappush(heap, (schedule[e_id][colIdx].start, e_id, colIdx))
    
    return result
  
--------------------------------------------------------------------------------------
The first solution came to my mind was sorting the intervals and doing a line sweep. However, since each employee schedule is sorted, we can use heapq.merge to sort intervals in O(NlogK) instead of O(NlogN) where N is the number of intervals and K is the number of employees.

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        import heapq

        intervals = heapq.merge(*schedule, key=lambda interval: (interval.start, interval.end))

        result = []
        end = next(intervals).end
        for interval in intervals:
            if interval.start > end:
                result.append(Interval(end, interval.start))
            end = max(interval.end, end)
        return result
      
----------------------------------------------------------------------
class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        if not schedule or not schedule[0]:
            return []
        List = [i for l in schedule for i in l]
        List.sort(key = lambda a:a.start)
        res, prev_end = [], List[0].end
        for interval in List:
            if interval.start>prev_end:
                new_i = Interval(prev_end, interval.start)
                res.append(new_i)
            prev_end= max(prev_end, interval.end)
        return res``
      
----------------------------------------------------------------------------------------
we will use the face that each employee list is individually sorted!

We take the first interval of each employee and insert it in a Min Heap. This Min Heap can always give us the interval with the smallest start time. Once we have the smallest start-time interval, we can then compare it with the next smallest start-time interval (again from the Heap) to find the gap.

Whenever we take an interval out of the Min Heap, we can insert the next interval of the same employee. This also means that we need to know which interval belongs to which employee.

import heapq



# Official Definition for an Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end



# Custom object definition to help operate the operations
class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval                    # interval representing employee's working hours
        self.employeeIndex = employeeIndex          # index of the list containing working hours of this employee
        self.intervalIndex = intervalIndex          # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: list<list<Interval>>
        :rtype: list<Interval>
        """
        scheduleLength = len(schedule)
        freeIntervals = []
        if not schedule or scheduleLength <= 0:
            return freeIntervals
        minHeap = []
        for index, employeeSchedule in enumerate(schedule):                     # insert the first interval of each employee to the queue/minHeap
            minHeap.append(EmployeeInterval(employeeSchedule[0], index, 0))
        heapq.heapify(minHeap)                                                  # create the heap from the array
        previousInterval = minHeap[0].interval
        while minHeap:
            queueTop = heapq.heappop(minHeap)
            if previousInterval.end < queueTop.interval.start:                  # if previousInterval is not overlapping with the next interval, insert a free interval
                freeIntervals.append(Interval(previousInterval.end, queueTop.interval.start))
                previousInterval = queueTop.interval
            else:                                                               # overlapping intervals, update the previousInterval if needed
                if previousInterval.end < queueTop.interval.end:
                    previousInterval = queueTop.interval
            intervalsArrayOfEmployee = schedule[queueTop.employeeIndex]
            nextIntervalIndexOfCurrentEmployee = queueTop.intervalIndex + 1
            if len(intervalsArrayOfEmployee) > nextIntervalIndexOfCurrentEmployee:           # if there are more intervals available for the same employee, add their next interval
                heapq.heappush(minHeap, EmployeeInterval(intervalsArrayOfEmployee[nextIntervalIndexOfCurrentEmployee], queueTop.employeeIndex, nextIntervalIndexOfCurrentEmployee))
        return freeIntervals
