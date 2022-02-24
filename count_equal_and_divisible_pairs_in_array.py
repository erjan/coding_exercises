'''
Given a 0-indexed integer array nums of length n and an integer k, return the 
number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
'''

#my own solution

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = nums
        count = 0
        for i in range(len(n)):
            
            for j in range(i+1,len(n)):
                if n[j] == n[i]:
                    if i < j and i*j %k == 0:
                        count+=1
            
        return count
            
            
