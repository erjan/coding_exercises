'''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <=len(nums):
                
            
                if nums[val-1] >0:
                    
                    nums[val-1] *=-1
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (len(nums)+1)
        
        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i
        return len(nums)+1
        
--------------------------------------------------------------------------------------
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        has1 = False
        for x in nums:
            if x == 1:
                has1 = True
                break
        if not has1:
            return 1
        
        n = len(nums)
        
        if n == 1:
            return 2
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n :
                nums[i] = 1
        
        for i in range(n):
            x = abs(nums[i])
            if nums[x-1] > 0:
                nums[x-1] *= -1
        
        for i in range(n):
            if nums[i] >0:
                return i+1
        
        return n+1
        
        
