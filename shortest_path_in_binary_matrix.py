'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
'''

import collections
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        visited = set((0, 0))
        queue = collections.deque([(0, 0, 1)])
        
        while queue:
            x, y, level = queue.popleft()
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1): return level
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == 0 and (x + dx, y + dy) not in visited:
                    visited.add((x + dx, y + dy))
                    queue.append((x + dx, y + dy, level + 1))
            
        return -1
      
-------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:                
        n = len(grid)
                
        if grid[0][0] == 1:
            return -1
        
        q = [(0,0,1)]#min length is 1                
        while len(q) > 0:
            x,y,d = q.pop(0)
            
            if x== n-1 and y == n-1:
                return d
            
            directions = [(x-1,y-1), (x+1,y+1),(x-1,y), (x+1,y), (x,y+1), (x,y-1),(x-1,y+1), (x+1,y-1)]
            
            for a,b in directions:
                if 0<=a<n and 0<=b<n and grid[a][b] == 0:
                    grid[a][b] = 1
                    q.append((a,b,d+1))
        return -1
            
  
