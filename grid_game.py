'''
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.
'''


'''
Since the robots cannot go up, we need to find the best point i for the first robot to go down.

For the second robot, we only have two choices - go down right away, or stay up till the end.

For a point i, the second robot can either collect bottom = sum(grid[1][0] .. grid[1][i - 1]) if it goes down, or top = sum(grid[0][i + 1] ... grid[0][n - 1]) otherwise.

We can compute those values using prefix/suffix sum in O(1), and then find the minimum of max(top, bottom).

Note that the prefix/suffix sum can overflow int, so we need to use a 64-bit integer in C++ and Java.
'''


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top, bottom = sum(grid[0]), 0
        ans = float("inf")
        
        for i in range(n):
            top -= grid[0][i]
            ans = min(ans, max(top, bottom))
            bottom += grid[1][i]
        
        return ans
      
--------------------------------------------------------------
class Solution(object):
    def gridGame(self, grid):
        
        top, bottom = grid
        top_sum = sum(top)
        bottom_sum = 0
        res = float('inf')
        
        for i in range(len(top)):
            top_sum -= top[i]
            res = min(res, max(top_sum, bottom_sum))
            bottom_sum += bottom[i]
            
        return res
