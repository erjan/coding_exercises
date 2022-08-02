'''
You are given a 0-indexed m x n integer matrix grid consisting of distinct integers from 0 to m * n - 1. You can move in this matrix from a cell to any other cell in the next row. That is, if you are in cell (x, y) such that x < m - 1, you can move to any of the cells (x + 1, 0), (x + 1, 1), ..., (x + 1, n - 1). Note that it is not possible to move from cells in the last row.

Each possible move has a cost given by a 0-indexed 2D array moveCost of size (m * n) x n, where moveCost[i][j] is the cost of moving from a cell with value i to a cell in column j of the next row. The cost of moving from cells in the last row of grid can be ignored.

The cost of a path in grid is the sum of all values of cells visited plus the sum of costs of all the moves made. Return the minimum cost of a path that starts from any cell in the first row and ends at any cell in the last row.
'''


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        matrix = [ [float('inf') for j in range(n)] for i in range(m)]
        
        #first row fill up
        
        for i in range(n):
            matrix[0][i] = grid[0][i]
            
        i = 1
        
        while i < m:
            for j in range(n):
                for k in range(len(moveCost[0])):
                    matrix[i][k] = min(matrix[i][k], matrix[i-1][j] + moveCost[grid[i-1][j]][k] + grid[i][k])
            i+=1
            
        return min(matrix[-1]) # min of last row
        
