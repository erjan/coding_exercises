'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of
the row below. More formally, if you are on index i 
on the current row, you may move to either index i or index i + 1 on the next row.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1] * n for _ in range(n)]
        dp[n - 1] = triangle[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                lower_left = triangle[i][j] + dp[i + 1][j]
                lower_right = triangle[i][j] + dp[i + 1][j + 1]
                dp[i][j] = min(lower_left, lower_right)

        return dp[0][0]
