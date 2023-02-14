'''
Given a 0-indexed integer array nums, return the number of 
subarrays
 of nums having an even product.
 '''

from collections import defaultdict
class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        i = -1
        res = 0
        for j,num in enumerate(nums):
            if num%2 == 0:
                i = j 
            res += i + 1
        return res
-----------------------------------------------------------------------------------------
class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        ans = val = 0
        for i, x in enumerate(nums): 
            if not x&1: val = i+1
            ans += val 
        return ans 
