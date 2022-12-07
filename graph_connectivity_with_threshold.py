'''
We have n cities labeled from 1 to n. Two different cities with labels x and y are directly connected by a bidirectional road if and only if x and y share a common divisor strictly greater than some threshold. More formally, cities with labels x and y have a road between them if there exists an integer z such that all of the following are true:

x % z == 0,
y % z == 0, and
z > threshold.
Given the two integers, n and threshold, and an array of queries, you must determine for each queries[i] = [ai, bi] if cities ai and bi are connected directly or indirectly. (i.e. there is some path between them).

Return an array answer, where answer.length == queries.length and answer[i] is true if for the ith query, there is a path between ai and bi, or answer[i] is false if there is no path.
'''

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

        self.rank = [1] * size


    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

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
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        import math
        
        @lru_cache
        def gcd(x, y):
            return math.gcd(x, y)
        
        uf = UnionFind(n+1)
        for k in range(threshold+1, n+1):
            std = k
            for num in range(std, n+1, k):
                uf.union(std, num)
                    
        for i in range(len(queries)):
            queries[i] = uf.connected(queries[i][0], queries[i][1])
        return queries
      
----------------------------------------------------------------------------------------------------------------
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        G = defaultdict(set)
        for i in range(max(1,threshold+1),n+1):
            for j in range(i,n+1,i):
                G[i+n].add(j)
                G[j].add(i+n)

        color = {}
        seed = 0
        def dfs(i,col):
            color[i]=col
            for j in G[i]:
                if j not in color:
                    dfs(j,col)
        
        for i in range(1,n+1):
            if i not in color:
                seed+=1
                dfs(i,seed)
        return [color[i]==color[j] for i,j in queries]
