'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).
'''

        min_heap = [(0, start)]
        visited = set()
        while min_heap:
            w, [r, c] = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if [r, c] == destination:
                return w
            for x, y in (-1, 0), (+1, 0), (0, -1), (0, +1):
                dr, dc = r, c
                k = 0
                while 0 <= dr + x < len(maze) \
                and 0 <= dc + y < len(maze[0]) \
                and maze[dr + x][dc + y] == 0:
                    dr, dc = dr + x, dc + y
                    k += 1
                if (dr, dc) not in visited:
                    heapq.heappush(min_heap, (w + k, [dr, dc]))
        return -1
      
---------------------------------------------

BFS + dijkstra's, use a min-heap instead of a queue.

every time, pop the shortest position from the heap
every time, what we want: make the value of distance[node] become samller
if the distance to current position + the weight of an edge cannot make that value smaller, we continue , skip this edge
import heapq

class Solution:

    def shortestDistance(self, maze, start, destination):
        if not maze or not maze[0]:
            return -1

        DIRECTION = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        start = (start[0], start[1])
        destination = (destination[0], destination[1])
        distance = {start:0}
        heap = []
        heapq.heappush(heap, (0, start))
        
        while heap:
            last_step, curr_position = heapq.heappop(heap)
            
            if curr_position == destination:
                return distance[curr_position]
            
            for dx, dy in DIRECTION:
                x, y = curr_position
                step = 0
                while True:
                    new_x = x + dx
                    new_y = y + dy
                    if self.isValid(maze, new_x, new_y):
                        step += 1
                        x, y = new_x, new_y
                    else:
                        break
                next_pos = (x, y)

          
                if next_pos in distance and distance[curr_position] + step >= distance[next_pos]:
                    continue
                
                heapq.heappush(heap, (last_step + step, next_pos))
                
                distance[next_pos] = distance[curr_position] + step
        
        return -1
    
    def isValid(self, maze, new_x, new_y):
        n = len(maze)
        m = len(maze[0])
        if new_x < 0 or new_x >= n or new_y <0 or new_y >= m:
            return False
        
        if maze[new_x][new_y] == 1:
            return False

        return True
-------------------------------------------------------------------------------



class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        def get_pos(r, c):
            pos = []
            for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                nr, nc, d = r, c, 0
                while (0 <= nr+x < M) and (0 <= nc+y < N) and maze[nr+x][nc+y] == 0:
                    nr += x
                    nc += y
                    d += 1
                pos.append((nr, nc, d))
            return pos
        
        M, N = len(maze), len(maze[0])
        queue, visited = deque([tuple(start + [0])]), {tuple(start): 0}
        min_dist = float(inf)
        while queue:
            r, c, dist = queue.popleft()
            if [r, c] == destination:
                min_dist = min(dist, min_dist)
                continue
            for nr, nc, d in get_pos(r, c):
                if ((nr, nc) not in visited) or (visited[(nr, nc)] > dist+d):
                    queue.append((nr, nc, dist+d))
                    visited[(nr, nc)] = dist+d
        return min_dist if min_dist < float(inf) else -1
---------------------------------------------------------------------------------

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        pq = [(0, start[0], start[1])] # min-heap 
        dist = defaultdict(lambda: inf, {tuple(start): 0})
        while pq: 
            x, i, j = heappop(pq)
            if [i, j] == destination: return x
            for di, dj in (-1, 0), (0, -1), (0, 1), (1, 0): 
                ii, jj = i, j
                while 0 <= ii+di < m and 0 <= jj+dj < n and maze[ii+di][jj+dj] == 0: 
                    ii += di
                    jj += dj 
                xx = x + abs(ii - i) + abs(jj - j)
                if xx < dist[ii, jj]: 
                    heappush(pq, (xx, ii, jj))
                    dist[ii, jj] = xx
        return -1
      
-----------------------------------------------------------------------------------

The question can be solved by normal DFS, if without the condition that the ball will keep rolling until it hits the war. For the cell the ball passes through, we don't consider 4 direction movement like a normal DFS question does. This adds the complexity for the problem.
If we look deeper, we have two issues to solve: find all the possible cells the ball can stop and find min distance from start cell to destination cell.
If we further check issue 1 and think in a way of graph, those cells are actually the vertices of the graph. And if a ball starts from cell A and stops at cell B, A and B are neighbours with weights to be the # of cells it goes through.
Combined with issue 2, this is a standard single source shortest distance in a graph with positive weights problem. We can exactly apply a Dijkstra's algorithm to solve it. Below is my code:

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n and maze[r][c] == 0
        
        
        def createGraph(r,c):
            if (r,c) in visit:
                return
            visit.add((r,c))
            for d in [(0,1), (1,0), (-1,0), (0,-1)]:
                # find neighbor point to be added to the graph
                x, y = r+d[0], c+d[1]
                # w is the weight of the edge
                w = 0
                while isValid(x, y):
                    x += d[0]
                    y += d[1]
                    w += 1
                x -= d[0]
                y -= d[1]
                if w:
                    graph[(r,c)].append((x,y,w))
                if (x, y) not in visit:
                    createGraph(x, y)
                
        
        m, n = len(maze), len(maze[0])
        graph = defaultdict(list)
        visit = set()
        createGraph(start[0], start[1])
        # destination not achieveable
        if tuple(destination) not in graph:
            return -1
        distances = dict()
        MAX_INT = m*n
        for key in graph:
            distances[key] = MAX_INT
        distances[tuple(start)] = 0
        heap = [(0, start[0], start[1])]
        while heap:
            d, r, c = heapq.heappop(heap)
            if r == destination[0] and c == destination[1]:
                return d
            for x,y,w in graph[(r,c)]:
                if d+w < distances[(x,y)]:
                    distances[(x,y)] = d+w
                    heapq.heappush(heap, (d+w,x,y))
        return -1
--------------------------------------------------------------------------------------      
      
