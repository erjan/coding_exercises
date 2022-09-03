'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])

        if len(intervals) < 0:
            return newInterval

        i = 1

        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][0] = min(intervals[i-1][0], intervals[i][0])

                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])

                intervals.pop(i)
            else:
                i+=1
                continue
        return intervals
-------------------------------------------------------------------------------------------------------------
def insert1(self, intervals, newInterval):
    intervals.append(newInterval)
    res = []
    for i in sorted(intervals, key=lambda x:x.start):
        if res and res[-1].end >= i.start:
            res[-1].end = max(res[-1].end, i.end)
        else:
            res.append(i)
    return res
    
# O(n) time, not in-place, make use of the 
# property that the intervals were initially sorted 
# according to their start times
def insert(self, intervals, newInterval):
    res, n = [], newInterval
    for index, i in enumerate(intervals):
        if i.end < n.start:
            res.append(i)
        elif n.end < i.start:
            res.append(n)
            return res+intervals[index:]  # can return earlier
        else:  # overlap case
            n.start = min(n.start, i.start)
            n.end = max(n.end, i.end)
    res.append(n)
    return res
