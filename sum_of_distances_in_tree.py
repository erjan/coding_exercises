'''
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.
'''

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        res = [0]*n
        for i in range(n):
            q = [i]
            visit = set()
            visit.add(i)
            step, cnt = 1, 0
            while q:
                num = len(q)
                for j in range(num):
                    node = q.pop(0)
                    for nei in g[node]:
                        if nei not in visit:
                            cnt += step
                            visit.add(nei)
                            q.append(nei)
                if q:step+=1
            res[i] = cnt
        
        return res
---------------------------------------------------------------------------------------------
#dfs

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        d = {i:[1, 0] for i in range(n)}
        
        def dfs(root, prev):
            for nei in g[root]:
                if nei != prev:
                    dfs(nei, root)
                    d[root][0] += d[nei][0]
                    d[root][1] += (d[nei][0] + d[nei][1])
        
        def dfs2(root, prev):
            for nei in g[root]:
                if nei != prev:
                    d[nei][1] = d[root][1] - d[nei][0] + (n-d[nei][0])
                    dfs2(nei, root)
        
        dfs(0, -1)
        dfs2(0, -1)
        res = []
        for key in d:
            res.append(d[key][1])
        return res
----------------------------------------------------------------------------------
class Solution:
    def dfs1(self, v):
        self.visited.add(v)
        self.results[v] = [0, 0]
        for u in self.graph[v]:
            if u not in self.visited:
                self.dfs1(u)
                self.results[v][1] += self.results[u][1] + (self.results[u][0] + 1)
                self.results[v][0] += self.results[u][0] + 1
                
    def dfs2(self, v, parent):
        self.visited.add(v)
        if parent != -1:
            self.results[v][1] += self.results[parent][1] - (self.results[v][1] + self.results[v][0] + 1) + (
                self.results[parent][0] - (self.results[v][0] + 1) + 1)
            self.results[v][0] += self.results[parent][0] - (self.results[v][0] + 1) + 1
        for u in self.graph[v]:
            if u not in self.visited:
                self.dfs2(u, v)
                
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.results = defaultdict(int)
        self.graph = defaultdict(set)
        for v, u in edges:
            self.graph[v].add(u)
            self.graph[u].add(v)
        self.visited = set()
        self.dfs1(0)
        self.visited = set()
        self.dfs2(0, -1)
        return [self.results[k][1] for k in range(n)]
