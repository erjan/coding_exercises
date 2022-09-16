'''
You are given a 0-indexed 2D integer array grid of size m x n that represents a map of the items in a shop. The integers in the grid represent the following:

0 represents a wall that you cannot pass through.
1 represents an empty cell that you can freely move to and from.
All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.
It takes 1 step to travel between adjacent grid cells.

You are also given integer arrays pricing and start where pricing = [low, high] and start = [row, col] indicates that you start at the position (row, col) and are interested only in items with a price in the range of [low, high] (inclusive). You are further given an integer k.

You are interested in the positions of the k highest-ranked items whose prices are within the given price range. The rank is determined by the first of these criteria that is different:

Distance, defined as the length of the shortest path from the start (shorter distance has a higher rank).
Price (lower price has a higher rank, but it must be in the price range).
The row number (smaller row number has a higher rank).
The column number (smaller column number has a higher rank).
Return the k highest-ranked items within the price range sorted by their rank (highest to lowest). If there are fewer than k reachable items within the price range, return all of them.

 
 '''

from collections import deque

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        def in_range(i, j):
            return 0 <= i < R and 0 <= j < C and grid[i][j] != 0
        
        R, C = len(grid), len(grid[0])
        dist = [[float('inf') for _ in range(C)] for _ in range(R)]
        
        queue = deque()
        queue.append((0, start))
        dist[start[0]][start[1]] = 0
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            curr_dist, (i, j) = queue.popleft()
            for move_i, move_j in moves:
                new_i, new_j = i + move_i, j + move_j
                if in_range(new_i, new_j) and dist[new_i][new_j] == math.inf:
                    dist[new_i][new_j] = curr_dist + 1
                    queue.append((curr_dist + 1, (new_i, new_j)))
        
        data = []
        for i in range(R):
            for j in range(C):
                if pricing[0] <= grid[i][j] <= pricing[1] and dist[i][j] != math.inf:
                    data.append((dist[i][j], grid[i][j], i, j))
        
        return [[i, j] for (_, _, i, j) in sorted(data)[:k]]
      
-----------------------------------------------------------------------

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        lo, hi = pricing
        mr, mc = len(grid), len(grid[0])
        ans, dist = [], 0
        if lo <= grid[start[0]][start[1]] <= hi:
            ans.append(start)
        grid[start[0]][start[1]] = 0
        paths = deque([[0, start[0], start[1]]])                    # dist, row, col

        while paths:
            dist += 1
            batch = []                                              # each batch has the same distance
            while paths and paths[0][0] < dist:
                _, row, col = paths.popleft()
                for r, c in ((row-1, col), (row, col-1), (row, col+1), (row+1, col)):
                    if -1 < r < mr and -1 < c < mc and grid[r][c]:  # neither wall nor processed
                        if lo <= grid[r][c] <= hi:                  # is an item with a good price
                            batch.append([grid[r][c], r, c])        # put it in "batch"
                        paths.append([dist, r, c])                  # one can pass, so put it in "paths"
                        grid[r][c] = 0                              # to avoid duplication
            ans.extend([[r, c] for _, r, c in sorted(batch)])
            if len(ans) >= k:
                break
        return ans[:k]
