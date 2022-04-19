'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
'''


def minMeetingRooms(self, intervals):
    intervals.sort(key=lambda x:x.start)
    heap = []  # stores the end time of intervals
    for i in intervals:
        if heap and i.start >= heap[0]: 
            # means two intervals can use the same room
            heapq.heapreplace(heap, i.end)
        else:
            # a new room is allocated
            heapq.heappush(heap, i.end)
    return len(heap)
  
  ----------------------------------------------------------------
  # Very similar with what we do in real life. Whenever you want to start a meeting, 
 # you go and check if any empty room available (available > 0) and
 # if so take one of them ( available -=1 ). Otherwise,
 # you need to find a new room someplace else ( numRooms += 1 ).  
 # After you finish the meeting, the room becomes available again ( available += 1 ).
 
 def minMeetingRooms(self, intervals):
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        
        starts.sort()
        ends.sort()
        s = e = 0
        numRooms = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                    
                s += 1
            else:
                available += 1
                e += 1
        
        return numRooms
-------------------------------------------------

we need to know when we need a new room and when we can share the room.
We sort the interval time slot by the start time.
The definition of overlap: the end time of the current time slot is larger than the begin time of the next time slot, [1,11],[10,19], 11 > 10, there is an overlap
If there is an overlap between the current time slot and the smallest end time in the minimum heap. we need a new room for the meeting.
If there is no overlap between the current time and the smallest end time in the minimum heap, we don't need a new room for the meeting since we can use the the same room of the smallest end time. But we still need the end time in the future to help us decide whether we have an overlap or not.
We use a minimum heap to store the k-largest end time we meet until now. If the current time slot's begin time is larger than the smallest end time in the minimum heap == we don't have overlap == we don't need a new room == we can share the room with the smallest end time in the minimum heap.However, we need to update the minimum heap by using replace method. If the current time slot's begin time is less than the smallest end time in the minimum heap, we have an overlap now, i.e., we need a new room, we need to push the current time slot's end time into the minimum heap.
heapq.heapreplace(heap, item)
Pop and return the smallest item from the heap, and also push the new item. The heap size doesn't change.
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        [[0,30],[5,10],[9,15],[15,18],[16,18],[19,20],[40,41] ]
        [0                                    30]
            [5  10]
               [9    15]
                     [15     18]
                         [16 18]
                                  [19 20] 
                                                   [40  41]
        [0,30],  h =[30]
        [5,10],  h =[10,30]
        [9,15],  h =[10,15,30]
        [15,18], h =[15,18,30]
        [16,18], h =[18,18,30]
        [19,20], h= [18,20,30]
		[40,41], h =[20,30,40]
        """
        h =[]
        sort = sorted(intervals)
        for i in sort:
            # need a new meeting room
            if h == [] or h[0] >i[0]:
                heapq.heappush(h,i[1])
            # don't need a new meeting room, just update the end time
            else:
                heapq.heapreplace(h,i[1])
        return len(h)
-------------------------------------------

This is an interval partition problem. We can have two correct heurstics that 1) we process intervals ordered by starting time and assign each interval to a 'current vacant' room. 2) We only check the room with the eariest ending time for global vacancy. If there is no vacant room, we add one.

Since we iterate intervals by starting time, there is no better choice than current interval as rest intervals would all request one more room if current one does.
And we also need to track the ending time since we need to determine whether there exists a vacant room at specific time. We only track the earliest ending time as we only check this room for vacancy. If this room is not vacant, there is no need to check the rest and we just add one more room.

So combining two heuristics, we can sort starting time and ending time separately. We iterate starting time and use a pointer to track current earliest ending time.
So s is current interval's starting time and i is the pointer to current earliest ending time. If s < ends[i], there is no vacant room, we add one more room.
Otherwise, we assign current interval to a vacant room and our current earliest ending time should be updated to ends[i+1].

def minMeetingRooms(intervals):
	starts = sorted(i.start for i in intervals)
	ends = sorted(i.end for i in intervals)
	i = cnt = 0
	for s in starts:
		if s < ends[i]: cnt += 1
		else: i += 1
	return cnt
And sorting takes O(NlogN) and greedy one pass takes O(N). So time complexity is O(NlogN).

-------------------------------------------------------------------------------

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        rooms = 0
        
        if not intervals:
            return 0
        
        endp = 0
        
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        for i in range(len(starts)):
            if starts[i]>=ends[endp]:
                endp+=1
            else:
                rooms+=1
        
        return rooms
      
      
