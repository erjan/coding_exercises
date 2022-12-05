'''
There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.
'''
'''
There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.
'''


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        
        g = defaultdict(list)
        
        # start from node with minimum val
        for a, b in edges:
            heappush(g[a], (vals[b], b))
            heappush(g[b], (vals[a], a))

        
        loc = list(range(n))
        
        def find(x):
            if loc[x] != x:
                loc[x] = find(loc[x])
            return loc[x]
        
        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                loc[b] = a
        
        # node by val
        v = defaultdict(list)
        for i, val in enumerate(vals):
            v[val].append(i)
        
        ans = n
        
        
        for k in sorted(v):
            for node in v[k]:
                # build graph if neighboring node <= current node val
                while g[node] and g[node][0][0] <= k:
                    nei_v, nei = heappop(g[node])
                    union(node, nei)
            
            # Count unioned groups
            grp = Counter([find(x) for x in v[k]])
            
            # for each unioned group, select two nodes (order doesn't matter)
            ans += sum(math.comb(x, 2) for x in grp.values())            
        
        return ans
      
---------------------------------------------------------------------------------------------------------
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        adj_list = defaultdict(list)
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        nodes = defaultdict(list)
        for i, v in enumerate(vals):
            nodes[v].append(i)
        
        uf = UnionFind(len(vals))
        
        ans = 0
        for v in sorted(nodes.keys()):
        
            # Add nodes with value v
            for i in nodes[v]:
                for j in adj_list[i]:
                    if vals[j] <= vals[i]:
                        uf.union(i, j)
            
            # Count number of nodes with value v in its root
            cnt = defaultdict(int)
            for i in nodes[v]:
                cnt[uf.find(i)] += 1
            
            # For each subtree that contains x nodes with value v,
            # it has x + (x choose 2) = x + x * (x - 1) // 2 good paths.
            for x in cnt.values():
                ans += x + x * (x - 1) // 2
        
        return ans
        
class UnionFind:
    """
    Disjoint-set forest implemented by union-find with
    1. path compression find()
    2. weighted union()
    Both find() and union() have an amortized O(a(n)) time complexity
    """
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, p: int) -> int:
        """find root with path compression"""
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int) -> None:
        """weighted union: join small tree to large tree"""
        root1 = self.find(p)
        root2 = self.find(q)
        if self.size[root1] >= self.size[root2]:
            root1, root2 = root2, root1
        # size of root1 is always smaller
        self.parent[root1] = self.parent[root2]
        self.size[root2] += self.size[root1]
