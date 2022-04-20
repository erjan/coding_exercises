'''
This is an interactive problem.

There is a robot in a hidden grid, and you are trying to get it from its starting cell to the target cell in this grid. The grid is of size m x n, and each cell in the grid is either empty or blocked. It is guaranteed that the starting cell and the target cell are different, and neither of them is blocked.

You want to find the minimum distance to the target cell. However, you do not know the grid's dimensions, the starting cell, nor the target cell. You are only allowed to ask queries to the GridMaster object.

Thr GridMaster class has the following functions:

boolean canMove(char direction) Returns true if the robot can move in that direction. Otherwise, it returns false.
void move(char direction) Moves the robot in that direction. If this move would move the robot to a blocked cell or off the grid, the move will be ignored, and the robot will remain in the same position.
boolean isTarget() Returns true if the robot is currently on the target cell. Otherwise, it returns false.
Note that direction in the above functions should be a character from {'U','D','L','R'}, representing the directions up, down, left, and right, respectively.

Return the minimum distance between the robot's initial starting cell and the target cell. If there is no valid path between the cells, return -1.

Custom testing:

The test input is read as a 2D matrix grid of size m x n where:

grid[i][j] == -1 indicates that the robot is in cell (i, j) (the starting cell).
grid[i][j] == 0 indicates that the cell (i, j) is blocked.
grid[i][j] == 1 indicates that the cell (i, j) is empty.
grid[i][j] == 2 indicates that the cell (i, j) is the target cell.
There is exactly one -1 and 2 in grid. Remember that you will not have this information in your code.
'''


Expalantion
Similar question: 1810. Minimum Path Cost in a Hidden Grid
Based on hint section, do a DFS to explore the grid, then use BFS to find the shortest path
DFS: Assuming that we are starting from (0, 0), explore the grid, save the relative offset of other reachable positions (including target)
BFS: Find the shortest path by visiting reachable locations stored by DFS
Implementation
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        opposite = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        reachable = set([(0, 0)])
        target = None
        def dfs(cur, x, y):                                       # dfs to explore the grid
            nonlocal target
            if cur.isTarget():
                target = x, y                                     # save `target` position
                return True
            ans = False
            for di, (i, j) in zip(['D', 'U', 'L', 'R'], [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                _x, _y = x+i, y+j
                if (_x, _y) not in reachable and cur.canMove(di): # if not reachable and can move
                    cur.move(di)
                    reachable.add((_x, _y))                       # save position to `reachable`
                    ans |= dfs(cur, _x, _y)                       # dfs on next position
                    cur.move(opposite[di])                        # move back to position before dfs
            return ans                    
        
        if not dfs(master, 0, 0): return -1
        
        dq = collections.deque([(0, 0, 0)])                       # starting BFS here
        while dq:
            step, x, y = dq.popleft()
            if (x, y) == target: return step
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _x, _y = x+i, y+j
                if (_x, _y) not in reachable: continue            # only continue BFS on reachable neighbors
                dq.append((step+1, _x, _y))                       # BFS at neighbor positions
                reachable.remove((_x, _y))                        # remove from `reachable` once used to avoid repeats
        return -1
      
-----------------------------------------

class Solution(object):
    DIRECTIONS = (('U', -1, 0, 'D'), ('D', 1, 0, 'U'), ('L', 0, -1, 'R'), ('R', 0, 1, 'L'))
    
    def findShortestPath(self, master: 'GridMaster') -> int:
        start = 0, 0
        target, visited = dfs(start, master)
        if target is None:
            return -1
        return dijkstras(start, visited, target)

def dfs(start, master):
    seen = {start}
    target = None
    stack = [(start, None)]
    visited = set()
    while stack:
        node, direction = stack.pop()
        if direction is not None:
            master.move(direction)
        if node in visited:
            continue
        visited.add(node)
        if target is None and master.isTarget():
            target = node
        r, c = node
        for direction, rd, cd, inverted in Solution.DIRECTIONS:
            next_node = (r + rd, c + cd)
            if next_node not in seen:
                seen.add(next_node)
                if master.canMove(direction):
                    stack.append((node, inverted))
                    stack.append((next_node, direction))
    return target, visited

def dijkstras(start, visited, target):
    distances = dict.fromkeys(visited, math.inf)
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        distance, (r, c) = heappop(pq)
        if (r, c) == target:
            return distance
        for next_node in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if next_node not in distances:
                continue
            next_distance = distance + 1
            if next_distance < distances[next_node]:
                distances[next_node] = next_distance
                heappush(pq, (next_distance, next_node))
    return -1
-----------------------------------------------------------------------------  
  
