'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not len(matrix) or not len(matrix[0]):
			# Quick response for empty matrix
            return False
        
        h, w = len(matrix), len(matrix[0])
        
        # Start adaptive search from bottom left corner
        y, x = h-1, 0
        
        while True:
            
            if y < 0 or x >= w:
                break
            
            current = matrix[y][x]
            
            if target < current:
                # target is smaller, then go up
                y -= 1
            
            elif target > current:
                # target is larger, then go right
                x += 1
            
            else:
                # hit target
                return True
            
        return False
-----------------------------------------------------------------------
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # T: O(m + n), S: O(1)
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            curr = matrix[r][c]
            if curr == target:
                return True
            elif curr > target:
                c -= 1
            else:
                r += 1
        return False
