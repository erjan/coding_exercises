'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may 
not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
'''


def longestIncreasingPath(self, matrix):
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x, y) for x in range(M) for y in range(N))
  
  ----------------------------------------------------------------------------------------
  class Solution:
    def longestIncreasingPath(self, M: List[List[int]]) -> int:
        ylen, xlen = len(M), len(M[0])
        @lru_cache(maxsize=None)
        def dfs(y, x):
            val = M[y][x]
            return 1 + max(
                dfs(y+1,x) if y < ylen - 1 and val > M[y+1][x] else 0,
                dfs(y-1,x) if y > 0 and val > M[y-1][x] else 0, 
                dfs(y,x+1) if x < xlen - 1 and val > M[y][x+1] else 0,
                dfs(y,x-1) if x > 0 and val > M[y][x-1] else 0)
        return max(dfs(y, x) for y in range(ylen) for x in range(xlen))
