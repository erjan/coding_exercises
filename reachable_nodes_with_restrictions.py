'''
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.
'''

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        res = set(restricted)
        graph = defaultdict(list)
        vis = set()
        
        for u, v in edges:
            if u in res or v in res: continue
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            r = 1
            for nei in graph[node]:
                if nei in vis: continue
                vis.add(nei)
                r += dfs(nei)
            return r
        
        vis.add(0)
        return dfs(0)
      
-----------------------------------------------------------------------------------------------------------------
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        restrictedSet = set(restricted)
        uf = UnionFindSet(n)
        for edge in edges:
            if edge[0] in restrictedSet or edge[1] in restrictedSet:
                continue
            else:
                uf.union(edge[0], edge[1])

        ans = 1
        rootNode = uf.find(0)
        for i in range(1, n):
            if uf.find(i) == rootNode:
                ans += 1
        return ans

class UnionFindSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
