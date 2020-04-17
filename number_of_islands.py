'''
Given a 2d grid map 
of '1's (land) and '0's (water), count the 
number of islands. An island is surrounded by water 
and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(self,grid,x,y,r,c):
            if x < 0 or x >=r or y < 0 or y >= c or grid[x][y] != '1':
                return None
            else:
                grid[x][y]= '2'

                helper(self,grid,x+1,y,r,c)
                helper(self,grid,x-1,y,r,c)
                helper(self,grid,x,y+1,r,c)
                helper(self,grid,x,y-1,r,c)
        
        rows = len(grid)
        if rows == 0:
            return 0
        columns = len(grid[0])
        num_islands = 0
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]=='1':
                    num_islands +=1
                    helper(self,grid,i,j,rows,columns)
        return num_islands
                    
        
