'''
There is a knight on an n x n chessboard. In a valid configuration, the knight starts at the top-left cell of the board and visits every cell on the board exactly once.

You are given an n x n integer matrix grid consisting of distinct integers from the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col) is the grid[row][col]th cell that the knight visited. The moves are 0-indexed.

Return true if grid represents a valid configuration of the knight's movements or false otherwise.

Note that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.
'''

#bfs

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        
        q = deque( [(0, 0)] )
        res = 0
        
        while q:
            res += 1
            x, y = q.popleft()

            for i, j in [ (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2), (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1) ]:
                if 0 <= i < n and 0 <= j < n and grid[i][j] == grid[x][y] + 1:
                    q.append( (i, j) )

        return res == pow(n, 2)
      
-------------------------------------------------------------------

#bfs2

class Solution:       
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        r1,c1=0,0
        src=0
        dest=(len(grid)*len(grid))-1
        queue=collections.deque([(r1,c1,src)])
        vis=[[0 for i in range(len(grid))] for j in range(len(grid))]
        while queue:
            row,col,src=queue.popleft()
            vis[row][col]=1
            if src==dest:
                return True
            dx=[1,2,1,2,-1,-2,-1,-2]
            dy=[2,1,-2,-1,2,1,-2,-1]
            for i in range(8):
                newr=row+dx[i]
                newc=col+dy[i]
                #print(newr,newc)
                if 0<=newr<len(grid) and 0<=newc<len(grid) and vis[newr][newc]!=1:
                    if grid[newr][newc]==(src+1):
                        queue.append((newr,newc,src+1))
                        
        return False
      
--------------------------------------------------------------------------------------------------------------

#dfs

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        size = n*n
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)]

        def dfs(i, j, curr_size):
            if curr_size == size-1:
                return True
            
            next_position = grid[i][j]+1

            for d in directions:
                x, y = d
                r = x + i
                c = y + j
                if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != next_position:
                    continue

                ans = dfs(r, c, curr_size + 1)
                if ans:
                    return ans
            return False
        return dfs(0, 0, 0)
---------------------------------------------------------------------------------------

_VALID_MOVES: List[Tuple[int, int]] = [
        (-1, -2),                     (1, -2),
    (-2, -1),                             (2, -1),
    
    (-2, 1),                                (2, 1),
        (-1, 2),                        (1, 2)
]

class Solution:    
    def is_valid(self, grid: List[List[int]], x: int, y: int, expected_pos: int) -> bool:
        if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0 or grid[x][y] != expected_pos:
            return False
        
        if expected_pos == len(grid) * len(grid[0]) - 1:
            return True
        
        return any(self.is_valid(grid, x + dx, y + dy, expected_pos + 1) for dx, dy in _VALID_MOVES)

    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        return self.is_valid(grid, 0, 0, 0)
