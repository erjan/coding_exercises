'''
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.
'''


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        right = (0, 1, {1, 3, 5})
        left = (0, -1, {1, 4, 6})
        down = (1, 0, {2, 5, 6})
        up = (-1, 0, {2, 3, 4})
        
        directions = {
            1: [right, left],
            2: [up, down],
            3: [left, down],
            4: [right, down],
            5: [left, up],
            6: [right, up]
         }
        
        def traverse(i, j):
            if i == rows - 1 and j == cols - 1:
                return True
            visited.add((i, j))
            
            for d in directions[grid[i][j]]:
                i_next, j_next, valid_next_streets = i + d[0], j + d[1], d[2]
                valid_position = 0 <= i_next < rows and 0 <= j_next < cols
                if valid_position and grid[i_next][j_next] in valid_next_streets and (i_next, j_next) not in visited:
                    if traverse(i_next, j_next):
                        return True
            return False
        
        return traverse(0, 0)
