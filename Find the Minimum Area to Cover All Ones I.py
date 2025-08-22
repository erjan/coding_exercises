'''
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.
'''

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
        res = 0

        m = len(grid)
        n = len(grid[0])

        minrow, maxrow = m,-1
        mincol,maxcol = n,-1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    minrow = min(minrow,i)
                    maxrow = max(maxrow, i)
                    mincol = min(mincol,j)
                    maxcol = max(maxcol,j)
                
        return (maxrow-minrow+1)*(maxcol-mincol+1)
