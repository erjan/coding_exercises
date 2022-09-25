'''
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.
'''

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod=int(1e9+7)
        stack=[] # (index, prefix sum at index)
        rsum=0
        res=0
        
        nums.append(0)
        
        for i, v in enumerate(nums):
            while stack and nums[stack[-1][0]] >= v:
                index, _ = stack.pop()
				
				# if the stack is empty, the subarray sum is the current prefixsum
                arrSum=rsum
                
                if stack:
                    arrSum=rsum-stack[-1][1]
                
				# update res with subarray sum
                res=max(res, nums[index]*arrSum)
                
            rsum+=v
            stack.append((i, rsum))
        
        return res%mod
