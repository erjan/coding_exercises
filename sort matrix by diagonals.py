You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
-------------------------------------------------------------------------------------------------------------------------------------


  class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        # upper right triangle j=i+d
        for d in range(n-2, -1, -1):
            diag=sorted(grid[i][i+d] for i in range(n-d))
            for i, x in enumerate(diag):
                grid[i][i+d]=x
        # lower left triangle i=j+d
        for d in range(n-1):
            diag=sorted((grid[j+d][j] for j in range(n-d)), reverse=True)
            for j, x in enumerate(diag):
                grid[j+d][j]=x
        return grid
        
        
        
