'''
You are given a 2D integer array grid of size m x n, where each cell contains a positive integer.

A cornered path is defined as a set of adjacent cells with at most one turn. More specifically, the path should exclusively move either horizontally or vertically up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the alternate direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.

The product of a path is defined as the product of all the values in the path.

Return the maximum number of trailing zeros in the product of a cornered path found in grid.

Note:

Horizontal movement means moving in either the left or right direction.
Vertical movement means moving in either the up or down direction.
'''

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        prefixH = [[[0] * 2 for _ in range(n + 1)] for __ in range(m)]
        prefixV = [[[0] * 2 for _ in range(n)] for __ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                temp= grid[i][j]
                while temp % 2 == 0:
                    prefixH[i][j + 1][0] += 1
                    prefixV[i + 1][j][0] += 1
                    temp //= 2
                while temp % 5 == 0:
                    prefixH[i][j + 1][1] += 1
                    prefixV[i + 1][j][1] += 1
                    temp //= 5
                for k in range(2):
                    prefixH[i][j + 1][k] += prefixH[i][j][k]
                    prefixV[i + 1][j][k] += prefixV[i][j][k]
        for i in range(m):
            for j in range(n):
                left = prefixH[i][j]
                up = prefixV[i][j]
                right, down, center = [0] * 2, [0] * 2, [0] * 2
                for k in range(2):
                    right[k] = prefixH[i][n][k] - prefixH[i][j + 1][k]
                    down[k] = prefixV[m][j][k] - prefixV[i + 1][j][k]
                    center[k] = prefixH[i][j + 1][k] - prefixH[i][j][k]
                LU, LD, RU, RD = [0] * 2, [0] * 2, [0] * 2, [0] * 2
                for k in range(2):
                    LU[k] += left[k] + up[k] + center[k]
                    LD[k] += left[k] + down[k] + center[k]
                    RU[k] += right[k] + up[k] + center[k]
                    RD[k] += right[k] + down[k] + center[k]
                ans = max(ans,
                          min(LU[0], LU[1]),
                          min(LD[0], LD[1]),
                          min(RU[0], RU[1]),
                          min(RD[0], RD[1]))
        return ans
      
------------------------------

import numpy as np

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        A = np.array(grid)
        def cumdivs(d):
            D = sum(A % d**i == 0 for i in range(1, 10))
            return D.cumsum(0) + D.cumsum(1) - D
        return max(np.minimum(cumdivs(2), cumdivs(5)).max()
                   for _ in range(4)
                   if [A := np.rot90(A)])
