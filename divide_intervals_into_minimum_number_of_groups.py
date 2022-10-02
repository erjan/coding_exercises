'''
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.


same as meeting rooms

'''
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        heap = [intervals.pop(0)[1]]

        for start, end in intervals:
        
            if start <= heap[0]:
                heappush(heap, end)

            else:
                heappushpop(heap, end)

        return len(heap)
        
-------------------------------------------------------------------
    def minGroups(self, intervals):
        A = []
        for a,b in intervals:
            A.append([a, 1])
            A.append([b + 1, -1])
        res = cur = 0
        for a, diff in sorted(A):
            cur += diff
            res = max(res, cur)
        return res
