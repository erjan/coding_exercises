'''
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.
'''


def maxMoves(self, grid: List[List[int]]) -> int:
    m, n, dirs = len(grid), len(grid[0]), [(0, 1), (1, 1), (-1, 1)]
    @cache
    def dp(i, j):
        ans = 0
        for x, y in dirs:
            ni, nj = i + x, j + y
            if 0 <= ni < m and nj < n and grid[i][j] < grid[ni][nj]:
                ans = max(ans, 1 + dp(ni, nj))
        return ans
    return max(dp(i, 0) for i in range(m))
----------------------------------------------------------------------------
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n: return 0
            res = 0 
            cur = grid[i][j]
            for x, y in [(-1, 1), (0, 1), (1, 1)]:
                if 0 <= i + x < m and 0 <= j + y < n and grid[i + x][j + y] > cur:
                    res = max(res, dp(i + x, j + y) + 1)
            return res
        ans = 0
        for i in range(m):
            ans = max(ans, dp(i, 0))
        return ans
      
------------------------------------------------------------------------------------------
#bottom up dp

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        res = 0
        for j in range(1, n):
            for i in range(m):
                if i > 0 and grid[i - 1][j - 1] < grid[i][j] and dp[i - 1][j - 1]:
                    res = max(res, j)
                    dp[i][j] = j
                    continue
                if grid[i][j - 1] < grid[i][j] and dp[i][j - 1]:
                    res = max(res, j)
                    dp[i][j] = j
                    continue
                if i < m - 1 and grid[i + 1][j - 1] < grid[i][j] and dp[i + 1][j - 1]:
                    res = max(res, j)
                    dp[i][j] = j
                    continue
        return res
            
        
