'''
There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.
'''

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        dp = [[[0] * (minProfit+1) for _ in range(n+1)] for _ in range(m+1)]
        for j in range(n+1): dp[m][j][0] = 1
        for i in range(m-1, -1, -1): 
            for j in range(n+1): 
                for k in range(minProfit+1): 
                    dp[i][j][k] = dp[i+1][j][k]
                    if group[i] <= j: dp[i][j][k] += dp[i+1][j-group[i]][max(0, k-profit[i])]
                    dp[i][j][k] %= 1_000_000_007
        return dp[0][n][minProfit]
      
      
