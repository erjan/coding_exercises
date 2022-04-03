'''

Given a two-dimensional matrix of integers
matrix, determine whether it's a Toeplitz matrix. A Toeplitz 
is one where every diagonal descending from left to right has the same value.

'''


class Solution:
    def solve(self, matrix):
        

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
        
        
#another

class Solution:
    def solve(self, matrix):
        for row in range(1, len(matrix)):

            for col in range(1, len(matrix[0])):

                if matrix[row][col] != matrix[row - 1][col - 1]:
                    return False

        return True
