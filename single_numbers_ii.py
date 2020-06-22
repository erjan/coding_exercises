'''
Given a non-empty array of integers, every element appears 
three times except for one, which appears exactly once. 
Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]]+=1
        
        for k in d.keys():
            if d[k] == 1:
                return k
        
