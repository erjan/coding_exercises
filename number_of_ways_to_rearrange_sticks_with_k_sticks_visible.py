'''
There are n uniquely-sized sticks whose lengths are integers from 1 to n. You want to arrange the sticks such that exactly k sticks are visible from the left. A stick is visible from the left if there are no longer sticks to the left of it.

For example, if the sticks are arranged [1,3,2,5,4], then the sticks with lengths 1, 3, and 5 are visible from the left.
Given n and k, return the number of such arrangements. Since the answer may be large, return it modulo 109 + 7.
'''

class Solution:
    def rearrangeSticks(self, n, k):
        mod = 10**9 + 7
        dp = [1] + [0] * (k-1)
        for i in range(1, n):
            for j in range(min(i, k-1), 0, -1):
                dp[j] = (i * dp[j] + dp[j-1]) % mod
            dp[0] = (i * dp[0]) % mod
        return dp[-1]
      
----------------------------------------------------------
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0]*(k+1) for _ in range(n+1)]
        for i in range(1, k+1):
            dp[i][i] = 1
        for i in range(2, n+1):
            c = min(k+1, i)
            for j in range(1, c):
                dp[i][j] = (dp[i-1][j-1] + ((i-1)*dp[i-1][j])%mod)%mod
        return dp[n][k]
