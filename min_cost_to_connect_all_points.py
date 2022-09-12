'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
'''

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for record in c[j]: heapq.heappush(heap, record)
            if cnt >= n: break        
        return ans
      
-------------------------------------
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d, res = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}, 0
        while d:
            x, y = min(d, key=d.get)  # obtain the current minimum edge
            res += d.pop((x, y))      # and remove the corresponding point
            for x1, y1 in d:          # for the rest of the points, update the minimum manhattan distance
                d[(x1, y1)] = min(d[(x1, y1)], abs(x-x1)+abs(y-y1))
        return res
      
--------------------------------------------------
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        parent = list(range(len(points)))
        g = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                g.append((i, j, abs(points[j][1]-points[i][1]) + abs(points[j][0]-points[i][0])))
        
        cost = 0
        for u, v, w in sorted(g, key=lambda x:x[2]):
            ru, rv = find(u), find(v)
            if ru == rv:    # u and v must not be connected for now
                continue
            parent[ru] = rv
            cost += w
        
        return cost
----------------------------------------------------------------------------------
def minCostConnectPoints(self, points: List[List[int]]) -> int:
    #prims
    g = defaultdict(list)
    n = len(points)
	#create graph
    for i in range(n):
        for j in range(n):
            if i != j:
                g[i].append((abs(points[j][0]-points[i][0])+abs(points[j][1]-points[i][1]), j))
    
    heap = [(0,0)]
    ans = 0
    visited = set()
    while heap:
        weight, to = heapq.heappop(heap)
        if to in visited:
            continue
        ans += weight
        visited.add(to)
        
        for cost, nei in g[to]:
            if nei not in visited:
                heapq.heappush(heap, (cost, nei))
    
    return ans
