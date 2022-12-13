'''
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
 
 '''


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        #Go down or go right
        directions = [(1, 0), (0, 1)]
        
        #Enables cache for our dp
        @lru_cache(None)
        def dp(row_1, row_2, col_1, col_2):
            
            #if we hit a wall or we go out of the grid
            if col_1 >= cols or col_2 >= cols or row_1 >= rows or row_2 >= rows or grid[row_1][col_1] == -1 or grid[row_2][col_2] == -1:
                return -inf
            #Pick current cherries
            result = grid[row_1][col_1]
            
            #Do not double cherries if both paths are the same
            if col_1 != col_2 or row_1 != row_2:
                result += grid[row_2][col_2]
            
            # If we are at the end of the grid stop
            if not (row_1 == rows - 1 and col_1 == cols - 1):
                result += max(dp(new_row_1 + row_1, new_row_2 + row_2, new_col_1 + col_1, new_col_2 + col_2) 
                              for new_row_1, new_col_1 in directions
                              for new_row_2, new_col_2 in directions)
            
            return result
        
        ans = dp(0, 0, 0, 0)
        return 0 if ans == -inf else ans
            
------------------------------------------------------------------------------------------------------------------------
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if N == 1:
            return grid[0][0]
        memo = {}
        self.pickCherry2(grid,N,0,0,0,0,memo)
        print(memo)
        if len(memo) == 0 or memo[(0,0,0,0)] < 0:
            return 0
        return  memo[(0,0,0,0)]
    
    def pickCherry2(self, grid, N, x0, y0, x1, y1, memo):
        
        if x0 >= N or y0 >= N or x1 >= N or y1 >= N :
            return float('-inf') 
        
        if (x0, y0, x1, y1) in memo:
            return memo[(x0, y0, x1, y1)]
        
        if grid[x0][y0] == -1 or grid[x1][y1] == -1:
            return float('-inf')
        
        elif x0 == x1 and y0 == y1:
            cherryPicked = grid[x1][y1]
        else :
            cherryPicked = grid[x0][y0] + grid[x1][y1]
        
        #print(x0, y0, x1, y1 , cherryPicked)
        if x0 == N-1 and y0 == N-1 :
            return grid[x0][y0]
        if x1 == N-1 and y1 == N-1 :
            return grid[x1][y1]
            
        cherryPicked += max([self.pickCherry2(grid,N,x0+1,y0,x1+1,y1,memo),
                             self.pickCherry2(grid,N,x0+1,y0,x1,y1+1,memo),
                             self.pickCherry2(grid,N,x0,y0+1,x1+1,y1,memo),
                             self.pickCherry2(grid,N,x0,y0+1,x1,y1+1,memo)])
        
        memo[(x0, y0, x1, y1)] = cherryPicked
        
        return cherryPicked
          
