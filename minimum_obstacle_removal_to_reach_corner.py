'''
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
'''


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[inf]*n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        while pq: 
            x, i, j = heappop(pq)
            if i == m-1 and j == n-1: return x
            for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                if 0 <= ii < m and 0 <= jj < n and x + grid[ii][jj] < dist[ii][jj]: 
                    dist[ii][jj] = x + grid[ii][jj]
                    heappush(pq, (dist[ii][jj], ii, jj))
                    
---------------------------------------------------------------------------------------------
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 0:
            q = [(0, 0, 0)]
        else:
            q = [(0, 0, 1)]
        visit = set()
        
        while q:
            cost, x, y = q.pop(0)
            #print(x, y, cost)
            if x == m-1 and y == n-1:
                return cost
            if x > 0 and (x-1, y) not in visit:
                visit.add((x-1, y))
                if grid[x-1][y] == 0:
                    q.insert(0, (cost, x-1, y))
                else:
                    q.append((cost+1, x-1, y))
            if y > 0 and (x, y-1) not in visit:
                visit.add((x, y-1))
                if grid[x][y-1] == 0:
                    q.insert(0, (cost, x, y-1))
                else:
                    q.append((cost+1, x, y-1))
            if x < m-1 and (x+1, y) not in visit:
                visit.add((x+1, y))
                if grid[x+1][y] == 0:
                    q.insert(0, (cost, x+1, y))
                else:
                    q.append((cost+1, x+1, y))
            if y < n-1 and (x, y+1) not in visit:
                visit.add((x, y+1))
                if grid[x][y+1] == 0:
                    q.insert(0, (cost, x, y+1))
                else:
                    q.append((cost+1, x, y+1))
