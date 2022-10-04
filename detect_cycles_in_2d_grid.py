'''
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.
'''

#my bad code
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        
        m = len(grid)
        n = len(grid[0])
        visited = set()
        direc = [(1,0),(0,1),(-1,0),(0,-1)]
        
        
        def dfs(i,j,grid,m,n,cur_val, maxlen):
        
            if maxlen >=4 and cur_val == grid[i][j]:
                return True
            for i in range(m):

                for j in range(n):

                    if grid[i][j] not in visited:
                        visited.add(grid[i][j])
                        
                    if cur_val == grid[i][j]:
                        for dx,dy in direc:
                            dfs(i+dx,j+dy, grid,m,n,cur_val,maxlen+1)
            return False
                        
        
        
        return dfs(0,0,grid,m,n,grid[0][0], 0)
        
----------------------------------------------------------------------------------------------------------------------
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = {} # visited cell: enter direction
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    dq = deque([(i,j)])
                    visited[(i,j)] = {(0,0)}
                    while dq:
                        i,j = dq.pop()
                        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                            if (di*-1,dj*-1) not in visited[(i,j)]: # this makes sure that we don't go back to the immediate cell where we left off 
                                if 0<=i+di<len(grid) and 0<=j+dj<len(grid[0]) and grid[i+di][j+dj] == grid[i][j]:
                                    if (i+di,j+dj) not in visited:
                                        visited[(i+di,j+dj)] = set()
                                        visited[(i+di,j+dj)].add((di,dj))
                                        dq.append((i+di,j+dj))
                                    else:
                                        return True
        return False 
      
--------------------------------------------------------------------------------------------------------

class DSU:
    def __init__(self,m,n):
        self.par = {(i,j):(i,j) for i in range(m) for j in range(n)}
    
    def find(self,x):
        if self.par[x]!=x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        xp,yp = self.find(x),self.find(y)
        if xp == yp:
            return False
        self.par[xp] = yp
        return True

dirs = [(0,1),(1,0)]
class Solution:
    def containsCycle(self, grid):
        R,C = len(grid),len(grid[0])
        dsu = DSU(R,C)        
        for r in range(R):
            for c in range(C):
                for x,y in dirs:
                    nr,nc = r+x,c+y
                    if 0<=nr<R and 0<=nc<C and grid[r][c] == grid[nr][nc]:
                        if dsu.union((r,c),(nr,nc)) == False:
                            return True
        return False
      
-------------------------------------------------------------------------------------------------------------------------

class Solution:
    def containsCycle(self, A: List[List[str]]) -> bool:
        R, C = len(A), len(A[0])
        visited = set()
        
        def neighbors(r, c):
            return [(i, j) for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] if 0 <= i < R and 0 <= j < C and A[i][j] == A[r][c]]
        
        def dfs(r, c, x, prev, seen):
            if (r, c) in seen:
                return True
            seen.add((r, c))
            visited.add((r, c))

            for i, j in neighbors(r, c):
                if not prev or prev != (i, j):
                    if dfs(i, j, x, (r, c), seen):
                        return True
            return False
            
        
        for r in range(R):
            for c in range(C):
                if (r, c) not in visited:
                    seen = set()
                    if dfs(r, c, A[r][c], None, seen):
                        return True
        return False
