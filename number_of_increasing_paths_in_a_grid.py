'''
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.
'''


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = {}
        mod = (10 ** 9) + 7

        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] <= prev:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            pathLength = 1
            pathLength += (dfs(r + 1, c, grid[r][c]) + dfs(r - 1, c, grid[r][c]) +
                dfs(r, c + 1, grid[r][c]) + dfs(r, c - 1, grid[r][c]))
            dp[(r, c)] = pathLength
            return pathLength
            
        count = 0
        for r in range(rows):
            for c in range(cols):
                count += dfs(r, c, 0)

        return count % mod
      
---------------------------------------------------------------------------------------------------      

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dir = [[1,0],[0,1],[-1,0],[0,-1]]

        dp = {}

        def dfs(r,c):
            
            if (r,c) in dp:
                return dp[(r,c)]
                
            ans = 1
            for dr,dc in dir:
                if 0<=r+dr<ROWS and 0<=c+dc<COLS and grid[r+dr][c+dc]>grid[r][c]:
                    ans += dfs(r+dr,c+dc)
            
            dp[(r,c)] = ans%1000000007

            return ans%1000000007

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res += dfs(r,c)

        return res%1000000007
        
-------------------------------------------------------------------------------------------------
def count_paths(grid, y, x, mem):
    if (y, x) in mem:
        return mem[(y, x)]
    local_counter = 1
    if y > 0 and grid[y - 1][x] > grid[y][x]:
        local_counter += count_paths(grid, y - 1, x, mem)
        
    if y + 1 < len(grid) and grid[y + 1][x] > grid[y][x]:
        local_counter += count_paths(grid, y + 1, x, mem)
        
    if x > 0 and grid[y][x - 1] > grid[y][x]:
        local_counter += count_paths(grid, y, x - 1, mem)
    
    if x + 1 < len(grid[0]) and grid[y][x + 1] > grid[y][x]:
        local_counter += count_paths(grid, y, x + 1, mem)
    mem[(y, x)] = local_counter
    return local_counter
    

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mem = {}
        counter = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                counter += count_paths(grid, y, x, mem)
        return counter % (10 ** 9 + 7)
