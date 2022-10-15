'''
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.
'''

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        for j in range(col): # calculate the prefix consecutive one for each column 
            for i in range(1,row):
                if matrix[i][j]:
                    matrix[i][j]+=matrix[i-1][j]
        ans = 0
        for i in range(row): # for every row we sort the list in ascending order
            matrix[i].sort()
            for j in range(col-1,-1,-1): 
                if matrix[i][j]==0:
                      break
                ans = max(ans, (col-j)*matrix[i][j]) # record the largest submatrix
        return ans
