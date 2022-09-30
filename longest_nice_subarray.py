'''
You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.
'''


class Solution:
    def longestNiceSubarray(self, A):
        res = AND = i = 0
        for j in range(len(A)):
            while AND & A[j]:
                AND ^= A[i]
                i += 1
            AND |= A[j]
            res = max(res, j - i + 1)
        return res
                
                
            
