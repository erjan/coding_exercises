'''
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.


 '''

from math import gcd

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        return gcd(min_,max_)
