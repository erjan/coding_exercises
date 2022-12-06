'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
'''


class Solution:
    DIRECTIONS = (-1, 0), (1, 0), (0, -1), (0, 1)
    
    def neighbours(self, i, j):
        return ((i + di, j + dj) for di, dj in Solution.DIRECTIONS
                if 0 <= i + di < self.n and 0 <= j + dj < self.n)
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        area = collections.Counter()
        
        def dfs(i, j, groupNumber):
            if grid[i][j] != 1:
                return
            
            grid[i][j] = groupNumber
            area[groupNumber] += 1
            for ni, nj in self.neighbours(i, j):
                dfs(ni, nj, groupNumber)
        
        groupNumber = 2
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell != 1:
                    continue
                dfs(i, j, groupNumber)
                groupNumber += 1
        
        if not area:
            return 1
        res = max(area.values())
        
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    continue
                neighbourGroups = {grid[ni][nj] for ni, nj in self.neighbours(i, j)}
                res = max(res, 1 + sum(area[group] for group in neighbourGroups))
        
        return res
      
---------------------------------------------------------------------------------------------
class UnionFind:
  def __init__(self):
    self.root = {}
  def findOrAdd(self, a):
    if a not in self.root:
      self.root[a] = a
      return a
    if self.root[a] == a:
      return a
    self.root[a] = self.findOrAdd(self.root[a])
    return self.root[a]
  def unite(self, a, b):
    ra = self.findOrAdd(a)
    rb = self.findOrAdd(b)
    if ra == rb:
      return ra
    self.root[ra] = rb
    return rb

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
      n = len(grid)
      uf = UnionFind()
      diff = [(-1,0),(1,0),(0,-1),(0,1)]
      for i in range(n):
        for j in range(n):
          if grid[i][j] == 1:
            uf.findOrAdd((i, j))
      for i in range(n):
        for j in range(n):
          if grid[i][j] == 1:
            for dx, dy in diff:
              x, y = i+dx, j+dy
              if x >= 0 and x < n and y >= 0 and y < n and grid[x][y] == 1:
                uf.unite((i, j), (x, y))
      counter = {}
      for i in range(n):
        for j in range(n):
          if grid[i][j] == 1:
            r, c = uf.findOrAdd((i, j))
            counter[(r, c)] = counter.get((r, c), 0) + 1
      res = 0
      for _, count in counter.items():
        res = max(res, count)
      for i in range(n):
        for j in range(n):
          if grid[i][j] == 0:
            st = set()
            for dx, dy in diff:
              x, y = i+dx, j+dy
              if x >= 0 and x < n and y >= 0 and y < n and grid[x][y] == 1:
                r, c = uf.findOrAdd((x, y))
                st.add((r, c))
            count = 1
            for r, c in st:
              count += counter[(r, c)]
            res = max(res, count)
      return res
    
-------------------------------------------------------------------------------------------
class Solution:
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != 1:
            return 0
        grid[row][col] = 2
        x1 = self.dfs(grid, row-1, col)
        x2 = self.dfs(grid, row, col-1)
        x3 = self.dfs(grid, row+1, col)
        x4 = self.dfs(grid, row, col+1)
        return 1 + x1 + x2 + x3 + x4
        
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    ans = max(ans, self.dfs(grid, i, j))
                    grid[i][j] = 0
                    for k in range(m):
                        for l in range(n):
                            if grid[k][l] == 2:
                                grid[k][l] = 1
        return ans if ans > 0 else n*n
