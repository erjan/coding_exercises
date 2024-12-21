'''
There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.

A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the values of its nodes.

Return the maximum number of components in any valid split.
'''

class Solution:
    def __init__(self):
        self.cnt = 0

    def getSubtree(self, node,adj,parent,subtree):
        if len(adj[node])==1 and adj[node][0]==parent:
            return
        for neib in adj[node]:
            if neib!=parent:
                self.getSubtree(neib,adj,node,subtree)
                subtree[node]+=subtree[neib]
        
    def dfs(self,node,adj,parent,subtree,k):
        if len(adj[node])==1 and adj[node][0]==parent:
            return
        
        for neib in adj[node]:
            if neib!=parent:
                parSubtree = subtree[node]-subtree[neib]
                childSubtree = subtree[neib]
                if parSubtree%k == 0 and childSubtree%k==0:
                    self.cnt+=1
                    subtree[node]-=subtree[neib]
                else:
                    subtree[neib]=subtree[node]
                self.dfs(neib,adj,node,subtree,k)

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        subtree = [val for val in values]
        self.getSubtree(0,adj,-1,subtree)
        self.dfs(0,adj,-1,subtree,k)
        return self.cnt+1
        
