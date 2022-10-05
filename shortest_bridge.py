'''
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.
'''

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        
        # DFS paint the first island to 2
        def paint(x: int, y: int) -> None:
            grid[x][y] = 2
            q.append((x, y))
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                    paint(nx, ny)
                    
        def init() -> None:
            for i in range(N):
                for j in range(N):
                    if grid[i][j]:
                        paint(i, j)
                        return
                    
        init()
        
        # BFS level order traversal
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != 2:
                        q.append((nx, ny))
                        if grid[nx][ny] == 1:
                             return level
                        grid[nx][ny] = 2
            level += 1

        return -1
      
-------------------------------------------------------------------------------

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        pos_incs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
        def mark_2(i, j):
            """Mark the island (of grid[i][j]) as 2s."""
            grid[i][j] = 2
            
            for i_inc, j_inc in pos_incs:
                ni, nj = i + i_inc, j + j_inc
                if ni >= 0 and nj >= 0 and ni < rows and nj < cols and grid[ni][nj] == 1:
                    mark_2(ni, nj)

        # Mark the first island to 2s
        marked = False
        for i in range(rows):
            if not marked:
                for j in range(cols):
                    if not marked and grid[i][j] == 1:
                        mark_2(i, j)
                        marked = True
        
        def expand(i, j, mark) -> bool:
            """Expand the island (of grid[i][j]) with the given mark."""
            for i_inc, j_inc in pos_incs:
                ni, nj = i + i_inc, j + j_inc
                if ni >= 0 and nj >= 0 and ni < rows and nj < cols:
                    if grid[ni][nj] == 1:
                        return True
                    elif grid[ni][nj] == 0:
                        grid[ni][nj] = mark

            return False
        
        # Expland the first island as follows:
        #
        #  2    # mark = 2; island
        #
        #  3
        # 323   # mark = 3; after expanding once
        #  3
        #
        #  4
        # 434
        #43234  # mark = 4; after expanding twice
        # 434
        #  4  
        mark = 2
        while True:
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == mark and expand(i, j, mark + 1):
                        return mark - 2
            mark += 1
                    
        raise Exception('Impossible')
