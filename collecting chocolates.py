'''
You are given a 0-indexed integer array nums of size n representing the cost of collecting different chocolates. The cost of collecting the chocolate at the index i is nums[i]. Each chocolate is of a different type, and initially, the chocolate at the index i is of ith type.

In one operation, you can do the following with an incurred cost of x:

Simultaneously change the chocolate of ith type to ((i + 1) mod n)th type for all chocolates.
Return the minimum cost to collect chocolates of all types, given that you can perform as many operations as you would like.
'''


class Solution:
    def minCost(self, nums: list[int], x: int) -> int:
        
        N, dp, ans, nums = range(len(nums)), nums[:], inf, deque(nums)
        
        for rot in N:

            dp = [min(dp[i], nums[i]) for i in N]
            ans = min(ans, sum(dp) + x*rot)

            nums.rotate(1)

        return ans
