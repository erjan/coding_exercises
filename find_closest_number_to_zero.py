'''
Given an integer array nums of size n, return the number with 
the value closest to 0 in nums. If there are multiple answers, return the 
number with the largest value.
'''


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        m = float('inf')
        for i in nums:
            x = abs(i-0)
            if x < m:
                m = x
                val = i
            elif x == m and val < i:
                val = i
        return val
