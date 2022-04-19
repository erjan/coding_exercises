'''
This is an interactive problem.

There is a robot in a hidden grid, and you are trying to get it from its starting cell to the target cell in this grid. The grid is of size m x n, and each cell in the grid is either empty or blocked. It is guaranteed that the starting cell and the target cell are different, and neither of them is blocked.

Each cell has a cost that you need to pay each time you move to the cell. The starting cell's cost is not applied before the robot moves.

You want to find the minimum total cost to move the robot to the target cell. However, you do not know the grid's dimensions, the starting cell, nor the target cell. You are only allowed to ask queries to the GridMaster object.

The GridMaster class has the following functions:

boolean canMove(char direction) Returns true if the robot can move in that direction. Otherwise, it returns false.
int move(char direction) Moves the robot in that direction and returns the cost of moving to that cell. If this move would move the robot to a blocked cell or off the grid, the move will be ignored, the robot will remain in the same position, and the function will return -1.
boolean isTarget() Returns true if the robot is currently on the target cell. Otherwise, it returns false.
Note that direction in the above functions should be a character from {'U','D','L','R'}, representing the directions up, down, left, and right, respectively.

Return the minimum total cost to get the robot from its initial starting cell to the target cell. If there is no valid path between the cells, return -1.
'''


Explanation
The code is long but the idea is simple:
We don't know what the hidden grid looks like, so we want to find it out
First, "draw the grid" using DFS (we are not really drawing it, see more details below)
Then find the lowest cost to target using Dijkstra
Based on hint section, we can first do a DFS to:
Explore the hidden grid and save the cost for each location
Assuming starting from index (0, 0) and trying to find & store all accessible locations
Indices for all other locations are relative offsets to the starting origin (0, 0)
See if we can get to target
Then, we can do a Dijkstra search to find the lowest cost to target
Implementation
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        opposite = {'D': 'U', 'U': 'D', 'L': 'R', 'R': 'L'}       # opposite direction to move back and force
        cost_dict = collections.defaultdict(lambda: sys.maxsize)  # save cost for each location (x, y)
        target = None                                             # this will be `target` index
        
        def dfs(cur, x, y):
            nonlocal target
            if cur.isTarget():                                    # if `target` found, save its index and return True
                target = x, y
                return True
            ans = False
            for di, (i, j) in zip(['D', 'U', 'L', 'R'], [(-1, 0), (1, 0), (0, -1), (0, 1)]): # explore 4 directions
                _x, _y = x+i, y+j
                if (_x, _y) in cost_dict: continue                # check if (_x, _y) is visited
                cost_dict[(_x, _y)] = sys.maxsize                 # mark (_x, _y) as visited
                if cur.canMove(di):
                    cost = cur.move(di)                           # move to direction `di`
                    cost_dict[(_x, _y)] = cost                    # save cost of (_x, _y)
                    ans |= dfs(cur, _x, _y)                       # `dfs`
                    cur.move(opposite[di])                        # move back
            return ans                    
        
        if not dfs(master, 0, 0): return -1                       # if can't reach to `target`, return -1
        
        heap = [(0, 0, 0)]                                        # starts from (0, 0) again. Parameters are (cost, x, y)
        while heap:                                               # Dijkstra starts here
            cost, x, y = heapq.heappop(heap)
            if (x, y) == target: return cost
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _x, _y = x+i, y+j
                if (_x, _y) not in cost_dict: continue            # if location not in `cost_dict`, meaning it's not accessible
                heapq.heappush(heap, (cost+cost_dict[(_x, _y)], _x, _y))
                cost_dict[(_x, _y)] = sys.maxsize                 # mark as visited
        return -1
      
      
--------------------------------------------------------------------


from heapq import heappop, heappush
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        def dfs(row = 0, col = 0):
            nonlocal final_destination
            for direction, opp_direction, new_row, new_col in ('U', 'D', row - 1, col), ('D', 'U', row + 1, col), ('L', 'R', row, col - 1), ('R', 'L', row, col + 1):
                if master.canMove(direction) and (new_row, new_col) not in graph:
                    graph[(new_row, new_col)] = master.move(direction)
                    if master.isTarget():
                        final_destination = [new_row, new_col]
                    dfs(new_row, new_col)
                    master.move(opp_direction) # backtrack and move back to original position
                    
        graph = {(0, 0): 0} # {(row, col): cost}
        final_destination = None
        dfs() #Dfs to populate 'graph'
        
        if final_destination is None:
            return -1
        
        # Dijkstra using min heap
        heap = [(0, 0, 0)] #cost, row, col
        distance_cost = dict()
        while heap:
            cost, row, col = heappop(heap)
            if (row, col) not in distance_cost:
                distance_cost[(row, col)] = cost
                if [row, col] == final_destination:
                    return cost
                for new_row, new_col in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                    if (new_row, new_col) in graph and (new_row, new_col) not in distance_cost:
                        heappush(heap, (cost + graph[(new_row, new_col)], new_row, new_col))
        return -1
-----------------------------------------------------------------

import collections
import heapq
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        back = {'U': 'D', 'D': 'U', 'L':'R', 'R':'L'}
        inf = float('inf')
        visited = set()
        self.distance = dict()
        coor = {'U': (-1, 0), 'D': (1, 0), 'L':(0, -1), 'R': (0, 1)}
        self.target_cor = ()
        # Use DFS to explore the map and find the location of the target
        def dfs(master, cur):
            visited.add(cur)
            canMoves = []
            if master.isTarget():
                self.target_cor = cur
            for d in ['U', 'D', 'L', 'R']:
                new_x = cur[0] + coor[d][0]
                new_y = cur[1] + coor[d][1]
                if master.canMove(d) and (new_x, new_y) not in visited:
                    c = master.move(d)
                    self.distance[(new_x, new_y)] = c
                    dfs(master, (new_x, new_y))
                    master.move(back[d])
        
        dfs(master, (0, 0))
        if not self.target_cor:
            return -1

        dist = collections.defaultdict(lambda: float('inf'))
        start = (0, 0)
        dist[start] = 0
        
        # Use dijkstra to find the shortest path from the start to the end.
        def dijkstra():
            minHeap = [(0, 0, 0)]
            while minHeap:
                u = heapq.heappop(minHeap)
                w, x, y = u
                neir_cors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for cor in neir_cors:
                    new_x = x + cor[0]
                    new_y = y + cor[1]
                    if (new_x, new_y) in self.distance and w + self.distance[(new_x, new_y)] < dist[(new_x, new_y)]:
                        dist[(new_x, new_y)] = w + self.distance[(new_x, new_y)]
                        heapq.heappush(minHeap, [w + self.distance[(new_x, new_y)], new_x, new_y])
        dijkstra()
        
        return dist[self.target_cor]

      
      
