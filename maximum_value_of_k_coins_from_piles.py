'''
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.
'''

#bottom up
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n, m = len(piles), 0
        prefixSum = []
        for i in range(n):
            temp = [0]
            for j in range(len(piles[i])):
                temp.append(temp[-1] + piles[i][j])
                m += 1
            prefixSum.append(temp)
        if m == k:
            return sum(temp[-1] for temp in prefixSum)
            
        dp = [[0] * (k + 1) for _ in range(n)]
        for j in range(1, k + 1):
            if j < len(prefixSum[0]):
                dp[0][j] = prefixSum[0][j]
        
        for i in range(1, n):
            for j in range(1, k + 1):
                for l in range(len(prefixSum[i])):
                    if l > j:
                        break
                    dp[i][j] = max(dp[i][j], prefixSum[i][l] + dp[i - 1][j - l])
        return dp[n - 1][k]
