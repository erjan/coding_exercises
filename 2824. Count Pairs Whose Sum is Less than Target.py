'''
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
'''

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]<target:
                    res+=1
        return res
