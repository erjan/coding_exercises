'''
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a 
square to another 4-directionally adjacent square if and only if the elevation of both squares individually 
are at most t. You can swim infinite distances in zero time. Of course, you must stay 
within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0)
'''



class Solution:
    def swimInWater(self, M: List[List[int]]) -> int:
        n = len(M)
        Queue = [(M[0][0],0,0)]
        dist = {}
        while Queue:
            t, i, j = heappop(Queue)
            if i == n - 1 and j == n - 1: return t
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < n and ((x, y) not in dist or dist[(x, y)] > max(t, M[x][y])):
                    dist[(x,y)] = max(t, M[x][y])
                    heappush(Queue,(dist[(x,y)],x,y))
                    
------------------------------------------------------------------------------------------------------------------
class Solution:
    def swimInWater(self, grid) -> int:
        """
        Given an NxN grid whose elements are a permutation of
        the array [0, 1, ..., NxN - 1], this program determines
        the least time needed to reach the bottom right cell
        from the top left cell. It uses binary search combined
        with depth-first search (dfs) to determine the answer.

        :param grid: square matrix where each cell represents
                     an elevation
        :type grid: list[list[int]]
        :return: least time needed to reach bottom right cell
                 from the top left cell.
        :rtype: int
        """

        def dfs(row: int, col: int, swim_time: int, visited) -> bool:
            """
            Given the row and column location of a cell (row, col),
            a candidate swim time (swim_time), and the set of
            cells already visited (visited), this program uses
            depth-first search recursively to determine whether
            it is possible to reach the bottom right cell of
            the grid within swim_time.
            
            :param row: cell row
            :type row: int
            :param col: cell column
            :type col: int
            :param swim_time: candidate swim time
            :type swim_time: int
            :param visited: set of cells already visited with
                            each cell represented as (row, col)
                            tuple
            :type visited: set(tuple)
            :return: True if it is possible to reach the bottom
                     right cell (grid[-1][-1] within swim_time,
                     else False
            :rtype: bool
            """
            
            """
            Return False when:
            - given location defined by row and col is off the grid
            - given location has already been visited
            - the cell time (cell_time) is greater than swim_time
            """
            if row < 0 or row >= len_grid or col < 0 or col >= len_grid:
                return False
            if (row, col) in visited:
                return False
            visited.add((row, col))
            cell_time = grid[row][col]
            if cell_time > swim_time:
                return False
            
            """
            Return True if the given location is the bottom
            right cell of the grid.
            """
            if row == len_grid - 1 and col == len_grid - 1:
                return True
            
            """
            Perform depth-first search (dfs) on all adjacent cells.
            """
            if dfs(row + 1, col, swim_time, visited):
                return True
            elif dfs( row, col + 1, swim_time, visited ):
                return True
            elif dfs( row - 1, col, swim_time, visited ):
                return True
            elif dfs(row, col - 1, swim_time, visited):
                return True
            return False

        """
        Use binary search and dfs to find the lowest swim time
        that enables a swimmer to reach grid[-1][-1] from
        grid[0][0].
        """
        len_grid = len(grid)
        left = grid[-1][-1]
        right = len_grid * len_grid - 1
        while left < right:
            visited = set()
            swim_time = left + (right - left) // 2
            if dfs(0, 0, swim_time, visited):
                right = swim_time
            else:
                left = swim_time + 1
        return left
