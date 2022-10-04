'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.
'''


class Solution:
def closedIsland(self, grid: List[List[int]]) -> int:
    
    def dfs(i,j):
        if grid[i][j]==1:
            return True
        if i<=0 or i>=m-1 or j<=0 or j>=n-1:
            return False
        grid[i][j]=1
        up=dfs(i-1,j)
        down=dfs(i+1,j)
        left=dfs(i,j-1)
        right=dfs(i,j+1)
        return left and right and up and down
     
    m,n = len(grid),len(grid[0])
    c=0
	# iterate through the grid from 1 to length of grid for rows and columns.
    # the iteration starts from 1 because if a 0 is present in the 0th column, it can't be a closed island.
    for i in range(1,m-1):
        for j in range(1,n-1):
			# if the item in the grid is 0 and it is surrounded by
            # up, down, left, right 1's then increment the count.
            if grid[i][j]==0 and dfs(i,j):
                c+=1
    return c
--------------------------------------------------------------------------------------------------------------------
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ## RC ##
        ## APPROACH : DFS ##
        ## LOGIC ##
        ## 1. Find, Islands just like normal Leetcode 200. Number of Islands problem.
        ## 2. While doing so, check if every land block, is not in the border.
        ## 3. If it is in the border, mark that Island as Invalid island and after traversal donot include in the count
        
        def dfs( i, j, visited):
            
            if( (i,j) in visited ):
                return
            
            if not self.inValidIsland and ( i== 0 or j == 0 or i == m-1 or j == n-1 ):
                self.inValidIsland = True
            
            visited.add((i,j))
            
            for x,y in directions:
                if 0 <= i+x < m and 0 <= j+y < n and grid[i+x][j+y] == 0:
                    dfs( i+x, j+y, visited )
        
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        count, visited = 0, set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(m):
            for j in range(n):
                self.inValidIsland = False
                if (i,j) not in visited and grid[i][j] == 0:
                    dfs( i, j, visited )
                    count = count + (1 if( not self.inValidIsland ) else 0)
        return count
      
-----------------------------------------------------------------------------------------------------------
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count =0
        
        # iterate through the grid from 1 to length og grid for rows
        # and columns.
        # the iteration starts from 1 because if a 0 is present
        # in the 0th column, it can't be a closed island.
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                
                # if the item in the grid is 0 and it is surrounded by
                # up, down, left, right 1's then increment the count.
                if grid[i][j] == 0 and self.dfs(grid, i , j):
                    count +=1
        return count
    
    def dfs(self, grid, i, j):
        
        # if grid[i][j] is 1 then return True, this helps is checking the
        # final return conditons.
        if grid[i][j]==1:
            return True
        
        # now check if the element 0 is present at the outmost rows and column
        # then return False
        if i<=0 or j<=0 or i>=len(grid)-1 or j >=len(grid[0])-1:
            return False
        
        # initialize the item as 1
        grid[i][j] = 1
        
        # now check the conditions for up, down, left, right
        up = self.dfs(grid, i+1, j)
        down = self.dfs(grid, i-1, j)
        right = self.dfs(grid, i, j+1)
        left = self.dfs(grid, i, j-1)
        
        # if up, down , left, right is True, then return to main function
        return up and down and left and right
