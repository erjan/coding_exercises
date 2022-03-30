'''
Given an array of distinct integers arr, where 
arr is sorted in ascending order, return the smallest 
index i that satisfies arr[i] == i. If there is no such index, return -1.
'''


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        
        
        for i in range(len(arr)):
            
            if arr[i] == i:
                return i
        return -1
