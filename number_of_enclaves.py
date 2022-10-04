'''
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
'''

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
		#step2 - function to change ones
        def dfs(r, c) :
            if grid[r][c] == 1 :
                grid[r][c] = '$'
                if r-1 >= 0 : dfs(r-1, c)
                if r+1 < rows : dfs(r+1, c)
                if c-1 >= 0 : dfs(r, c-1)
                if c+1 < cols : dfs(r, c+1)
        #step1 - change boundary ones and those connected ones to them (as only these one's can walk off the boundary)   
        for i in range(rows) :
            for j in range(cols) :
                if i == 0 or j == 0 or i == rows-1 or j == cols-1 and grid[i][j] == 1 :
                    dfs(i, j)
        #step3 - Remaining ones will be our answer
        ans = 0
        for i in range(rows) :
            for j in range(cols) :
                if grid[i][j] == 1 :
                    ans += 1
        
        return ans
