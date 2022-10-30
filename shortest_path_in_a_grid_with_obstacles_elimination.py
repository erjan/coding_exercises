'''
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
'''

class Solution(object):
    
    def search(self, cur, i, j, grid, k):
        # invalid position
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
            return
        # not enough k
        if k == 0 and grid[i][j] == 1:
            return
        # has been visited
        if grid[i][j] == 2:
            return
        # has got the best path, pruning
        if self.rst == len(grid) + len(grid[0]) - 2:
            return
        # valid path
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            self.rst = min(self.rst, cur)
            return
        c = grid[i][j]
        # mark the visited position
        grid[i][j] = 2
        if c == 1:
            k -= 1
        # always try to go right or down first
        self.search(cur + 1, i + 1, j, grid, k)
        self.search(cur + 1, i, j + 1, grid, k)
        self.search(cur + 1, i - 1, j, grid, k)
        self.search(cur + 1, i, j - 1, grid, k)
        grid[i][j] = c


    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        self.rst = float('inf')
        self.search(0, 0, 0, grid, k)
        return self.rst if self.rst != float('inf') else -1
      
------------------------------------------------------------------------------------------------
def shortestPath(self, grid: List[List[int]], k: int) -> int:
   trgtX , trgtY = len(grid)-1, len(grid[0])-1
   if trgtX == trgtY == 0:
   	return 0

   if k > trgtX + trgtY:
   	return trgtX + trgtY

   from collections import deque
   q = deque()
   q.append((0,0,0,k))
   visited = {(0,0): 0}
   dirs = [(1,0), (0,1), (-1,0), (0,-1)]
   while q:
   	x, y, r, k = q.popleft()
   	for dir in dirs:
   		newX, newY = x+dir[0], y+dir[1]
   		if newX >= 0 and newX <= len(grid)-1 and newY >= 0 and newY <= len(grid[0])-1:
   			if (newX, newY) == (trgtX, trgtY):
   				return r+1
   			# traverse one layer further
   			if grid[newX][newY] == 1:
   				if k:
   					if (newX, newY) not in visited or ( (newX, newY) in visited and visited[(newX,newY)] < k-1 ): # --- NOTE [1]
   						q.append((newX, newY, r+1, k-1))
   						visited[(newX, newY)] = k-1
   			else:
   				if (newX, newY) not in visited or ( (newX, newY) in visited and visited[(newX,newY)] < k ):
   					q.append((newX, newY, r+1, k))
   					visited[(newX, newY)] = k
   return -1


# NOTE [1]
# --------
# if prev cell had less remaming passes, then we should give this path a chance since it has more passes
# even though the raduis is bigger
