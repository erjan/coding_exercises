'''
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
'''

Concept: Along diagonal, the sum of the indices are always SAME. For ex- take index- [0,2], [1,1], [2,0] (all have a total sum of 2).
So we will try to make a empty List of list, and sum of index will act a new index for List of list.

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i, r in enumerate(nums):
            for j, val in enumerate(r):
                if len(res) <= i + j: # adding a empty list at index i  + j
                    res.append([])
                res[i+j].append(val)
        l = []
        for r in res:
            l+=reversed(r)
        return l
