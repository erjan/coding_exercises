'''
You are given an m x n binary matrix grid.

In one operation, you can choose any row or column and flip each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.

 
 '''


Explanation
I honestly don't know how to categorize this problem. It seems like a Math problem to me. Once you understand the logic, the implementation is simple.
Basically the "pattern" of each row should be the same, by pattern, I mean following:
001100 and 001100 are the same pattern
001100 and 110011 (the invert of original) are the same pattern
Only in above situation, one matrix can be converted to all zero
Intuition?
Believe it or not, I draw a couple examples to test it out and suddenly it becomes obvious
I guess it's good habit to get your hands dirty :)
Implementation
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1, r1_invert = grid[0], [1-val for val in grid[0]]
        for i in range(1, len(grid)):
            if grid[i] != r1 and grid[i] != r1_invert:
                return False
        return True
You need an one-liner? Sure, why not.

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        return all(grid[i] == grid[0] or grid[i] == [1-val for val in grid[0]] for i in range(len(grid)))
      
------------------------------------------------------------------------------------------------------------------

We need to get the following properties first:

For each row or col, we only need to flip it once or do not flip. (Flip 2, 4, 6,.. times is same as not flip; flip 1, 3, 5, .. times is same as flip once);
The order of flipping does not matter.
If after some flips, we can get the all-zero matrix. Then for each pair of rows (or cols), they must be exactly same (every element is the same) or completely different (every element is different).
1 and 2 are easier to get. How should we get 3?
Pay attention to the assumption: " If after some flips, we can get the all-zero matrix."
We can start from a matrix with all-zeros. Then we only need to flip some rows and cols and get the original matrix.

Let's start with flipping columns (from 2, we know the order does not matter). Let's assume magically, from the God's View, we know which k columns to flip. Let's flip the k columns first. Then what do we observe for each row?

Each row is same with others [with k 1s and (n-k) 0s]. Okay, then the only choice we have is to flip rows. If we flip one row, then it becomes a completely different row.

For example, [1, 0, 1] -> [0, 1, 0]. Only two conditions for each row. That is, in the orginal matrix, each pair of rows must be the same or completely different.

The code is easy ~~~~~

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        row_ori = grid[0]
        row_flip = [1 - x for x in grid[0]]
        
        for row in range(1, m):
            if grid[row] != row_ori and grid[row] != row_flip:
                return False
        
        return True
      
-----------------------------------------------------------------------------
# pre-processing: get the dimensions of grid:
	m, n = len(grid), len(grid[0])
    
	# loop through all columns in the first row. if its value
	# is 1, then flip all the values in that column:
    for ii in range(n):
        if grid[0][ii] == 1:
            
            for jj in range(m):
                grid[jj][ii] = (grid[jj][ii] + 1) % 2
    
	# after doing this procedure, each row should be 
	# [0,0,....0] or [1,1,1,....1]. so len(set(row)) should be 
	# equal to 1. if it's 2, then it's impossible to convert and return False:
    for row in grid:
        if len(set(row)) == 2:
            return(False)
    
	# if no Falses short-circuited this process, all rows 
	# can be made 0. So return True:
    return(True)	
      
      
