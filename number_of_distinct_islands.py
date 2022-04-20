'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.
'''

# Similar to LC 200 Number of Islands
def numDistinctIslands(self, grid: List[List[int]]) -> int:
	def dfs(start, shape, i, j):
		if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and grid[i][j] == 1:
			shape.append((i-start[0], j-start[1])) # track shape using starting coords
			grid[i][j] = 0 # make sure we don't visit again
			dfs(start,shape,i+1,j)
			dfs(start,shape,i-1,j)
			dfs(start,shape,i,j+1)
			dfs(start,shape,i,j-1)
		return shape

	unique_islands, islands = set(), 0

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				island = tuple(dfs((i,j), [], i, j)) # shape of island we just visited
				if island not in unique_islands:
					unique_islands.add(island)
					islands += 1
	return islands

---------------------------------------------------

So basically, the way we're going to approach this problem is by running a DFS for every island. While we run the DFS on an island, we're going to keep track of the path which will be translated back depending on the coordinates of the root (the coordinates at which DFS was initiated). After getting the path of the island, we will add it to a set so that at the end, we will be able to return the length of the set which will be equivilant to returning the number of distinct islands.

Below is the code. Please let me know if you have any questions or comments!

class Solution:
    def _dfs(self, grid, i, j, path, rootI, rootJ):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return path
        
        grid[i][j] = 0
        path.append((i - rootI, j - rootJ))
        self._dfs(grid, i, j+1, path, rootI, rootJ) # right
        self._dfs(grid, i+1, j, path, rootI, rootJ) # down
        self._dfs(grid, i, j-1, path, rootI, rootJ) # left
        self._dfs(grid, i-1, j, path, rootI, rootJ) # up
        return path
    
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinctIslands = set()
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num:
                    path = []
                    distinctIslands.add(tuple(self._dfs(grid, i, j, path, i, j)))
        return len(distinctIslands)
--------------------------------------------------------------

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [[1,0],[0,1],[-1,0],[0,-1],]
        patterns = []
        path = []
        I = 0
        J = 0
        def explore(i,j):            
            visited[i][j]=True
            for dir_ in directions:
                i_=i+dir_[0]
                j_=j+dir_[1]
                if i_<m and i_>=0 and j_<n and j_>=0 and not visited[i_][j_] and grid[i_][j_]==1:
                    path.add((i_-I,j_-J))
                    explore(i_,j_)
                
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]==1:
                    path=set([(0,0)])
                    I=i
                    J=j
                    explore(i,j)
                    if path not in patterns:
                        patterns.append(path)
        return len(patterns)
------------------------------------------------------------------------------------

The intution of behind this problem is tricky, below i explain it.

we are tasked with counting the number of distinct islands. two islands are said to be be same as eachother if they can be translated (not rotated, or reflected) to eqaul each other

translating an island to make it eqaul to another island means if we were to pick up an island and drop it on top of another island it should completely overlap that island. this is only possible if the islands have the exact same shape. if two islands have the same shape, they are not distinct

11000
11000
00011
00011
these two islands are both sqaures of the same size. they are not distinct
thus there is only one distinct shape for an island in this grid. we return 1

How do we find the shape of an island?

in number of islands, we explore islands by looking for adjacent pieces of land. To check for adjacent pieces of land we make a choice from piece of land we are currently at (move up, down, left, or right). To find all pieces of land that make up an island, we end up making a sequence of choices.

The key observation is for an island to be the same shape as another island it must be formed by the exact same sequence of choices.

if we construct a string that represents a sequence choices for each island we visit we now have found the shape of every island.

if we store the shape of each island in a set. we are left with distinct (unique) island shapes only. thus the length of the set will give us the count of distinct islands.

it is important to note any time we hit water or exceed the bounds of the grid that this is also considered a unique choice and a this must also be reflected in the shape string. the solution to this problem is almost identical to number of islands except we record the shape of each island as we go along and store it in a set.

dirs = {(-1,0, 'U'),(1,0, 'D'),(0,-1, 'L'),(0,1, 'R')}
       
        def bfs(row, col, grid):
            queue = collections.deque([(row, col)])
            s = "S"
            while queue:
                row, col = queue.popleft()   
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                    grid[row][col] = 0
                    for dir in dirs:
						# record shape 
                        s += dir[2]
                        neighbor = (row + dir[0], col + dir[1])
                        queue.append(neighbor)
                else:
				   # record hitting water or out of bounds 
                   s += 'X'
			# return shape 
            return s
        
        pattern = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    shape = bfs(i, j, grid)
										# add shape to set 
                    pattern.add(shape)
         # only unique shapes in set 
        return len(pattern)
    ```
----------------------------------------------------------------------

We use BFS to work through encountered islands, marking visited locations and tracking our path for and island pattern/signature. The 'e' we add after each direction iteration is to mark the end of the iteration for situations like this:

[1, 1, 0]
[0, 1, 1]
[0, 0, 0]
[1, 1, 1]
[0, 1, 0]

For the top case 'srederee':
We can only right from the start location. Then only down, then only right.
For the second island 'sredreee':
We can only right from the start location. Then we can go down or right.
If we didn't use the 'e' we'd have 'srdr' for both but they are different islands.

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0
		# Store our island patterns in a set to ensure uniqueness.
        island_patterns = set()
        rows = len(grid)
        cols = len(grid[0])
		# Directions to traverse our grid.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dstrs = ['d', 'u', 'r', 'l']
        
		# Iterate through our grid looking for islands.
        for ro in range(rows):
            for co in range(cols):
			    # If we find an island (given the iteration order we'll start at the top left location of each island).
                if grid[ro][co] == 1:
                    q = collections.deque([])
                    q.append((ro, co))
                    grid[ro][co] = '#'
                    stdir = 's'
                    while q:
                        row, col = q.popleft()
						# Iterate through our possible directions to move.
                        for i in range(len(directions)):
                            r, c = directions[i]
                            nr = row + r
                            nc = col + c
							# Validate that the new coordinates are valid (within our grid and contain a 1).
                            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
								# If valid we'll mark the location for being visited
                                grid[nr][nc] = '#'
								# Append new r and c to our q.
                                q.append((nr, nc))
								# Add the direction we took to our island signature or path history.
                                stdir += dstrs[i]
						# Track the end of the iteration, this is needed for uniquness in certain cases.
                        stdir += 'e'
					# When the q is empty add the pattern to our set.
                    island_patterns.add(stdir)

        return len(island_patterns)
----------------------------------------------------------------------------------

class Solution:
    """
    Iterate through grid
    - BFS when there is a 1
    - set its value to 0 then find nbrs and add to queue
    - for all other directions that are not 1, append some unique char for nonvalid
    - when popping a value keep track of the direction it came from
    - use set to keep unique ways bfs worked
    """
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        if not grid: return 0
        
        def bfs(r,c):
            
            offsets = [('r',0,1),('d',1,0),('l',0,-1),('u',-1,0)]
            tempDir = ''
            queue = deque([('s',r,c)])
            # print(r,c)
            while queue:
                cell = queue.popleft()
                fromDir = cell[0]
                tempDir += fromDir
                
                cellR = cell[1]
                cellC = cell[2]
                # print("currCell",cellR,cellC)
                for offset in offsets:
                    newR = cellR + offset[1]
                    newC = cellC + offset[2]
                    # print("newPre",newR,newC)
                    if newR >= 0 and newR < len(grid) and newC >= 0 and newC < len(grid[0]) and grid[newR][newC] == 1:
                        grid[newR][newC] = 0
                        queue.append((offset[0],newR,newC))
                        # print("new",newR,newC)
                    else:
                        tempDir += "n"
            
            return tempDir
                
                
        
        
        patternSet = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    pattern = bfs(row,col)
                    # print(pattern)
                    patternSet.add(pattern)
        
        return len(patternSet)
                    
        
        
      
    
      
      
