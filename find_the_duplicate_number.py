'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
 '''

#my own solution

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = dict()
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                return nums[i]
