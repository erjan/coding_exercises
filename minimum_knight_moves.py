'''
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 
 '''

All solutions below are based on symmetry, meaning (x, y), (-x, y), (x, -y), (-x, -y) will have the same results.

Approach #1 - One-direction BFS with pruning
Use pruning to remove unnecessary location
-1 <= a+dx <= x+2 and -1 <= b+dy <= y+2:
Time Complexity: O(|x|*|y|)
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = collections.deque([(0, 0, 0)])
        x, y, visited = abs(x), abs(y), set([(0,0)])
        while q:
            a, b, step = q.popleft()
            if (a, b) == (x,y): return step
            for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1)]:  # no need to have (-1, -2) and (-2, -1) since it only goes 1 direction
                if (a+dx, b+dy) not in visited and -1 <= a+dx <= x+2 and -1 <= b+dy <= y+2:
                    visited.add((a+dx, b+dy))
                    q.append((a+dx, b+dy, step+1))
        return -1 
Approach #2 - Two-direction BFS with pruning
Start BFS from both origin & target coordinates
Use pruning to remove unnecessary location
-1 <= a+dx <= x+2 and -1 <= b+dy <= y+2:
Time Complexity: O(|x|*|y|), ideally half time costs of approach #1
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        qo = collections.deque([(0, 0, 0)])
        qt = collections.deque([(x, y, 0)])
        do, dt = {(0,0): 0}, {(x,y): 0}
        while True:
            ox, oy, ostep = qo.popleft()
            if (ox, oy) in dt: return ostep + dt[(ox, oy)]
            tx, ty, tstep = qt.popleft()
            if (tx, ty) in do: return tstep + do[(tx, ty)]
            for dx, dy in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]:
                if (ox+dx, oy+dy) not in do and -1 <= ox+dx <= x+2 and -1 <= oy+dy <= y+2:
                    qo.append((ox+dx, oy+dy, ostep+1))
                    do[(ox+dx,oy+dy)] = ostep+1
                if (tx+dx, ty+dy) not in dt and -1 <= tx+dx <= x+2 and -1 <= ty+dy <= y+2:
                    qt.append((tx+dx, ty+dy, tstep+1))
                    dt[(tx+dx,ty+dy)] = tstep+1
        return -1
Approach #3 - DFS + Math + Memoization
Try to move from target to origin as fast as possible
When reaching to certain point, handle the special situation and return the result
Time Complexity: O(|x|*|y|)
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None) 
        def dp(x,y):
            if x + y == 0: return 0
            elif x + y == 2: return 2
            return min(dp(abs(x-1),abs(y-2)), dp(abs(x-2),abs(y-1))) + 1
        return dp(abs(x),abs(y))
Approach #4 - Math
Pretty much the same idea as previous
With Math induction, you will find a pattern with division, which can replace previous DFS process
Time Complexity: O(1)
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if (x < y): x, y = y, x
        if (x == 1 and y == 0): return 3        
        if (x == 2 and y == 2): return 4        
        delta = x - y
        if (y > delta): return delta - 2 * int((delta - y) // 3);
        else: return delta - 2 * int((delta - y) // 4);
        
-------------------------------------------------------------------------------------

I don't believe we need to use any formulas in an actual interview. I had given the following solution for a mock and an actual interview and got through to next round.

class Solution:
    def minKnightMoves(self, s: int, e: int) -> int:
        q = collections.deque()
        q.append([0,0,0])
        visited = set()
        visited.add((0,0))
        while q:
            x,y,steps = q.popleft()
            if x==s and y==e:
                return steps
            dirs = [(x-1,y-2),(x-2,y-1),(x-2,y+1),(x-1,y+2),(x+1,y-2),(x+2,y-1),(x+1,y+2),(x+2,y+1)]
            for i,j in dirs:
                if (i,j) not in visited:
                    q.append([i,j,steps+1])
                    visited.add((i,j))
        return -1
---------------------------------------------------------------------------------------

Naive BFS is trival, we need some optimizations.

Since the board is symemtric, quadrant has no effect to the final answer(steps to the target). We can put the target to the first quadrant for convenice. x, y = abs(x), abs(y)
Notice that for some points on the edge or close to the edge, like (1 ,1), we need some help for other quadrants to reach the point with minimum steps. So we relax the bound to (-2, inf) for both x, y. -2 is the max range a knight can reach within 1 step.
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0:
            return 0
        
        dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        q = collections.deque([(0, 0)])
        
        step = 0
        visited = set()
        x, y = abs(x), abs(y)
        
        while q:
            step += 1
            
            qSize = len(q)
            for _ in range(qSize):
                nextX, nextY = q.popleft()
                
                for dx, dy in dirs:
                    newX, newY = nextX + dx, nextY + dy
                    if (newX, newY) == (x, y):
                        return step
                    
                    if newX < -2 or newY < -2 or (newX, newY) in visited:
                        continue
                       
                    visited.add((newX, newY))
                    q.append((newX, newY))
                    
        return step
----------------------------------------------------------------------------------------

def minKnightMoves(self, x: int, y: int) -> int:
    # let's do bfs
    # Because of the symmetry, we can just look into the first
    # quadrant and also push only positive coordinates to the queue
    # also look for x >= -5 and y >= -5 case.
	# x >= 0 and y >= 0 is sufficient to pass all the leetcode test case,
	# but code fails when x = 1 and y = 1 ( [0,0]->[-1,2]->[1,1] )
    if x == 0 and y == 0:
        return 0
    return self.bfs(abs(x), abs(y))


def bfs(self, x, y):
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    q = [(0, 0, 0)]
    visited = set()
    visited.add((0, 0)) 
    while len(q) > 0:
        i, j, dis = q.pop(0)
        for move in moves:
            a, b = i + move[0], j + move[1]
            if (a,b) not in visited and a >= -5 and b >= -5:
                if a == x and b == y:
                    return dis + 1
                q.append((a, b, dis+1))
                visited.add((a, b))
--------------------------------------------------------------------------------------

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        ## RC ##
        ## APPROACH : BFS ##
        if x == 0 and y == 0: return 0  # must
        directions = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        queue = collections.deque([(0, 0, 0)])
        visited = set([(0,0)])
        x, y = abs(x), abs(y)  # as knight moves are symmetric we donot need to BFS in all four quadrants, moves to reach (-2,100) and (2, 100) and (-2,-100) and (2,-100) are all same. so we are moving only in first quadrant.
        while queue:
            i, j, d = queue.popleft()
            for di, dj in directions:
                if ((i + di, j + dj) not in visited) and ( d < 2 or (i + di >= 0 and j + dj >= 0)):     # d < 2, for x,y = (1,1) ans will be 4 without this ans is 2
                    if i + di == x and j + dj == y:
                        return d + 1
                    queue.append((i + di, j + dj, d + 1))
                    visited.add((i + di, j + dj))  
-------------------------------------------------------------------------------

from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:  
        if x == 0 and y == 0:
            return 0
        queue = deque([(0,0,0)])
        directions = [[-2,1],[-2,-1],[-1,2],[-1,-2],[1,2],[1,-2],[2,1],[2,-1]]
        visited = set()
        visited.add((0,0))
        while queue:
            cur_r,cur_c,move = queue.popleft()  
            for d_r,d_c in directions:
                i_r,i_c = cur_r + d_r, cur_c + d_c
                if (i_r,i_c) not in visited:
                    if i_r == x and i_c == y:
                        return move + 1 
                    queue.append((i_r,i_c,move+1))
                    visited.add((i_r,i_c))
                    
                
      
      
        
        
