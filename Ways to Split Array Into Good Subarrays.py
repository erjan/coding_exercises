'''
You are given a binary array nums.

A subarray of an array is good if it contains exactly one element with the value 1.

Return an integer denoting the number of ways to split the array nums into good subarrays. As the number may be too large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.
'''


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        
        n = len(nums)
        dp = [0]*(n+1)
        curr = 0  # used for the previous consecutive zeroes dp sum
        for i in range(n):
            if nums[i] == 0:
                dp[i] = dp[i-1]
                curr = (curr + dp[i]) % mod
            else:
                dp[i] = ( max(1, dp[i-1]) + curr ) % mod    # max(1,dp[i-1) in case first 1 encounter you need to assign dp[i] = 1
                curr = 0
        
        return dp[n-1] % mod
