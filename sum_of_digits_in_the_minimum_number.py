'''
Given an integer array nums, return 0 if the sum of the digits of the minimum integer in nums is odd, or 1 otherwise.

 '''


class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:             
        mini = min(nums)
        
        sum_digits = 0
        
        while mini >= 1:
                sum_digits += mini %10
                mini = mini // 10
                
        print(sum_digits)
        if sum_digits %2 == 1:
            return 0
        return 1
        
