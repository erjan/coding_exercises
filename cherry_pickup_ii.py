'''
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.
'''


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.memo = {}
        return max(self.dfs(grid,0,0,0,n - 1), 0)
    
    def dfs(self,grid,i1,j1,i2,j2):
        if (i1,j1,i2,j2) in self.memo: return self.memo[(i1,j1,i2,j2)]
        m, n = len(grid), len(grid[0])
        #end cases
        if j1 == n or j2 == n or j1 == -1 or j2 == -1: return -float('inf')
        if i1 == m and i2 == m: return 0
         
        # 9 different next steps
        d1 = self.dfs(grid,i1 + 1,j1 - 1,i2 + 1,j2 - 1)
        d2 = self.dfs(grid,i1 + 1,j1 - 1,i2 + 1,j2)
        d3 = self.dfs(grid,i1 + 1,j1 - 1,i2 + 1,j2 + 1)
        d4 = self.dfs(grid,i1 + 1,j1 ,i2 + 1,j2 - 1)
        d5 = self.dfs(grid,i1 + 1,j1 ,i2 + 1,j2)
        d6 = self.dfs(grid,i1 + 1,j1 ,i2 + 1,j2 + 1)
        d7 = self.dfs(grid,i1 + 1,j1 + 1 ,i2 + 1,j2 - 1)
        d8 = self.dfs(grid,i1 + 1,j1 + 1,i2 + 1,j2)
        d9 = self.dfs(grid,i1 + 1,j1 + 1,i2 + 1,j2 + 1)
        max_res = max([d1,d2,d3,d4,d5,d6,d7,d8,d9])
        
        #if two robots step on same place
        if i1 == i2 and j1 == j2:
            res = max_res + grid[i1][j1]
        else:
            res = max_res + grid[i1][j1] + grid[i2][j2]
        self.memo[(i1,j1,i2,j2)] = res
        return res
# I really appreciate it if u vote up! （￣︶￣）↗

-------------------------------------------------------------------------------------------------------
