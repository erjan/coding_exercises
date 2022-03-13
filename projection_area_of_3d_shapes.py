'''
You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).

We view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.
'''

#skipped it! just copy pasted solution

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0
        for i in grid:
            area += len(i) - i.count(0) + max(i)
        for i in zip(*grid):
            area += max(i)
        return area
