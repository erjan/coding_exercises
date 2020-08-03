'''
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
'''



class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        
        status = True
        peak = max(A)
        peak_index = A.index(peak)
        
        if peak_index == 0 or peak_index == len(A)-1:
            return False

        for i in range(peak_index):
            if A[i] >= A[i+1]:
                print(A[i])
                return False


        for i in range(peak_index, len(A)-1):

            if A[i] <= A[i+1]:
                return False

        return True
