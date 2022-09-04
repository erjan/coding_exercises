'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] * m

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]


        res = dp[-1][-1]
        return res
