'''
Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an integer and add all these numbers. 
The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.

Return True if the array is good otherwise return False.
'''


def isGoodArray(self, nums):

    if len(nums) == 1:
        return nums[0] == 1
		
    def gcd(a, b):
        if a == 0 :
            return b

        return gcd(b%a, a)
    
    for i in range(1,len(nums)):
        greatest_denom = gcd(nums[i-1],nums[i])
        if greatest_denom == 1:
            return True
        nums[i] = greatest_denom
    return False
  
----------------------------------------------------
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a,b):
            while a:
                a, b = b%a, a
            return b
        return reduce(gcd,nums)==1
