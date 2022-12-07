'''
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.
'''


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        parent = [i for i in range(n+1)]
    
        rank = [0 for i in range(n+1)]

        def find(parent, x):

            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, a, b):

            a = find(parent, a)
            b = find(parent, b)

            if a == b:
                return 

            if rank[a] < rank[b]:
                parent[a] = b
            elif rank[a] > rank[b]:
                parent[b] = a
            else:
                parent[b] = a
                rank[a] += 1
                
        edgeList.sort(key = lambda x: x[2])
        res = [0] * len(queries)
        queries = [[i, ch] for i, ch in enumerate(queries)]
        queries.sort(key = lambda x: x[1][2])
        
        ind = 0
        for i, (a, b, w) in queries:
            
            while ind < len(edgeList) and edgeList[ind][2] < w:
                union(parent, edgeList[ind][0], edgeList[ind][1])
                ind += 1
                
            res[i] = find(parent, a) == find(parent, b)
        return res
      
-----------------------------------------------------------------------------------------------------
class UnionFind:

    def __init__(self, size):
        self.size = size
        self.parents = list(range(size))
        self.sizes = [0] * size
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty: return
        small, big = (rootx, rooty) if self.sizes[rootx] < self.sizes[rooty] else (rooty, rootx)
        self.parents[small] = big
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        
        edgeList.sort(key=lambda x: x[2])
        answers = [None] * len(queries)
        queries = [(l, s, d, i) for i, (s, d, l) in enumerate(queries)]
        queries.sort(key=lambda x:x[0])
        
        eidx = 0
        for limit, src, dest, q_idx in queries:
            while eidx < len(edgeList) and edgeList[eidx][2] < limit:
                uf.union(edgeList[eidx][0], edgeList[eidx][1])
                eidx += 1
            
            answers[q_idx] = uf.find(src) == uf.find(dest)
        
        return answers
      
      
