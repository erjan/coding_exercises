

'''
You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.
'''



class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        visited = [[False] * n for _ in range(m)]
        heap = [(0, 0, 0)] # (t, r, c)
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return t
            if visited[r][c]:
                continue
            visited[r][c] = True
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                    continue
                wait = (grid[nr][nc] - t) % 2 == 0
                nt = max(grid[nr][nc] + wait, t + 1)
                heapq.heappush(heap, (nt, nr, nc))
        return -1
      
---------------------------------------------------------------------------------------------------------------
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] <= 1 or grid[1][0] <= 1: 
            m, n = len(grid), len(grid[0])
            pq = [(0, 0, 0)]
            dist = defaultdict(lambda : inf, {(0, 0) : 0})
            while pq: 
                x, i, j = heappop(pq)
                if (i, j) == (m-1, n-1): return x 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n: 
                        xx = x + 1 + max(0, (grid[ii][jj] - x)//2*2) 
                        if dist[ii, jj] > xx: 
                            heappush(pq, (xx, ii, jj))
                            dist[ii, jj] = xx 
        return -1 
