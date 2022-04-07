
'''
Given an integer 
array nums, return true if nums is consecutive, otherwise return false.

An array is consecutive if it contains 
every number in the range [x, x + n - 1] (inclusive), where x is the 
minimum number in the array and n is the length of the array.

'''


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        for i in range(len(nums)-1):
            
            if nums[i] +1 != nums[i+1]:
                return False
        return True
        
#another

class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        
        # edge case
        if len(nums) == 1:
            return True
        
        num_set = set(nums)
        
        # check there is no duplicate items
        if len(num_set) != len(nums):
            return False
        
        # calculate the maximum value using minimum value and length
        n = len(nums)
        start = min(nums)
        end = start + n - 1
        
        # check the distance is divisible
        if (end - start) % (n - 1) != 0:
            return False
        
        dis = (end - start) // (n - 1)
        
        # check every number exists
        for num in range(start + dis, end + 1, dis):
            if num not in num_set:
                return False
            
        return True
