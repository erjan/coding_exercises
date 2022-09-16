'''
You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if they have the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

You should color the border of the connected component that contains the square grid[row][col] with color.

Return the final grid.
'''

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        
        def dfs(r, c, current, border, seen):
            
            # if out of range or seen
            if r<0 or c<0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != current or (r,c) in seen:
                return
            
            seen.add((r,c))
            
            # if it is a border
            if (r==0 or c==0 or r==len(grid)-1 or c==len(grid[0])-1 or grid[r-1][c] != current or grid[r+1][c] != current or grid[r][c-1] != current or grid[r][c+1] != current):
                border.add((r,c))
                
                
            dfs(r-1, c, current, border, seen)
            dfs(r+1, c, current, border, seen)
            dfs(r, c-1, current, border, seen)
            dfs(r, c+1, current, border, seen)
                
            return
        
        if not grid:
            return grid
        
        current = grid[r0][c0]
        border = set()
        seen = set()
        dfs(r0, c0, current, border, seen)
        
        for elem in border:
            grid[elem[0]][elem[1]] = color
        
        return grid
      
-------------------------------------------------------------------------
from queue import Queue
class Solution:
    """
    approach: the problem can be tackled using breadth first approach
    start the bfs from (row, col) and maintain visited and border_set
    """
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        start_color = grid[row][col]
        visited = set()
        
        def is_valid(index):
            i, j = index
            if 0 <= i < m and 0 <= j < n:
                return True
            return False
        
        def is_boundary(index):
            i, j = index
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                return True
            return False
        
        def get_neighbors(index):
            i, j = index
            return [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        
        def dfs(index):
            visited.add(index)
            
            flag = 0
            if is_boundary(index):
                flag = 1
                
            for pos in get_neighbors(index):
                if is_valid(pos) and pos not in visited: 
                    if grid[pos[0]][pos[1]] == start_color:
                        dfs(pos)
                    else:
                        # it's a border point, index needs to be colored with color
                        flag = 1
            if flag:
                grid[index[0]][index[1]] = color
                
        dfs((row, col))
        return grid
