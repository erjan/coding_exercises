'''
There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are (x, y).

We start at the source = [sx, sy] square and want to reach the target = [tx, ty] square. There is also an array of blocked squares, where each blocked[i] = [xi, yi] represents a blocked square with coordinates (xi, yi).

Each move, we can walk one square north, east, south, or west if the square is not in the array of blocked squares. We are also not allowed to walk outside of the grid.

Return true if and only if it is possible to reach the target square from the source square through a sequence of valid moves.
'''

from collections import deque
class Solution:
    def isSafe(self, i, j):
        return 0 <= i < 10**6 and 0 <= j < 10**6
    
    def bfs(self, source, target, blocked):
        a = source[0]
        b = source[1]
        
        
        if len(blocked) == 0:
            return True
        
        queue, visited = deque([(a, b)]), set([(a, b)])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while queue:
            coordinates = queue.popleft()
            x = coordinates[0]
            y = coordinates[1]
            
            if [x, y] == target:
                return True
            
            if x in (a + 210,a - 210) or y in (b + 210, b - 210):
                return True
            
            for direction in directions:
                xNew = x + direction[0]
                yNew = y + direction[1]
                
                newPair = (xNew, yNew)
                if self.isSafe(xNew, yNew) and (newPair not in visited) and (list(newPair) not in blocked):
                    queue.append((xNew, yNew))
                    visited.add((xNew, yNew))
        
        return False
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        return self.bfs(source, target, blocked) and self.bfs(target, source, blocked)
      
--------------------------------------------------------------------------------------------------------------------
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(map(tuple, blocked))
        
        def fn(x, y, tx, ty): 
            """Return True if (x, y) is not looped from (tx, ty)."""
            seen = {(x, y)}
            queue = [(x, y)]
            level = 0 
            while queue: 
                level += 1
                if level > 200: return True 
                newq = []
                for x, y in queue: 
                    if (x, y) == (tx, ty): return True 
                    for xx, yy in (x-1, y), (x, y-1), (x, y+1), (x+1, y): 
                        if 0 <= xx < 1e6 and 0 <= yy < 1e6 and (xx, yy) not in blocked and (xx, yy) not in seen: 
                            seen.add((xx, yy))
                            newq.append((xx, yy))
                queue = newq
            return False 
        
        return fn(*source, *target) and fn(*target, *source)
