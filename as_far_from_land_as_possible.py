'''
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
'''

def maxDistance(self, grid):
		
        rows = len(grid)
        if rows == 0:
            return -1
        
        cols = len(grid[0])
        lands = collections.deque()
        
        maxDistance = 0
        
		# Cover up all the lands and say there nearest distance to themselves is = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    lands.append([(i,j), 0])
                    
        while lands:
            for _ in range(len(lands)):
			
				# Get the node and the distance value corresponding to it
                temp = lands.popleft()
                x,y = temp[0] 
                d = temp[1]
				
				# Keep a global maxDistance check
                maxDistance = max(maxDistance, d)
                
                # Explore everything around the given land mass
				for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + dx, y + dy
                    
					# Simple edge cases tested
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    
					# If you find a sea around it
                    if grid[xx][yy] == 0:
					
						# Mutate and append
						grid[xx][yy] = d + 1
                        lands.append([(xx, yy), d + 1])
                        
        return maxDistance or -1
------------------------------------------------------------------------------------------
class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dq = deque((i, j) for i in range(n) for j in range(n) if grid[i][j])
        res = 0

        while dq:
            r0, c0 = dq.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r1, c1 = r0 + dr, c0 + dc
                if 0 <= r1 < n and 0 <= c1 < n and not grid[r1][c1]:
                    dq.append((r1, c1))
                    grid[r1][c1] = grid[r0][c0] + 1
                    res = max(res, grid[r1][c1])

        return res - 1
