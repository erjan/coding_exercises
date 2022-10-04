'''
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
'''

from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dest in connections:
            graph[src].append((dest, 1))
            graph[dest].append((src, 0))
        
        q = deque([0])
        visited = set([0])
        num_changes = 0
        
        while q:
            curr = q.popleft()
            for child, cost in graph[curr]:
                if child not in visited:
                    visited.add(child)
                    num_changes += cost
                    q.append(child)
                    
        return num_changes
      
------------------------------------------------------------------------------------------
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        # building undirected graph
        for s, e in connections:
            graph[s].append((e, True))
            graph[e].append((s, False))
        
        def dfs(currCity):
            count = 0
            if currCity in visited:
                return
            visited.add(currCity)
            for neigh, orig in graph[currCity]:
                if neigh not in visited:
					# if current path is same as original path that were given from input, 
					# we know that we need to invert the path
                    if orig == True:
                        count += 1
                    count += dfs(neigh)
            return count
			
        return dfs(0)
-----------------------------------------------------------------------------------------------------
Short description:
In this solution, we add cities one by one to the country map. This addition follows 3 rules:
1)If the first city of the road is already on the map, we need to change direction of this road and add a new city to the map.
2)If the second city of the road is already on the map, we only add a new city to the map.
3) If both cities are not on the map, we postpone this road and select next one.

Solution:

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        cmap = {0}
        count = 0
        dq = deque(connections)
        while dq:
            u, v = dq.popleft()
            if v in cmap:
                cmap.add(u)
            elif u in cmap:
                cmap.add(v)
                count += 1
            else:
                dq.append([u, v])
        return count
            
      
