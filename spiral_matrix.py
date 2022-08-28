'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1
        u, d = 0, len(matrix) - 1
        res = []
        step = 0
        while l <= r and u <= d:
            match (step % 4):
                case 0:
                    for i in range(l, r+1):
                        res.append(matrix[u][i])
                    u += 1
                case 1:
                    for i in range(u, d+1):
                        res.append(matrix[i][r])
                    r -= 1
                case 2:
                    for i in range(r, l-1, -1):
                        res.append(matrix[d][i])
                    d -= 1
                case 3:
                    for i in range(d, u-1, -1):
                        res.append(matrix[i][l])
                    l += 1
            step += 1
        return res
      
------------------------------------------------------------------------------
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        row_begin = 0
        col_begin = 0
        row_end = len(matrix)-1 
        col_end = len(matrix[0])-1
        while (row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])
            row_begin += 1
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            if (row_begin <= row_end):
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])
                row_end -= 1
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin])
                col_begin += 1
        return res

---------------------------------------------------------------------------------------------------------------
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        res = []
        while left <= right and top <= bottom:
            #  top left to top right
            for col in range(left,right+1):
                res.append(matrix[top][col])
            top += 1
            # top right to right bottom
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -= 1
            # right bottom to right left
            for col in range(right, left-1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1
             # left bottom to top left
            for row in range(bottom, top-1, -1):
                res.append(matrix[row][left])
            left += 1
        # just ignore the redundant and return length of m*n
        return res[:m*n]
