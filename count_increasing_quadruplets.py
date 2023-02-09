'''
Given a 0-indexed integer array nums of size n containing all numbers from 1 to n, return the number of increasing quadruplets.

A quadruplet (i, j, k, l) is increasing if:

0 <= i < j < k < l < n, and
nums[i] < nums[k] < nums[j] < nums[l].
'''


'''
Intuition
dp[j] stores the count of all valid triplets (i, j, k) that satisfies i < j < k and nums[i] < nums[k] < nums[j] and using the current number as the role j. (Refer to Leetcode Q456 132 pattern, point out by @RealFan.)

For every new value l, iterate all previous stored dp[j] (132 pattern counts). If nums[l] > nums[j], they can form a 
valid 1324 quadruplet pattern, then add dp[j] into total 1324 counts.

During iteration, we also update previous dp[j] by keeping track of the amount of smaller 
numbers in front of each new value. If nums[l] < nums[j], the new value is a potential k for j in the future, so add its previous_small to the dp[j].
'''

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0
        for j in range(n):
            prev_small = 0
            for i in range(j):
                if nums[j] > nums[i]:
                    prev_small += 1
                    ans += dp[i]
                elif nums[j] < nums[i]:
                    dp[i] += prev_small
        return ans
