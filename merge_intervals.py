'''
Given an array of intervals where intervals[i] = [starti, endi], merge all 
overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        for cur in intervals[1:]:
            if cur[0] <= res[-1][1]:
                res[-1][1] = max(cur[1],res[-1][1])
            else:
                res.append(cur)
        return res
