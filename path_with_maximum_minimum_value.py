'''
Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.

The score of a path is the minimum value in that path.

For example, the score of the path 8 → 4 → 5 → 9 is 4.
'''

class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        DIRS = [[0,1], [1,0], [0,-1], [-1,0]]
        pq = []
        # negate element to simulate max heap
        heappush(pq, (-A[0][0], 0, 0))
        n, m, maxscore = len(A), len(A[0]), A[0][0]
        while len(pq) != 0:
            (a, i, j) = heappop(pq)
            maxscore = min(maxscore, -a)
            if i == n - 1 and j == m - 1:
                break
            for d in DIRS:
                newi, newj = d[0] + i, d[1] + j
                if newi >= 0 and newi < n and newj >= 0 and newj < m and A[newi][newj] >= 0:
                    heappush(pq, (-A[newi][newj], newi, newj))
                    A[newi][newj] = -1;
        return maxscore
-------------------------------------------------------

Since score is bounded by the smallest value in the path, the strategy would be always picking the neighboring cell with the largest value for the next step.
So we can use a priority queue to take all neighboring cells as candidates for the next step. And each time we pop out the largest one to move forward and update score as well.
And I set "seen" cell to -1 to avoid revisiting.
Once we detect the destination as one of the neighboring cells, we finish the path and return the score.

Inspired by @mhelvens, it's faster to move from (m-1,n-1) to (0,0) for Python solution. So we can set (0,0) as destination of the path. This is because Python implements a minHeap, so it will “prefer” popping the point that is closer to (0,0) when it's in the same distance to the destination with other points, and help converge to the destination faster.

def maximumMinimumPath(A):
	m, n = len(A), len(A[0])
	pq, score, A[m-1][n-1] = [(-A[m-1][n-1], m-1, n-1)], A[0][0], -1
	while pq:
		s, i, j = heapq.heappop(pq)
		score = min(-s, score)
		for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
			if not (x or y): 
				return score
			if 0 <= x < m and 0 <= y < n and A[x][y] >= 0:
				heapq.heappush(pq, (-A[x][y], x, y))
				A[x][y] = -1
--------------------------------------------------

lrow = len(A)
lcol = len(A[0])
que = [(-A[0][0],0,0)]
seen = {(0,0)}
heapq.heapify(que)
minVal = float('inf')
while True:
	val,row,col = heapq.heappop(que)
	minVal = min(minVal,-1*val)
	if row == lrow-1 and col == lcol-1:
		return minVal

	for nr,nc in [(row+1,col),(row-1,col),(row,col-1),(row,col+1)]:
		if 0<=nr<lrow and 0<=nc<lcol and (nr,nc) not in seen:
			seen.add((nr,nc))
			heapq.heappush(que,(-A[nr][nc],nr,nc))
------------------------------------------------------------------------------------------------------


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        p = [i for i in range(R * C)]
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[px] = py
                
        points = [(x, y) for x in range(R) for y in range(C)]
        points.sort(key=lambda x:A[x[0]][x[1]], reverse=True)
        
        visited = [[False] * C for _ in range(R)]
        for x, y in points:
            visited[x][y] = True
            
            for nx, ny in [[x-1, y], [x, y+1], [x+1, y], [x, y-1]]:
                if 0 <= nx < R and 0 <= ny < C and visited[nx][ny]:
                    union(x * C + y, nx * C + ny)
                    
            if find(0) == find(R * C - 1):
                return A[x][y]
            
        return -1
      
-----------------------------------------------------------------------------------------------
We want to always expand the path with the largest minimum value. We can use a max heap to keep track of the minimum value in the paths we've discovered.

from heapq import heappush, heappop
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])       
        pq = [(-grid[0][0], 0, 0)]
        grid[0][0] = -1
        ret = -float("inf")
        while pq:
            cur_path_min, cur_i, cur_j = heappop(pq)
            if cur_i == m-1 and cur_j == n-1:
                return -cur_path_min
            for d_i, d_j in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                new_i, new_j = cur_i+d_i, cur_j+d_j
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != -1:
                    heappush(pq, (-min(grid[new_i][new_j], -cur_path_min),new_i, new_j))
                    grid[new_i][new_j] = -1
      
        
      
