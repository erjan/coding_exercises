'''
You are given an integer array nums.

Splitting of an integer array nums into subarrays is valid if:

the greatest common divisor of the first and last elements of each subarray is greater than 1, and
each element of nums belongs to exactly one subarray.
Return the minimum number of subarrays in a valid subarray splitting of nums. If a valid subarray splitting is not possible, return -1.

Note that:

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
A subarray is a contiguous non-empty part of an array.
'''


class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * (n+1)
        dp[-1] = 0
        for i in range(n-1, -1, -1): 
            for j in range(i, n): 
                if gcd(nums[i], nums[j]) > 1: dp[i] = min(dp[i], 1+dp[j+1])
        return dp[0] if dp[0] < inf else -1
