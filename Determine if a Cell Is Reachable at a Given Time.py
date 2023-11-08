'''
You are given four integers sx, sy, fx, fy, and a non-negative integer t.

In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.

Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.


 '''



class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        if sx == fx and sy == fy:
            return t>1 or t == 0

        height_diff = abs(sy-fy)
        width_diff = abs(sx-fx)

        extra_time = abs(height_diff - width_diff)
        return (min(height_diff, width_diff) + extra_time)<=t
