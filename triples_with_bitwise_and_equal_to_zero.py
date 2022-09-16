'''
Given an integer array nums, return the number of AND triples.

An AND triple is a triple of indices (i, j, k) such that:

0 <= i < nums.length
0 <= j < nums.length
0 <= k < nums.length
nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.
'''

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        ans = 0
        mem = [0] * (1 << 16)
        size = len(nums)

        for i in range(size):
            for j in range(i, size):
                mem[nums[i]&nums[j]] += 2 if i != j else 1
        
        for ij in range(1 << 16):
            if mem[ij] > 0:
                for k in nums:
                    if k & ij == 0:
                        ans += mem[ij]
        return ans
      
----------------------------------------------------------------------------------------
from collections import defaultdict

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = defaultdict(int)
        for i in range(n):
            for j in range(n):
                ctr[nums[i] & nums[j]] += 1
        res = 0
        for i in range(n):
            for val in ctr:
                if nums[i] & val == 0:
                    res += ctr[val]
        return res
