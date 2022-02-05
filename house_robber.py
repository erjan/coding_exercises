'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
 '''

#TLE SOLUTION
class Solution:
    def rob(self, nums: List[int]) -> int:
        d = nums
        if len(d) == 0:
            return 0
        elif len(d) == 1:
            return d[0]
        else:
            return max( d[0] + self.rob(d[2:]), self.rob(d[1:]))
         
         
         
#working solution - with tips from knowledge center https://www.youtube.com/watch?v=jzpsHKJy00c

#insight: first find the recurrence, figure out the relations btw subproblems

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        v1 = nums[0]
        v2 = max(nums[1], nums[0]) #dont forget it should not be just nums[1] !!!!!!!!!!!!!!
        
        for i in range(2, len(nums)):
            tmp = v2
            v2 = max( nums[i] + v1, v2)
            v1 = tmp
            
        return v2
