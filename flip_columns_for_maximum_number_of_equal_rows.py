'''
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.
'''

# we are storing the patter of the row and the flipped version of that row values which ever has the max value will be considered as the answer
    
'''
    [0,0,0],
    [0,0,1],
    [1,1,0]
                        count
    pattern -> (0,0,0) -> 1
               (1,1,1) -> 1  // flipped
               (0,0,1) -> 1  
               (1,1,0) -> 1  // Flipped
               (1,1,0) -> 2   // as 1,1,0 is already present
               (0,0,1) -> 2   // Flipped and since (0,0,1) is already present count is 2
               
               Max count 2 is the answer
			   
		
               
'''

TC -> O(m*n)

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        pattern=defaultdict(int)
        
        for row in matrix:
            
            pattern[tuple(row)]+=1
            flip=[1-c for c in row]
            pattern[tuple(flip)]+=1
        
        return max(pattern.values())
      
-----------------------------------------------------------------------------------------------------------------------------  

For each row, record the indices of the columns where the values are different from the first column in the row. We have to change these corresponding columns to make this row uniform.
Then store the tuple of these column indices into a dictionary counter.
Finally, find out which combination of column indices has the largest value in counter.

from collections import defaultdict
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = defaultdict(int)
        for i in range(len(matrix)):
            col = tuple(j for j in range(1, len(matrix[0])) if matrix[i][j] != matrix[i][0])
            counter[col] += 1
        return max(counter.values())
      
