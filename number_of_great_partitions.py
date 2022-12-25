'''
You are given an array nums consisting of positive integers and an integer k.

Partition the array into two ordered groups such that each element is in exactly one group. A partition is called great if the sum of elements of each group is greater than or equal to k.

Return the number of distinct great partitions. Since the answer may be too large, return it modulo 109 + 7.

Two partitions are considered distinct if some element nums[i] is in different groups in the two partitions.
'''


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k + 1)] + [[-1] * (k + 1) for _ in range(n)]
        dp[0][0] = 1
        def subsetSumCounts(s, idx):
            if s < 0:
            	return 0
            if dp[idx][s] < 0:
                dp[idx][s] = subsetSumCounts(s, idx - 1) + subsetSumCounts(s - nums[idx - 1], idx - 1)
            return dp[idx][s]
                
        invalid_pairs = sum([subsetSumCounts(i, n) for i in range(k)]) * 2
        return max(2**n - invalid_pairs, 0) % (10**9 + 7)

