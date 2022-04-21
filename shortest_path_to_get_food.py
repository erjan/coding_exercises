'''
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.
'''

Explanation
Intuition: We need to find the shortest path from one point to the other. Pretty obvious hint of BFS.
First, we need to find where to start. O(m*n)
Starting BFS with the help of deque (i, j, cnt), explore 4 neighbors and increment cnt by 1
Mark visited point as X to avoid revisit
If # is met, return cnt
Time: O(m*n)
Space: O(m*n)
Implementation
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*': 
                    q.append((i,j, 0)); break
            if q: break        
        while q:
            x, y, cnt = q.popleft()
            if grid[x][y] == 'X': continue
            elif grid[x][y] == '#': return cnt
            grid[x][y] = 'X'
            for i, j in [(x + _x, y + _y) for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
                if 0 <= i < m and 0 <= j < n and grid[i][j] != 'X':
                    q.append((i, j, cnt + 1))
        return -1            
----------------------------------------------------------------------

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # Get parameters
        rows = len(grid)
        cols = len(grid[0])

        # Find the start cell
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '*':
                    start_row = row
                    start_col = col

        # Initialization for Breadth First Search
        state = (start_row, start_col)
        steps = 0
        queue = deque([(state, steps)])
        visited = set(state)

        # Start BFS traverse
        while queue:

            # Get the current state and steps
            (curr_row, curr_col), steps = queue.popleft()

            # If it found a pizza, return the number of steps so far.
            # This steps is guaranteed to be the minimum steps because we use BFS
            if grid[curr_row][curr_col] == '#':
                return steps

            # We haven’t found a pizza yet, so go to another cell to find it
            for next_row, next_col in [
                (curr_row + 1, curr_col),
                (curr_row - 1, curr_col),
                (curr_row, curr_col + 1),
                (curr_row, curr_col - 1)
            ]:

                # We can go if the next cell is in the grid, a free space, not visited yet, and either a free space or pizza place
                if 0 <= next_row < rows \
                        and 0 <= next_col < cols \
                        and grid[next_row][next_col] in ['O', '#'] \
                        and (next_row, next_col) not in visited:
                    next_state = (next_row, next_col)
                    # Append the next_state to queue and visit to allow BFS to happen
                    queue.append((next_state, steps + 1))
                    visited.add(next_state)

        # Otherwise, it wasn’t able to find a pizza, meaning no parth to find the pizza so return -1
        return -1
-------------------------------------------------------------------------------------

from collections import deque


def getCurrentPosition(grid, locationMarker='*'):
    """
    Return the row and col coordinates of my location
    """
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == locationMarker:
                return (row, col)
    return -1


def getGridMarker(location, grid):
    """Return marker in grid at given location"""
    return grid[location[0]][location[1]]


def findValidLocations(location, grid):
    """
    Return all valid locations next to the provided location
    """
    r, c = location
    allDirections = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    
    return [(i, j) for i, j in allDirections
            if 0 <= i < len(grid) and 0 <= j < len(grid[0])
            and getGridMarker((i,j), grid) in ('O', '#')]

    

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        myLocation = getCurrentPosition(grid)
        
        grid[myLocation[0]][myLocation[1]] = -1 # Mark as visted
        
        # Implement a BFS to find food
        queue = deque([(myLocation, 1)])  #  (location, currentSteps)
        
        while queue:
            location, steps = queue.pop()
             
            for adjLocation in findValidLocations(location, grid):
                gridMarker = getGridMarker(adjLocation, grid)
                
                if gridMarker == "#":
                    return steps
                
                grid[adjLocation[0]][adjLocation[1]] = -1 # Mark as visted
                queue.appendleft((adjLocation, steps + 1))
                
        
        return -1
----------------------------------------------------------------------------------------

Use BFS to find the shortest path to a food from the start position. Store the number of steps it takes to get to the destination in the queue.

Time complexity: O(M * N)
Space complexity: O(M * N)

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        def getStartPos():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == "*":
                        return (i, j)
                    
        startX, startY = getStartPos()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False for c in range(n)] for r in range(m)]
        visited[startX][startY] = True
        q = collections.deque([(0, startX, startY)])
        
        while q:
            steps, x, y = q.popleft()
            
            if grid[x][y] == "#":
                return steps
            
            for dX, dY in dirs:
                nX, nY = x + dX, y + dY
                
                if m > nX >= 0 <= nY < n and grid[nX][nY] != "X" and not visited[nX][nY]:
                    visited[nX][nY] = True
                    q.append((steps+1, nX, nY))
        
        return -1
--------------------------------------------------------------------------------------

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        directions = [(-1,0), (0,-1), (1,0),(0,1)]
        m = len(grid)
        n = len(grid[0])
        def bfs(i,j):
            queue = deque([(i,j, 0)])
            
            while queue:
                currX, currY, step = queue.popleft()
                for x, y in directions:
                    nX = currX + x
                    nY = currY + y
                    
                    if 0<=nX<m and 0<=nY<n and grid[nX][nY] != 'X':
                        if grid[nX][nY] == '#':
                            return step+1
						# Mark the cell as visited
                        grid[nX][nY] = 'X'
                        queue.append((nX, nY, step+1))
            return - 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    return bfs(i,j)
        return -1
      
      
      
      
      
