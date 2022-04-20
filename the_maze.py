'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).
'''

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(row, col):
			# 3 means seen
            maze[row][col] = 3
            for r, c in ((1, 0), (0, 1), (-1, 0), (0 ,-1)):
				# go until hitting walls
                nextR, nextC = row+r, col+c
                while 0<=nextR<rowL and 0<=nextC<colL and maze[nextR][nextC]!=1:
                        nextR, nextC = nextR+r, nextC+c
				# the node next the wall
                nextR, nextC = nextR-r, nextC-c
				# endpoint
                if maze[nextR][nextC]==2:
                    return True
				# change direction
                elif maze[nextR][nextC]!=3 and dfs(nextR, nextC):
                    return True
            return False
        rowL, colL = len(maze), len(maze[0])
		# 2 means endpoint
        maze[destination[0]][destination[1]] = 2
        return dfs(start[0], start[1])
      
--------------------------------------------------------------------------

Time complexity: O(n*m) where n is the number of rows in the maze and m the number of columns on the maze.
Space complexity: O(n*m) where n is the number of rows in the maze and m the number of columns on the maze.

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
		# If the start or the destination are not reachable return False
        if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
            return False
        
        # Since this is a BFS approach, we have to initialize a queue
		# with the starting coordinate, and set of visited coordinates
        visited = set()
        queue = [(start[0], start[1])]
        
		# Search while we have elements to iterate
        while queue:
			# Array to store next initial coordinates
            next_elements = []
			
			# Process the coordinates, if they have not been visited
            for x, y in queue:
                if not (x,y) in visited:
                    visited.add((x,y))
                    
					# From the current coordinate, search in 4 directions (up, down, left and right)
                    for i, j in [(+1,0), (-1, 0), (0, +1), (0, -1)]:
						# Get the next coordinate, this mean move in the given direction
                        next_x, next_y = x+i, y+j
						
						# While the coordinate is valid and the current element is zero, keep moving
						# This means we have not reached a wall
                        while 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == 0:
                            next_x += i
                            next_y += j
                        
						# Once we reach a wall, check if the previous coordinate is this direction is equal to the destination coordinate
						# If so, we have reached the goal
                        if destination[0] == next_x-i and destination[1] == next_y-j:
                            return True
							
						# If not add the previous coordinate is an starting point to perform BFS
                        next_elements.append((next_x-i, next_y-j))

			# Update the queue with the next elements
            queue = next_elements
        
		# Return false since we could not reach the destination coordinate 
        return False
    
--------------------------------------------------------------------

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = set() 
        queue = collections.deque([(start[0], start[1])])
        visited.add((start[0], start[1]))
        while queue:
            i, j = queue.popleft()
            if [i,j] == destination:
                return True
            for dx, dy in [(0,1), (0,-1), (1, 0), (-1, 0)]:
                new_x, new_y = i, j
                # look ahead one step to make sure the next space is valid
                while 0 <= new_x+dx < m and 0 <= new_y+dy < n and maze[new_x+dx][new_y+dy] == 0:
                    new_x += dx
                    new_y += dy
                # mark space as visited upon discovery
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return False
------------------------------------------------------

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        
        stack = [start]
        seen = {tuple(start)}
        while stack: 
            i, j = stack.pop()
            if [i, j] == destination: return True 
            for di, dj in (-1, 0), (0, -1), (0, 1), (1, 0): 
                ii, jj = i, j
                while 0 <= ii+di < m and 0 <= jj+dj < n and maze[ii+di][jj+dj] == 0: 
                    ii += di
                    jj += dj 
                if (ii, jj) not in seen: 
                    stack.append((ii, jj))
                    seen.add((ii, jj))
        return False 
------------------------------------------------------------

class Solution:        
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q, visited = deque([tuple(start)]), set()
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (-1,0), (0, -1), (1,0)]
        
        # Roll the ball until it hits a wall
        # and return its position.
        def roll(pos, d): 
            nextRow, nextCol = pos[0] + d[0], pos[1] + d[1]
            while nextRow >= 0 and nextCol >= 0 and \
                  nextRow < rows and nextCol < cols and \
                  maze[nextRow][nextCol] == 0:     
                nextRow, nextCol = nextRow + d[0], nextCol + d[1]
            nextRow, nextCol = nextRow - d[0], nextCol - d[1]
            return nextRow, nextCol
        
        # For all the nodes in the maze...
        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            # Roll the ball until it hits a wall...
            for d in directions:
                nei = roll(node, d)
                # If the ball lands on destination...
                if nei == tuple(destination):
                    return True
                q.append(nei)
            
        return False         
      
-----------------------------------------------------------------------------------------

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        def get_pos(r, c):
            pos = []
            for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                nr, nc = r, c
                while (0 <= nr+x < M) and (0 <= nc+y < N) and maze[nr+x][nc+y] == 0:
                    nr += x
                    nc += y
                pos.append((nr, nc))
            return pos
        
        M, N = len(maze), len(maze[0])
        queue, visited = deque([start]), set(tuple(start))
        while queue:
            r, c = queue.popleft()
            if [r, c] == destination:
                return True
            for nr, nc in get_pos(r, c):
                if (nr, nc) not in visited:
                    queue.append([nr, nc])
                    visited.add((nr, nc))
        return False
----------------------------------------------------------------------------      
      
      
      
