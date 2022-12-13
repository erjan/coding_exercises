'''
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.
'''

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        r, c = len(A), len(A[0])

        for i in range(1, r):
            for j in range(c):
                tmp = A[i - 1][:j] + A[i - 1][j + 1:] # except same col value from above row.
                A[i][j] += min(tmp) # taking min value from above array with excluded adj col.

        return min(A[r - 1]) # min from last row
        
---------------------------------------------------------------------------------------------------------
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        for i in range(1, len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] += min(grid[i-1][:j]+grid[i-1][j+1:])
        
        return min(grid[-1])
