'''
There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.
'''

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)       # build graph
        for a, b, w in edges:
            graph[a].append((w, b))
            graph[b].append((w, a))
        heap = graph[n]
        heapq.heapify(heap)
        d = {n: 0}
        while heap:                                 # Dijkstra from node `n` to other nodes, record shortest distance to each node
            cur_w, cur = heapq.heappop(heap)
            if cur in d: continue
            d[cur] = cur_w
            for w, nei in graph[cur]:
                heapq.heappush(heap, (w+cur_w, nei))
        graph = collections.defaultdict(list)
        for a, b, w in edges:                       # pruning based on `restricted` condition, make undirected graph to directed-acyclic graph
            if d[a] > d[b]:
                graph[a].append(b)
            elif d[a] < d[b]:
                graph[b].append(a)
        ans, mod = 0, int(1e9+7)
        @cache
        def dfs(node):                              # use DFS to find total number of paths
            if node == n:
                return 1
            cur = 0 
            for nei in graph[node]:
                cur = (cur + dfs(nei)) % mod
            return cur    
        return dfs(1)
