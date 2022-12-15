'''
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queres[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.
'''

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        point = []
        prefix = 0 
        prev = -inf 
        pq = [(grid[0][0], 0, 0)]
        grid[0][0] = 0 
        while pq: 
            v, i, j = heappop(pq)
            if prev != v: point.append((prev, prefix))
            prefix += 1
            prev = v
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]: 
                    vv = max(v, grid[ii][jj])
                    heappush(pq, (vv, ii, jj))
                    grid[ii][jj] = 0
        point.append((prev, prefix))
        ans = []
        for q in queries: 
            i = bisect_left(point, q, key=lambda x: x[0]) - 1
            ans.append(point[i][1])
        return ans 
      
-------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        threshold = [[0 for j in range(n)] for i in range(m)]
        heap = []
        heapq.heappush(heap, [grid[0][0], 0, 0])
        while heap:
            while heap and threshold[heap[0][1]][heap[0][2]] > 0:
                heapq.heappop(heap)
            if heap:
                cost, x, y = heapq.heappop(heap)
                threshold[x][y] = cost
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < m and 0 <= ny < n:
                        heapq.heappush(heap, [max(grid[nx][ny], cost), nx, ny])
        elements = []
        for i in range(m):
            for j in range(n):
                elements.append(threshold[i][j])
        elements.sort()
        
        result = []
        for query in queries:
            result.append(bisect.bisect_left(elements, query))
        return result
        
        
