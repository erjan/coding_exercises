'''
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.
'''


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans, n = [], 0
        for x in A:
            n  = ( 2*n + x ) % 5
            ans.append( n==0 )
        return ans
