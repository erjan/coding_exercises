'''


Given an integer square (n by n) matrix, return its transpose. A transpose 
of a matrix switches the row and column indices. That is, for every r and c, matrix[r][c] = matrix[c][r].

'''


class Solution:
    def solve(self, matrix):

        col = [ c for c in zip(*matrix)]
        matrix = []
        for c in col:
            matrix.append(c)
        return matrix


      
#another

class Solution:
    def solve(self, matrix):
        if matrix:
            new_mat = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        else:
            return []
        return new_mat
        
