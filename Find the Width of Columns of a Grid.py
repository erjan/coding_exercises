
'''
You are given a 0-indexed m x n integer matrix grid. The width of a column is the maximum length of its integers.

For example, if grid = [[-10], [3], [12]], the width of the only column is 3 since -10 is of length 3.
Return an integer array ans of size n where ans[i] is the width of the ith column.

The length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise.
'''



def findColumnWidth(self, matrix: List[List[int]]) -> List[int]:
        result = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j] = max(result[j],len(str(matrix[i][j])))
        return result
        
        
------------------------------------------------------------------------------------------------------------------
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        widths = [0] * n  
        for j in range(n):
            for i in range(m):
                width = len(str(abs(grid[i][j])))
                if grid[i][j] < 0:
                    width += 1 
                widths[j] = max(widths[j], width)
        return widths
