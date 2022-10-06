'''
You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.
'''

class Solution:
  def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

      m,n = len(isWater),len(isWater[0])
      q = collections.deque()
      dp = [[float('inf') for _ in range(n)] for _ in range(m)]
      for i in range(m):
          for j in range(n):
              if isWater[i][j]==1:
                  dp[i][j] = 0
                  q.append([i,j,0])

      while q:
          x,y,c = q.popleft()
          for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
              if 0<=x+i<m and 0<=y+j<n and dp[x+i][y+j]==float('inf'):
                  dp[x+i][y+j] = c+1
                  q.append([x+i,y+j,c+1])

      return dp
    
---------------------------------------------------------------------------
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        arr = collections.deque()
        m, n = len(isWater), len(isWater[0])
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    arr.append((0, i, j))
                    
        ans = [[-1] * n for _ in range(m)]
        while arr:
            val, x, y = arr.popleft() 
            if ans[x][y] != -1: continue
            ans[x][y] = val
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx, yy = x+dx, y+dy
                if 0 <= xx < m and 0 <= yy < n and ans[xx][yy] == -1:
                    arr.append((val+1, xx, yy))
        return ans
      
-------------------------------------------------------------------------------------
class Solution:
def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
    row, col = len(isWater), len(isWater[0])
    queue, visited = deque([]), set([])
    for x in range(row):
        for y in range(col):
            if isWater[x][y] == 1:
                isWater[x][y] = 0
                queue.append((x,y))
                visited.add((x,y))
    
    while queue:
        x, y = queue.popleft()
        for nx,ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
            if (nx,ny) in visited: continue
            if 0<=nx<row and 0<=ny<col:
                isWater[nx][ny] = isWater[x][y] + 1 
                visited.add((nx,ny))
                queue.append((nx,ny))
    
    return isWater
