'''
Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.
'''

#my own solution
class Solution:
    def countElements(self, nums: List[int]) -> int:
    
        if len(nums) == 1:
            return 0
        elif min(nums) == max(nums):
            return 0
        
        nums = sorted(nums)
        max1 = max(nums)
        min1 = min(nums)

        count_max = nums.count(max1)
        count_min = nums.count(min1)

        i = 0
        while i < count_max-1:
            nums.remove(max1)
            i += 1
        i = 0
        while i < count_min-1:
            nums.remove(min1)
            i += 1
        nums = sorted(nums)
        print(nums)
        res = len(nums)-2
        print(res)
        return res
   
