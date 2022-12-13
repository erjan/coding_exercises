'''
You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.
'''


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp = [[[0 for i in range(k)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        rem = grid[0][0] % k
        dp[0][0][rem] = 1
        for i in range(1, len(grid[0])):
            dp[0][i][(rem + grid[0][i]) % k] = 1
            rem = (rem + grid[0][i]) % k
        rem = grid[0][0] % k
        for j in range(1, len(grid)):
            dp[j][0][(rem + grid[j][0]) % k] = 1
            rem = (rem + grid[j][0]) % k
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                for rem in range(k):
                    dp[i][j][(rem + grid[i][j]) % k] = dp[i - 1][j][rem] + dp[i][j - 1][rem]
        return dp[-1][-1][0] % (10**9 + 7)
------------------------------------------------------------------------------
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        p=10**9+7
        m=len(grid)
        n=len(grid[0])
        
        lst=[([0]*k if j else [1]+[0]*(k-1)) for j in range(n)]

        for i in range(m):
            gr=grid[i]
            klst=[0]*k
            for j in range(n):
                g=gr[j]
                l=lst[j]
                klst=[(klst[(r-g)%k]+l[(r-g)%k])%p for r in range(k)]
                lst[j]=klst

        return lst[-1][0]
