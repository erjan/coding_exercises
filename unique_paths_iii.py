'''
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
'''



'''
First of all, lets calculate the starting position, ending 
position and total number of empty cells present in the grid. And using Depth First Search (DFS) algorithm and 
Backtracking, we can check the possible paths having no obstacles and add find the valid path 
using visited set. If a valid path is found, then increment the output.
'''
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        start_row,start_col,end_row,end_col = 0,0,0,0
        empty_cells = 0

        # Traversing the grid to find the start and end index
        for i in range(0,rows):
            for j in range(0,cols):
                if (grid[i][j] == 1):
                    start_row,start_col = i,j
                elif (grid[i][j] == 2):
                    end_row,end_col = i,j
                elif (grid[i][j] == 0):
                    empty_cells += 1
        
        self.output = 0
        visited = set()

        def dfs(r,c,visited,walk):
            if (r == end_row and c == end_col):
                if (walk == empty_cells+1):
                    self.output += 1  # Path found
                return

            if (0<= r < rows and 0<= c < cols and grid[r][c] != -1 and (r,c) not in visited):
                visited.add((r,c))
                for i,j in [(0,-1),(0,1),(1,0),(-1,0)]:
                    dfs(r+i,c+j,visited,walk+1)
                visited.remove((r,c))
            
        dfs(start_row,start_col,visited,0)

        return self.output
      
-----------------------------------------------------------------------------------------------------------------------      
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.depth = 0

        def dfs(row, col, non_obstacles):

            if grid[row][col] == 2 and non_obstacles == 1:
                self.depth += 1
                return

            temp = grid[row][col]
            grid[row][col] = -1
            non_obstacles -= 1

            for index1, index2 in directions:

                next_row = index1 + row
                next_col = index2 + col

                if next_row in range(len(grid)) and next_col in range(len(grid[0])) and grid[next_row][next_col] != -1:
                       
                        dfs(next_row, next_col, non_obstacles)

            grid[row][col] = temp

            return self.depth

  
        non_obstacles = 0
        for row in range(len(grid)):

            for col in range(len(grid[0])):

                if grid[row][col] == 1:
                    result = [row, col]
                if grid[row][col] >= 0:
                    non_obstacles += 1

        return dfs(result[0], result[1], non_obstacles)

------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [-1, 0, 1, 0, -1]
        m, n = len(grid), len(grid[0])

        def helper(ans, start, target, cur_count, M, visited, grid):
            if start == target:
                if cur_count == M:
                    return ans + 1
                else:
                    return ans
                
            x, y = start
            for i in range(4):
                next_x, next_y = x + directions[i], y + directions[i + 1]

                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y] and grid[next_x][next_y] != -1:
                    visited[next_x][next_y] = True
                    ans = helper(ans, (next_x, next_y), target, cur_count + 1, M, visited, grid)
                    visited[next_x][next_y] = False
                
            return ans
        
        start, target = None, None
        M = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    target = (i, j)
                elif grid[i][j] == -1:
                    M += 1

        M = m * n - M
                
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[start[0]][start[1]] = True
        return helper(0, start, target, 1, M, visited, grid)






      
