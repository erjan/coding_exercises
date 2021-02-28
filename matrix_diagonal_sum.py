'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the 
elements on the secondary diagonal that are not part of the primary diagonal.
'''


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        first_diag_indices = []
        sum_primary_diag = 0
    
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j:
                    sum_primary_diag += mat[i][j]
                    first_diag_indices.append( [i,j])
        
        sum_back_diag = 0
        back_diag_indices = []
        for row in range(len(mat)):
                count = len(mat)-1 - row
                
                for j in range(len(mat[row])):
                        t = [row,count]
                        if t not in first_diag_indices:
                            sum_back_diag += mat[row][count]
                        count -=1
                        break
                        
        return sum_primary_diag + sum_back_diag
        

        
