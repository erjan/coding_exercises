'''
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
'''

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        
        if a == b:
            return
        
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        elif self.rank[b] > self.rank[a]:
            a, b = b, a
            
        self.parent[b] = a
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        uf = UnionFind()
        
        for i, j in connections:
            uf.union(i, j)
        
        return sum(uf.find(x) == x for x in range(n)) - 1
