'''
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.
'''

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def gen_next(p):
            directions = [(0,-1,2), (0,1,1), (1,0,3), (-1,0,4)]
            for x, y, d in directions:
                yield x, y, (0 if d == p else 1)
        visited = set()
        q = [(0,0,0)]
        while len(q) > 0:
            cost, x, y = heapq.heappop(q)
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return cost
            if (x, y) not in visited:
                visited.add((x,y))
                for dx, dy, c in gen_next(grid[x][y]):
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_y < len(grid[0]) and 0 <= new_x < len(grid):
                        heapq.heappush(q, (cost+c, new_x, new_y))

---------------------------------------------------------------------------------------
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        dir=[0,[0,1],[0,-1],[1,0],[-1,0]]
        n=len(grid)
        m=len(grid[0])
        
        q=[[0,0,0]]
        visit=set()
        
        while q:
            val,i,j=heapq.heappop(q)
            if i==n-1 and j==m-1:
                return val
            if i<0 or i>=n or j<0 or j>=m or (i,j) in visit:
                continue
            visit.add((i,j))
            for d in range(1,5):
                heapq.heappush(q,[val+int(grid[i][j]!=d),i+dir[d][0],j+dir[d][1]])
        
        
                        
