'''
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.
'''

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # Divide each square into 4 triangles
        uf = UnionFind(4 * n * n) 
        
        for row in range(n):
            for col in range(n):
                cell = grid[row][col]
                index = 4 * (row * n + col) 
                
                # When there are no lines in the square
                if cell == ' ':
                    uf.union(index+0, index+1)
                    uf.union(index+1, index+2)
                    uf.union(index+2, index+3)
                # When there's a bottom left - top right diagonal line dividing the square
                if cell == '/':
                    uf.union(index+0, index+3)
                    uf.union(index+1, index+2)
                # When there's a top left - bottom right diagonal line dividing the square
                if cell == '\\':
                    uf.union(index+2, index+3)
                    uf.union(index+0, index+1)
                # Connecting a square with square below it
                if row < n - 1:
                    uf.union(index+2, (index + 4*n) + 0)
                # Connecting a square with right side square
                if col < n - 1:
                    uf.union(index+1, (index + 4) + 3)
                    
        output = 0
        for i in range(4*n*n):
            if uf.find(i) == i:
                output += 1
        return output
      
------------------------------------------------------------------------------------------------------
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        def check(x,y,t):
            if x>=0 and y>=0 and x<row and y<col and (x,y,t) not in visited:
                return True
            return False
        
        row,col=len(grid),len(grid[0])
        visited=set()
        
        def dfs(r,c,t):
            if check(r,c,t):
                visited.add((r,c,t))
                if t==1:
                    dfs(r,c+1,3)# going right
                elif t==2:
                    dfs(r+1,c,0)# going down
                elif t==3:
                    dfs(r,c-1,1) # going back
                elif t==0: 
                    dfs(r-1,c,2)# going up
                if grid[r][c]!="/":
                    dfs(r,c,t^1) #trick to traverse 0 to 1 or 3 to 2 and viceversa
                if grid[r][c]!="\\":
                    dfs(r,c,t^3)#trick to traverse 3 to 0 or 1 to 2 and viceversa
        
        cntofregion=0
        for i in range(row):
            for j in range(col):
                for typ in range(4):
                    if (i,j,typ) not in visited:
                        dfs(i,j,typ)
                        cntofregion+=1
        return cntofregion   
