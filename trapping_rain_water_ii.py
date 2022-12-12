'''
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
'''

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3: return 0
        # to simplify the code
        def adjacent(i,j):
            return [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
        
        # first we sort all heights from the matrix and store their corresponding positions
        # heights will be [(h1,[p1, p2,...]), (h2,[p1, p2, ...]), ...]
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[heightMap[i][j]].append((i,j))
        heights = sorted(d.items())
        # initialization
        volumn, area, h_lower = 0, 0, heights[0][0]
        level = [[1 for j in range(n)] for i in range(m)]
        for h, positions in heights:
            volumn += area*(h-h_lower)
            h_lower = h
            leak = []
            for i, j in positions:
                # due to height rising, now this position may hold water
                level[i][j] = 0
                area += 1
                if i == 0 or i == m-1 or j == 0 or j == n-1 or any([level[a][b] == -1 for a, b in adjacent(i,j)]):
                    # this position is reachable from outside, therefore cannot hold water
                    leak.append((i,j))
                    level[i][j] = -1
                    area -= 1
            while leak:
                i, j = leak.pop()
                for a, b in adjacent(i,j):
                    if 0 <= a < m and 0 <= b < n and not level[a][b]:
                        # new leaking position found through DFS
                        leak.append((a,b))
                        level[a][b] = -1
                        area -= 1

        return volumn
    
---------------------------------------------------------------------------------------------------------------------------
class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        pq = []
        
        for i in range(m):
            visited[i][0] = True
            heapq.heappush(pq, (grid[i][0], i, 0))
            visited[i][n-1] = True
            heapq.heappush(pq, (grid[i][n-1], i, n-1))
        
        for j in range(n):
            visited[0][j] = True
            heapq.heappush(pq, (grid[0][j], 0, j))
            visited[m-1][j] = True
            heapq.heappush(pq, (grid[m-1][j], m-1, j))
        
        
        res = 0
        while pq:
            val, x, y = heapq.heappop(pq)
            
            if x > 0 and visited[x-1][y] == False:
                visited[x-1][y] = True
                if grid[x-1][y] < val:
                    res += (val-grid[x-1][y])
                    grid[x-1][y] = val
                heapq.heappush(pq, (grid[x-1][y], x-1, y))
                
            if y > 0 and visited[x][y-1] == False:
                visited[x][y-1] = True
                if grid[x][y-1] < val:
                    res += (val-grid[x][y-1])
                    grid[x][y-1] = val
                heapq.heappush(pq, (grid[x][y-1], x, y-1))
            
            if x < m-1 and visited[x+1][y] == False:
                visited[x+1][y] = True
                if grid[x+1][y] < val:
                    res += (val-grid[x+1][y])
                    grid[x+1][y] = val
                heapq.heappush(pq, (grid[x+1][y], x+1, y))
            
            if y < n-1 and visited[x][y+1] == False:
                visited[x][y+1] = True
                if grid[x][y+1] < val:
                    res += (val-grid[x][y+1])
                    grid[x][y+1] = val
                heapq.heappush(pq, (grid[x][y+1], x, y+1))
        
        return res
