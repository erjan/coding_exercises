'''
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses 
the element in the next row that is either directly below or diagonally
left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
'''

import math
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix)):
				# Update current element with the min of its upper 3 elements. 
				# If any of those do not exist then just use math.inf as placeholder
                matrix[row][col] = matrix[row][col] + \
				min(matrix[row-1][col], 
				matrix[row-1][col-1] if col - 1 >= 0 else math.inf, 
				matrix[row-1][col+1] if col + 1 < len(matrix) else math.inf)
		# The minimum item on the last row is the result because it is the "smallest path sum"
        return min(matrix[-1])
    
----------------------------------------------------------------------------------------------------
def minFallingPathSum(self, matrix: List[List[int]]) -> int:
	grid = matrix
	for i in range(1, len(grid)):
		for j in range(len(grid[i])):

			# [1] up-left
			if i-1 >= 0 and j-1 >= 0:
				p1 = grid[i-1][j-1]
			else:
				p1 = float('inf')

			# [2] up-same
			if i-1 >= 0:
				p2 = grid[i-1][j]
			else:
				p2 = float('inf')

			# [3] up-right
			if i-1 >= 0 and j+1 <= len(grid[0])-1:
				p3 = grid[i-1][j+1]
			else:
				p3 = float('inf')

			grid[i][j] += min(p1,p2,p3)

	return min(grid[len(grid)-1])

------------------------------------------------------------------

#my own code - version

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)

        
        
        
        for i in range(1,n):
            for j in range(n):
                
                if j-1>=0 and i-1>=0:
                    topleft = matrix[i-1][j-1]
                else:
                    topleft = float('inf')
                    
                if j+1 < n and i-1 >=0:
                    topright = matrix[i-1][j+1]
                else:
                    topright = float('inf')
                
                if i-1 >=0:
                    top = matrix[i-1][j]
                else:
                    top = float('inf')
                                                
                matrix[i][j] += matrix[i][j] + min(top, topleft, topright)
                
        return min(matrix[-1])                                                
