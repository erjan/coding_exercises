'''
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
'''


class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        h = len(rooms)
        w = len(rooms[0])
        
        q = []
        for i in range(h):
            for j in range(w):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        for row, col in q:
            dist = rooms[row][col] + 1
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dy
                c = col + dx
                if 0 <= r < h and 0 <= c < w and rooms[r][c] == 2147483647:
                    rooms[r][c] = dist
                    q.append((r,c))
                    
-----------------------------------------------------------------
def wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    if not rooms:
        return
    
    m, n = len(rooms), len(rooms[0])
    queue = collections.deque([])
    
    dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
    
    for i in xrange(m):
        for j in xrange(n):
            if rooms[i][j] == 0:
                queue.append((i, j))
    
    dis = 0
    while queue:
        length = len(queue)
        dis += 1
        for i in xrange(length):
            cur = queue.popleft()
            for dir in dirs:
                nextPos = (cur[0]+dir[0], cur[1]+dir[1])
                if nextPos[0] >= 0 and nextPos[0] < m and nextPos[1] >= 0 and nextPos[1] < n and rooms[nextPos[0]][nextPos[1]] == 2147483647:
                    rooms[nextPos[0]][nextPos[1]] = dis
                    queue.append(nextPos)
                    
-------------------------------------------------------------------------------------------------
My solutions are below.

Outcomes from solving this problem:

Even if this problem is a shortest-path problem in a weighted graph, Dijksta's algorithm is not efficient
In fact, in this problem, all edges have the same weight
Therefore, for shortest-path problems:
If graph weights are equal: Bellman-Ford, Dijkstra's algorithms and BFS traversal are all solutions but the BFS is the most efficient
If graph weights are different and all are positive: Bellman-Ford and Dijkstra's algorithms are solutions but the Dijkstra's is the most efficient
If graph weights are different and could be positive/negative: Bellman-Ford algorithms is the only solution betweem the 3 algorithm mentioned here.
Common for both solution:

def __init__(self):
		self.gate = 0
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)] # left, up, right, down
Solution 1: BFS:

Time Complexity: O(nm)
Space Complexity: O(nm)
from collections import deque
    
def wallsAndGates(self, rooms: List[List[int]]) -> None:
	if not rooms:
		return

	rows_count = len(rooms)
	cols_count = len(rooms[0])

	#// 1. Find all gates
	q = deque()
	for r in range(rows_count):
		for c in range(cols_count):
			if rooms[r][c] == self.gate:
				q.append((r, c))

	#// 2. Find shorstest distance to gate: BFS:
	while q:
		r, c = q.popleft()

		candidate_distance = rooms[r][c] + 1
		
		for d_r, d_c in self.directions:
			adj_r, adj_c = r + d_r, c + d_c
			if adj_r in (-1, rows_count) or adj_c in (-1, cols_count):
				continue
                    
			if candidate_distance < rooms[adj_r][adj_c]: #// no check if cell is a wall since the candidate_distance will be always > -1
				rooms[adj_r][adj_c] = candidate_distance
				q.append((adj_r, adj_c))

Solution 2: Dijkstra's:

Time Complexity: O(nm*lognm)
Space Complexity: O(nm)
import heapq

def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        
        rows_count = len(rooms)
        cols_count = len(rooms[0])
        
        #// 1. Find all gates
        heap = []
        for r in range(rows_count):
            for c in range(cols_count):
                if rooms[r][c] == self.gate:
                    heap.append((0, r, c))
                
        #// 2. Find shorstest distance to gate: Dijkstra
        while heap:
            distance, r, c = heapq.heappop(heap)
            
            candidate_distance = distance + 1
            for d_r, d_c in self.directions:
                adj_r, adj_c = r + d_r, c + d_c
                if adj_r in (-1, rows_count) or adj_c in (-1, cols_count):
                    continue
                
                if candidate_distance < rooms[adj_r][adj_c]:
                    rooms[adj_r][adj_c] = candidate_distance
                    heapq.heappush(heap, (candidate_distance, adj_r, adj_c))
-----------------------------------------------------------------------------------
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ## Find all starting points
        n, m = len(rooms), len(rooms[0])
        queue = []
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append((i,j, 0))
        ## BFS
        while queue:
            x, y, d = queue.pop(0)
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x_new, y_new = x+dx, y+dy
                if 0<=x_new<n and 0<=y_new<m and d + 1 < rooms[x_new][y_new]:
                    rooms[x_new][y_new] = d+1
                    queue.append((x_new,y_new,d+1))
                    
-------------------------------------------------------------
class Solution:
    def wallsAndGates(self, rooms):
       
        if not rooms:
            return 
        
        r, c = len(rooms), len(rooms[0])
        queue = collections.deque([])
        
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            
            for nx, ny in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                nx += x
                ny += y
            
                if 0 <= nx < r and 0 <= ny < c and rooms[nx][ny] == 2147483647:                
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append((nx, ny))
                    
                    -------------------------------------------------------
                    
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque([])
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        while queue:
            i, j = queue.popleft()
            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= r < len(rooms) and 0 <= c < len(rooms[0]) and rooms[r][c] == 2147483647:
                    rooms[r][c] = rooms[i][j] + 1
                    queue.append([r, c])                    
