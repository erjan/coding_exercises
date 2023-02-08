'''
You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).

You can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).

Return true if it is possible to make the matrix disconnect or false otherwise.

Note that flipping a cell changes its value from 0 to 1 or from 1 to 0.
'''



'''
Intuition
If there exist a point (i, j) which is not (0, 0) or (m-1, n-1), such that the number of the paths from (0, 0) to (m-1, n-1) go through (i, j)equals the number of paths from (0, 0) to (m-1, n-1) without any constraint, return True.

Approach
To count the numbers of paths go through (i, j). We just calculate number of paths from (0, 0) to (i, j) and number of paths from (i, j) to (m-1, n-1), then multiply them up.
'''


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        #  number of paths from (0, 0) to (i, j)
        dp1 = [[0] * (n+1) for _ in range(m + 1)]
        dp1[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i-1][j-1]:
                    dp1[i][j] += dp1[i-1][j] + dp1[i][j-1]
        
        #  number of paths from (i, j) to (m-1, n-1)      
        dp2 = [[0] * (n+1) for _ in range(m + 1)]
        dp2[-2][-2] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    dp2[i][j] += dp2[i+1][j] + dp2[i][j+1]
        
        # number of paths from (0, 0) to (m-1, n-1)     
        target = dp1[-1][-1]

        for i in range(m):
            for j in range(n):
                if (i!=0 or j!=0) and (i!=m-1 or j!=n-1):
                    if dp1[i+1][j+1] * dp2[i][j] == target: 
                        return True
        return False
      
--------------------------------------------------------------------------------------------------------
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        
        M = len(grid)
        N = len(grid[0])

        #visited set, to not visit the same nodes again
        v= set()

        dirs=[[0,1],[1,0]]

        path = set()
        
        v.add((0,0))
        path.add((0,0))
        
        def dfs(x,y):
            
            if x == M -1 and y == N -1:
                return True
            
            for d in dirs:
                nx = x + d[0]
                ny = y + d[1]
                
                if nx < M and ny < N and (nx,ny) not in v and grid[nx][ny] == 1:
                    v.add((nx,ny))
                    path.add((nx,ny))
                    if dfs(nx,ny):
                        return True
                    path.remove((nx,ny))
            return False

        # 1 do a dfs from (0,0) to (M-1,N-1) 
        res =  dfs(0,0)
        
        # if there is no path the it's already disconnectd, return True
        if not res:
            return True
        
        # remove the first and last node from the path
        path.remove((0,0))
        path.remove((M-1,N-1))
        
        # 2 remove the path from the grid
        for p in path:
            grid[p[0]][p[1]] = 0
        
        #reset the visited set
        v= set()
        v.add((0,0))

        # 3 try again DFS, if it's not connected, return True
        return not dfs(0,0)
        
        
--------------------------------------------------------------------------------------------------------
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n, used = len(grid), len(grid[0]), set()
        def dfs(x, y):
            nonlocal m, n
            if x == m - 1 and y == n - 1: return True
            if x + y: used.add((x, y))
            if x + 1 < m and grid[x + 1][y] and (x + 1, y) not in used and dfs(x + 1, y): return True
            if y + 1 < n and grid[x][y + 1] and (x, y + 1) not in used and dfs(x, y + 1): return True
            return False
        return not (dfs(0, 0) and dfs(0, 0))
