'''
You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.
'''


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            mat[r1][c1] += 1
            if r2 + 1 < n: mat[r2 + 1][c1] -= 1
            if c2 + 1 < n: mat[r1][c2 + 1] -= 1
            if r2 + 1 < n and c2 + 1 < n: mat[r2 + 1][c2 + 1] += 1
        for i in range(n):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]
        for i in range(1, n):
            for j in range(n):
                mat[i][j] += mat[i - 1][j]
        return mat
