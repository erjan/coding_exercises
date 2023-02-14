'''
You are given two 0-indexed integer arrays of the same length present and future where present[i] is the 
current price of the ith stock and future[i] is the price of the ith 
stock a year in the future. You may buy each stock at most once. You are also given an integer budget 
representing the amount of money you currently have.

Return the maximum amount of profit you can make.
'''



Explanation
dp[i]: Maximum profit when spend $i
Initially dp[0] = 0
Each stock can be only purchase once, thus they are the outer loop
For the inner loop, we want to test the present value against each cost (from 0 to budget), and see if we can get a large profit at cost j (dp[j]) by using the profit at certain cost (dp[j-p]); we will do this from larger cost to smaller, to avoid repeat counting.
Time: O(mn), m = len(present), n = budget
Implementation


class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        dp = [0] * (budget+1)
        for p, f in zip(present, future):
            for j in range(budget, p-1, -1):
                dp[j] = max(dp[j], dp[j-p] + f-p)
        return dp[-1]

