'''
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
'''



Use hit to record how many times a 0 grid has been reached and use distSum to record the sum of distance from all 1 grids to this 0 grid. A powerful pruning is that during the BFS we use count1 to count how many 1 grids we reached. If count1 < buildings then we know not all 1 grids are connected are we can return -1 immediately, which greatly improved speed (beat 100% submissions).

def shortestDistance(self, grid):
    if not grid or not grid[0]: return -1
    M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
    hit, distSum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]
    
    def BFS(start_x, start_y):
        visited = [[False] * N for k in range(M)]
        visited[start_x][start_y], count1, queue = True, 1, collections.deque([(start_x, start_y, 0)])
        while queue:
            x, y, dist = queue.popleft()
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                    visited[i][j] = True
                    if not grid[i][j]:
                        queue.append((i, j, dist + 1))
                        hit[i][j] += 1
                        distSum[i][j] += dist + 1
                    elif grid[i][j] == 1:
                        count1 += 1
        return count1 == buildings  
    
    for x in range(M):
        for y in range(N):
            if grid[x][y] == 1:
                if not BFS(x, y): return -1
    return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])
  
  
  ----------------------------------------------------------------------------------------------
  def __init__(self):
	self.empty, self.building = 0, 1

	self.direction = [(0,-1), (-1,0), (0,1), (1,0) ]

def shortestDistance(self, grid: List[List[int]]) -> int:
	buildings = []
	candidate_lands = {} # {position, distance}

	# 1. Find all buildings and candidate empty lands
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == self.building:
				buildings.append((r, c))

			elif grid[r][c] == self.empty:
				candidate_lands[(r, c)] = 0

	# 2. Compute min distance from each building to all candidate empty lands
	for building_position in buildings:
		self.compute_shortest_distances_bfs(candidate_lands, building_position)

	return min(candidate_lands.values()) if buildings and candidate_lands else -1

def compute_shortest_distances_bfs(self, candidate_lands: dict, position: (int, int)):
	distance = 0
	visited = set()

	# 1. BFS: this 2-lists bfs traversal makes it possible to avoid storing the distance for each node
	curr_level = [position]
	while curr_level:
		distance += 1

		next_level = []
		for position in curr_level:
			for direction in self.direction:
				adjacent_position = (position[0] + direction[0], position[1] + direction[1])

				if adjacent_position in candidate_lands and adjacent_position not in visited:
				    candidate_lands[adjacent_position] += distance
					
					visited.add(adjacent_position)
					next_level.append(adjacent_position)
		
		curr_level = next_level

	# 2. All empty lands that are not reachable from a building are excluded
	if len(visited) != len(candidate_lands):
		for position in set(candidate_lands.keys()).difference(visited):
			candidate_lands.pop(position)
      
---------------------------------------------------------------------
O(ke) - k is number of buildings and e is number of empty tiles - for each building we need to visit every empty tile
Space: O(mn*k) - need to store every point of the grid and for those which have empty slots of land we need to store an array of k buildings

Algorithm: do a BFS from each building. At each point you encounter an empty slot of land, mark how far away it is from your (building n). You will do this for each building such that at the end self.grid_emtpy will hold the distances at each point to the nearest one of the buildings. It will hold a list which contains how many buildings it can reach and how far they are in the shortest path. Therefore if a tile needs to reach all of the buildings we should check that the length of visitable buildings is equal to the total number of seen buildings. Once this is met we want the total minimum distance to all buildings, so take the sum of distances and record the minimum you find.

def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        bldgs = 0
        # This will hold the distances at each empty slot to each building
        self.grid_empty = [[None]*len(grid[0]) for _ in range(len(grid))]
        res = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # BFS for each building
                    self.visited = set((i, j))
                    bldgs += 1
                    self.bfs(i, j, grid)

        min_val = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # For each of the empty slots check that the building length matches all buildings
                # i.e from this piece of land you can reach all other buildings
                # If you can, take the sum of the distances and keep track of the smallest seen
                if grid[i][j] == 0:
                    if self.grid_empty[i][j] and len(self.grid_empty[i][j]) == bldgs:
                        min_val = min(min_val, sum(self.grid_empty[i][j]))
        
        # If min_val is never updated it means that no tile can reach all buildings, return -1
        return -1 if min_val == float('inf') else min_val
        
    def bfs(self, i, j, grid):
        q = collections.deque([(i, j, 0)])
        while q:
            nx, ny, move = q.popleft()
            for incr_x, incr_y in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                x = nx + incr_x
                y = ny + incr_y
                # Ensure the next tile is in range and is empty 
                if (x, y) not in self.visited and 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                    self.visited.add((x, y))
                    # Update the distance to the building you are running BFS on
                    # If this tile has been previously visited it means another building can also reach it, so append your distance to that existing list
                    if not self.grid_empty[x][y]:
                        self.grid_empty[x][y] = [move + 1]
                    else:
                        self.grid_empty[x][y].append(move + 1)
                    q.append((x, y, move + 1))
