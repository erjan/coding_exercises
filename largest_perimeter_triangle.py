'''
Given an integer array nums, return the largest 
perimeter of a triangle with a non-zero area, formed 
from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 '''

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums = sorted(nums, reverse=True)

        print(nums)
        max_p = 0
        for i in range(len(nums)-2):

            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            cur_p = 0
            if (a+b) > c and (a+c) > b and (c+b) > a:
                
                cur_p = sum(list([a, b, c]))
                
                if cur_p > max_p:
                    max_p = cur_p

        return max_p
