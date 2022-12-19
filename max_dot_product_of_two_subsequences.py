'''
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
'''

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [-math.inf] * (m + 1)
        for i in range(1, n + 1):
            dp, old_dp = [-math.inf], dp
            for j in range(1, m + 1):
                dp += max(
                    old_dp[j], # not select i
                    dp[-1], # not select j
                    old_dp[j - 1], # not select either
                    max(old_dp[j - 1], 0) + nums1[i - 1] * nums2[j - 1], # select both
                ),
        return dp[-1]
      
-------------------------------------------------------------------------------------------------------------
from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def helper(i, j):
            if i == 0 or j == 0: return -math.inf
            return max(helper(i - 1, j - 1), helper(i, j - 1), helper(i - 1, j),
                       max(helper(i - 1, j - 1), 0) + nums1[i - 1] * nums2[j - 1])
        return helper(len(nums1), len(nums2))
