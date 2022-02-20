

'''
Given an integer array nums of length n, you want to create an array ans of 
length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
'''
#my solution

class Solution:
    def f(self, nums):
        return nums*2

#not my solution

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r=[]
        for i in range(0,2*n):
            if i<n:
                r.append(nums[i])
            else:
                r.append(nums[i-n])
        return r
