'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''


# Set + Recursion Solution
# Time:     O(n * m),     Iterates through grid once.
# Space:    O(n * m),     Uses set to keep track of visited indices.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])                                          # Gets size of grid.        
        visited = set()                                                         # Set containing a tuple if indices visited in grid.
        
        def isValidIndice(row: int, column: int) -> bool:                       # Chekcs if a row and column are in the grid.
            if row < 0 or M <= row: return False                                # Checks for out of bounds row.
            if column < 0 or N <= column: return False                          # Checks for out of bounds column.
            
            return True                                                         # Returns True if all checks are passed.
        
        def islandArea(row, column) -> int:                                     # Gets the area of a 4-connected island on the grid. 
            if (row, column) in visited: return 0                               # Checks if indices have been visited already.
            if not isValidIndice(row, column): return 0                         # Checks if the indice is in bounds.
            if grid[row][column] == 0: return 0                                 # Checks if cell is water.
            
            visited.add((row, column))                                          # Adds cell to visited set.
            up, down = islandArea(row-1, column), islandArea(row+1, column)     # Recursive call to cells above and below to get area.
            left, right = islandArea(row, column-1), islandArea(row, column+1)  # Recursive call to cells left and right to get area.
            
            return 1 + up + down + left + right                                 # returns the area of the island.
            
            
        area, maxArea = 0, 0
        for row in range(M):                                                    # Iterates through grid rows.
            for column in range(N):                                             # Iterates through grid columns.
                area = islandArea(row, column)                                  # Gets area of island if cell is 1.
                maxArea = max(maxArea, area)                                    # Sets max island area found.
                
                
        return maxArea   
      
--------------------------------------------------------------------------------------------------------------------------
# Recursion Solution
# Time:     O(n * m),     Iterates through grid once.
# Space:    O(1),         Constant space used by mutating the input list to track visited cells.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])                                          # Gets size of grid.        
        
        
        def isValidIndice(row: int, column: int) -> bool:                       # Chekcs if a row and column are in the grid.
            if row < 0 or M <= row: return False                                # Checks for out of bounds row.
            if column < 0 or N <= column: return False                          # Checks for out of bounds column.
            
            return True                                                         # Returns True if all checks are passed.
        
        
        def islandArea(row, column) -> int:                                     # Gets the area of a 4-connected island on the grid. 
            if not isValidIndice(row, column): return 0                         # Checks if the indice is in bounds.
            if grid[row][column] == 0: return 0                                 # Checks if cell is water or has been visited.
            
            grid[row][column] = 0                                               # Sets cell value to 0 to indicate its been visited.                                        
            up, down = islandArea(row-1, column), islandArea(row+1, column)     # Recursive call to cells above and below to get area.
            left, right = islandArea(row, column-1), islandArea(row, column+1)  # Recursive call to cells left and right to get area.
            
            return 1 + up + down + left + right                                 # returns the area of the island.
            
            
        area, maxArea = 0, 0
        for row in range(M):                                                    # Iterates through grid rows.
            for column in range(N):                                             # Iterates through grid columns.
                area = islandArea(row, column)                                  # Gets area of island if cell is 1.
                maxArea = max(maxArea, area)                                    # Sets max island area found.
                
                
        return maxArea  
-------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0
        # Search our grid looking for islands.
        for row in range(rows):
            for col in range(cols):
			# If we find and island, continue searching it.
                if grid[row][col] == 1:
                    area = 1
					# Mark the locations we've searched so we don't recount them.
                    grid[row][col] = '#'
                    q = collections.deque([])
                    q.append((row, col))
                    while q:
                        r, c = q.popleft()
						# Search all of the possible next locations based on our move directions.
                        for y, x in directions:
						    # new row and col = current + the new movement direction.
                            nr = r + y
                            nc = c + x
							# If the new location is valid: within the grid and contains more island (1)
                            if nr < rows and nr >= 0 and nc < cols and nc >= 0 and grid[nr][nc] == 1:
							    # Update the current islands area, mark as searched and add to the deque.
                                area += 1
                                grid[nr][nc] = '#'
                                q.append((nr, nc))
                    # Once we finish exploring the island, check if it's area is the largest we've seen thus far.
                    max_area = max(max_area, area)
                   
        return max_area
      
