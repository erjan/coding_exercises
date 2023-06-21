'''
You are given a 0-indexed permutation of n integers nums.

A permutation is called semi-ordered if the first number equals 1 and the last number equals n. You can perform the below operation as many times as you want until you make nums a semi-ordered permutation:

Pick two adjacent elements in nums, then swap them.
Return the minimum number of operations to make nums a semi-ordered permutation.

A permutation is a sequence of integers from 1 to n of length n containing each number exactly once.
'''


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:

        x = nums.index(1)
        y = nums.index(max(nums))
        n = len(nums)
        if x < y :
            return x + (n-y-1)
        else:
            return x + (n-y-1)-1
--------------------------------------------------------------------------------------------
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        
        if nums[0] == 1 and nums[len(nums) - 1] == len(nums):
            return 0
        
        op = 0
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        if min_idx < max_idx:
            op = min_idx + (len(nums) - 1 - max_idx)
        if min_idx > max_idx:
            op = min_idx + (len(nums) - 1 - max_idx) - 1
        
        return op


        
