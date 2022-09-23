'''
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
'''

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def dfs(i,val):
            if maxBit == val : return 1<<(len(nums)-i)
            if i == len(nums): return 0
            return dfs(i+1,val|nums[i]) + dfs(i+1,val)
        maxBit = 0
        for i in nums: maxBit |= i
        return dfs(0,0)
