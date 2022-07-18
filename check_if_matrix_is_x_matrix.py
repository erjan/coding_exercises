'''
A square matrix is said to be an X-Matrix if both of the following conditions hold:

All the elements in the diagonals of the matrix are non-zero.
All other elements are 0.
Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.
'''

class Solution:
    def isD(self,i,j,l):
        return i == j or i+j == l-1

    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        l = len(grid)
        
        for i in range(l):
            for j in range(l):
                
                if self.isD(i,j,l):
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j]!= 0:
                        return False
        return True
      
------------------------------------
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n-1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True
      
---------------------------------------------
def checkXMatrix(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0]) # problem states that m == n

        def isDiagonal(i,j):
            return i == j or (i + j + 1 == m)
        
        def isValid(i,j):
            return isDiagonal(i,j) == bool(grid[i][j]) # if it's diagonal, it's != 0; if it's not diagonal, it's 0
            
        return all(isValid(i,j) for i,j in product(range(m), range(n)))
        
