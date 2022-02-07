'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    def house_rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        v1 = nums[0]
        v2 = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            tmp = v2
            
            v2 = max( nums[i] + v1, v2)
            v1 = tmp

        return v2
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        first = self.house_rob(nums[1:])
        second = self.house_rob(nums[:-1])
        return max(first,second)
