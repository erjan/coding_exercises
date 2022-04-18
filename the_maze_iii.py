'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls onto the hole.

Given the m x n maze, the ball's position ball and the hole's position hole, where ball = [ballrow, ballcol] and hole = [holerow, holecol], return a string instructions of all the instructions that the ball should follow to drop in the hole with the shortest distance possible. If there are multiple valid instructions, return the lexicographically minimum one. If the ball can't drop in the hole, return "impossible".

If there is a way for the ball to drop in the hole, the answer instructions should contain the characters 'u' (i.e., up), 'd' (i.e., down), 'l' (i.e., left), and 'r' (i.e., right).

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).
'''


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        from heapq import heappush, heappop
        star_row, start_col = ball
        heap = [(0, star_row, start_col, '')] # steps, row, col, string (direction)
        visited_nodes = set()

        while heap:
            current_distance, current_row, current_col, current_string = heappop(heap)
            
            if (current_row, current_col) not in visited_nodes:
                
                visited_nodes.add((current_row, current_col)) 

                if [current_row, current_col] == hole:
                    return current_string
                
                for row_diff, col_diff, direction in [(1, 0, 'd'), (-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l')]:

                    row = current_row
                    col = current_col
                    count = 0

                    while 0 <= row + row_diff <= len(maze) - 1 and 0 <= col + col_diff <= len(maze[0]) - 1 and maze[row + row_diff][col + col_diff] == 0:
                        row += row_diff
                        col += col_diff
                        count += 1

                        if [row, col] == hole:
                            break

                    if (row, col) not in visited_nodes:
                        heappush(heap, (current_distance + count, row, col, current_string + direction))  

        return 'impossible'
      
---------------------------------------------------------------------
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        ## RC ##
        ## APPROACH : BFS ##
        ## EDGE CASE : Like maze I, we just cannot return by checking (i,j) in visited, we have to also check the previous distance with which (i,j) is visited and what is the current distance. Not only that we have to also check if both the distances are equal, we have to check the previous path and curr path values.
        directions = [(1, 0, 'd'),  (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
        queue = collections.deque([(ball[0], ball[1], "", 0)])
        M, N, visited = len(maze), len(maze[0]), {}
        result = collections.defaultdict(list)
        res_length = float('inf')
        while(queue):
            i, j, path, distance = queue.popleft()
            visited[(i,j)] = (path, distance)
            for x, y, d in directions:
                row, col, dist = i, j, distance     # init row, col to initial position before moving in each and every direction
                while 0 <= row + x < M and 0 <= col + y < N and maze[row + x][col + y] == 0:
                    row, col, dist = row + x, col + y, dist + 1
                    if [row, col] == hole:          # check if the ball falls while rolling
                        res_length = min(res_length, dist)
                        result[dist].append(path + d)
                if(row, col) not in visited: 
                    queue.append((row, col, path + d, dist))
                elif visited[(row, col)][1] >= dist and visited[(row, col)][0] > path + d:  # edge case
                        visited[(row, col)] = (path + d, dist)      # make sure to change in visited
                        queue.append((row, col, path + d, dist))    # also need to continue this path even though if its in visited as the current path is better in distance or path.
        return "impossible" if( not result ) else sorted(result[res_length])[0]
    
		## APPROACH : DFS ##
        ## BAD RUNTIME DUE TO DFS, BFS IS BETTER HERE, AS WE HAVE TO FIND THE SHORTEST PATH ##
        
        # the ball can move these possible directions
        directions = [("l", 0,-1),("r", 0, 1),("u", -1, 0),("d",1,0)]
        
        # when the ball curr direction is given, to keep the ball rolling in that direction, we use these values.
        rolling_directions = {
            "l" : (0,-1),
            "r" : (0, 1),
            "u": (-1, 0),
            "d":(1,0)
        }
        def dfs( i, j, path, distance, dir, visited ):            
            
            if( self.result and distance > self.result[1]):
                return False
                        
            if(dir): 
                dx, dy = rolling_directions[dir]
                
                while( 0 <= i + dx < len(maze) and 0 <= j +dy < len(maze[0]) and not (maze[i+dx][j+dy] == 1)):
                    i = i +dx
                    j = j +dy
                    
                    distance += 1
                    
                    if( i == hole[0] and j == hole[1] ):
                        if(self.result and self.result[1] >= distance or (not self.result) ):
                            if(self.result and self.result[1] == distance):
                                self.result =  (path[:], distance) if("".join(self.result[0]) > "".join(path[:]) ) else (self.result[0], distance)
                            else:
                                self.result = (path[:], distance)
                    
                    if( (i,j) in visited) : 
                        return False
                    
            if( i == hole[0] and j == hole[1] ):
                if(self.result and self.result[1] >= distance or (not self.result) ):
                    if(self.result and self.result[1] == distance):
                        self.result =  (path[:], distance) if("".join(self.result[0]) > "".join(path[:]) ) else (self.result[0], distance)
                    else:
                        self.result = (path[:], distance)
                        
            for new_dir, x, y in directions:
                if( (i+x, j+y) not in visited and 0 <= i + x < len(maze) and 0 <= j + y < len(maze[0]) and not maze[i+x][j+y] == 1 ):
                    
                    visited.add((i,j))
                    
                    dfs( i, j, path+[new_dir], distance, new_dir , visited )
                    
                    visited.remove((i,j))
        
        visited = set()
        path = []
        self.result = []
        dfs(ball[0], ball[1], path, 0, None, visited)
        return "".join(self.result[0]) if(self.result) else "impossible"
----------------------------------------------------------------------------------
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        self.m = len(maze)
        self.n = len(maze[0])
        self.maze = maze
        self.distance = [[(2**31, "z")] * self.n for _ in range(self.m)]
        self.distance[ball[0]][ball[1]] = (0, "")
        self.hole = hole
        self.build_path(ball)
        return self.distance[hole[0]][hole[1]][1] if self.distance[hole[0]][hole[1]][1] != "z" else "impossible" 
        
    def build_path(self, start: List[int]):
        heap = []
        directions = [(1, 0, "d"), (-1, 0, "u"), (0, 1, "r"), (0, -1, "l")]
        heapq.heappush(heap, (0, "", start[0], start[1]))
        
        while heap:
            cost, instr, point_i, point_j = heapq.heappop(heap)
            for d in directions:
                i = point_i
                j = point_j
                while i >= 0 and i < self.m and j >= 0 and j < self.n and self.maze[i][j] == 0 and not (i == self.hole[0] and j == self.hole[1]):
                    i += d[0]
                    j += d[1]
                
                if not (i == self.hole[0] and j == self.hole[1]):
                    i -= d[0]
                    j -= d[1]

                dist = abs(point_i - i) + abs(point_j - j) + cost
                instruction = instr + d[2]
                
                if dist < self.distance[i][j][0] or dist == self.distance[i][j][0] and instruction < self.distance[i][j][1]:
                    self.distance[i][j] = (dist, instruction)
                    heapq.heappush(heap, (dist, instruction, i, j))
-------------------------------------------------------------------------
   if not maze or not maze[0]:
            return "impossible"
        
        ball = tuple(ball) # make it hashable
        hole = tuple(hole) # make it hashable
        
        rows = len(maze)
        columns = len(maze[0])
        
        directions = [(-1, 0, "u"), (1, 0, "d"), (0, 1, "r"), (0, -1, "l")]
        
        priority_queue = [((0, ""), ball)]
        visited = set()
        
        def get_neighbors(node):
            for r_diff, c_diff, direction in directions:
                row, column = node
                distance = 0
                while row + r_diff >= 0 and column + c_diff >= 0 and row + r_diff < rows and column + c_diff < columns:
                    if maze[row + r_diff][column + c_diff]:
                        break
                        
                    row += r_diff
                    column += c_diff
                    distance += 1
                    
                    if (row, column) == hole:
                        break
                        
                if (row, column) not in visited:
                    yield row, column, distance, direction
        
        while priority_queue:           
            (current_distance, path), node = heapq.heappop(priority_queue)            
            if node in visited:
                continue
                
            if node == hole:
                return path
            
            visited.add(node)

            for new_row, new_column, distance, direction in get_neighbors(node):
                heapq.heappush(priority_queue, ((current_distance + distance, path + direction), (new_row, new_column)))
        
        return "impossible"
                    
      
      
