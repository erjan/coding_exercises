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
                    
------------------------------------------------------------------------------------------------------------
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        res = 0

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row,col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    r,c = row+dr,col+dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c]== '1' and 
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    res+=1
        return res

