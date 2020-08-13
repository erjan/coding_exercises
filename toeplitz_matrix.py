'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
'''

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = matrix
        for i in range(len(m)):
            for j in range(len(m[i])):
                cell = m[i][j]
                x = i
                y = j
                while x < len(m)-1 and y < len(m[0])-1:
                    x+=1
                    y+=1
                    next_cell = m[x][y]
                    if next_cell != cell:
                        return False

        return True
