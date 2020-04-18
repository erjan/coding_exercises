'''
Given a m x n grid filled 
with non-negative numbers, find a path 
from top left to bottom right which minimizes 
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        s = 0
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])
        if n == 0:
            return 0

        for i in range(m):
            for j in range(n):
                if i-1 >=0 and j-1 >=0:
                    grid[i][j] += min(grid[i-1][j],
                                      grid[i][j-1])
                else:
                    if i-1 >=0:
                        grid[i][j] += grid[i-1][j]
                    if j -1 >=0:
                        grid[i][j] += grid[i][j-1]
        return grid[m-1][n-1]
