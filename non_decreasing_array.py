'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
'''


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter = 0
        n = nums
        for i in range(1,len(n)):
            if n[i] < n[i-1]:
                if i == 1 or n[i-2] < n[i]:
                    n[i-1] = n[i]
                    counter+=1
                else:
                    n[i] = n[i-1]
                    counter+=1
        return counter <=1
