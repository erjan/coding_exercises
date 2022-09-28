'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.
'''

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            zero = one = 0
            mask = 1 << i
            for num in nums:
                if mask & num: one += 1
                else: zero += 1    
            ans += one * zero        
        return ans 
