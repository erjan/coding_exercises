'''
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
'''

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, v):
            seen.add((i, j))
            dp[i][j] = max(dp[i][j], v)
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] and (x, y) not in seen:
                    dfs(x, y, v + grid[x][y])
            seen.discard((i, j))
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    seen = set()
                    dfs(i, j, grid[i][j])
        return max(c for row in dp for c in row)
