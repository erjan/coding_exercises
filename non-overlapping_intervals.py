'''
Given an array of intervals intervals
where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        last_end = intervals[0][1]
        remove = 0
        
        for i in range(1, len(intervals)):
            # found overlap
            if intervals[i][0] < last_end:
                remove += 1
                # remove the interval with the longer end
                last_end = min(intervals[i][1], last_end)
            else:
                last_end = intervals[i][1]
            
        return remove

------------------------------------------------------------------------------------------
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev = float("-inf")
        ans = 0
        for i in intervals:
            if i[0] >= prev:
                prev = i[1]
            else:
                ans += 1
        return ans
