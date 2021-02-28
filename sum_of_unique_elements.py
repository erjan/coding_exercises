'''
You are given an integer array nums. The unique elements 
of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
'''

from collections import Counter 

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum_res = 0
        res = Counter(nums)
        for k,v in res.items():

            if v == 1:
                sum_res +=k
        return sum_res
