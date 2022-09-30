'''
Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

A subarray is a contiguous part of an array.
'''


class Solution:
    def trail(self,A,a,b):
        sa = ba = sum(A[:a]) # sum from beggining
        sb = sum(A[a:b+a])   # sum right after "sa"
        best = ba+sb
        for i in range(b+a,len(A)):
            sb += A[i]  - A[i-b]
            sa += A[i-b]- A[i-b-a]
            ba = max( ba, sa ) # window sum of sb runs with best from "sa"
            if ba+sb > best:
                best = ba+sb
        return best
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        trail = self.trail
        return max( trail(A,L,M) , trail(A,M,L) )
