'''
There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.

 

Example 1:

Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301
Explanation: 
The first event occurs at timestamp = 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already friends anything happens.
The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends we have that all become friends.
Example 2:

Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3
'''

 def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        self.n = N
        self.arr = [i for i in range(N)]
        logs = sorted(logs, key=lambda x: x[0])
        for op in logs:
            if self.union(op[1], op[2]):
                return op[0]
        return -1
    
    def union(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)
        if root1 != root2:
            self.arr[root2] = root1
            self.n -= 1
        return True if self.n == 1 else False
    
    def find(self, p):
        root = p
        while root != self.arr[root]:
            root = self.arr[root]
            
        # doing path compression for better perf
        while p != root:
            n = self.arr[p]
            self.arr[p] = root
            p = n
        
        return root
---------------------------------------------------------------------------

class Solution:
    '''
    When we have identical roots =>
    `count` won't be decreased. 
    Hecnce, [[0,1],[3,4],[2,3],
    [1,5],[2,4],[0,3]].
    1. union(0,1) -> different roots
    2. union(3,4) -> different roots
    3. union(2,3) -> different roots
    4. union(1,5) -> different roots
    
    5. union(2,4) -> SAME ROOTS. As
    2 has root of 3 and 4 has root of 3
    hence we don't decrease -1
    
    6. union(0,3) -> different roots
    And at this moment we have
    graph.count == 1
    
    '''
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        graph = UnionFind(n)
        
        for data in logs:
            graph.union(data[1], data[2])
            if graph.count == 1:
                return data[0]
    
        return -1


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = size
    
    def find(self, vert):
        if self.root[vert] == vert:
            return vert
        self.root[vert] = self.find(self.root[vert])
        return self.root[vert]
    
    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            if self.rank[r1] > self.rank[r2]:
                self.root[r2] = r1
            elif self.rank[r1] < self.rank[r2]:
                self.root[r1] = r2
            else:
                self.root[r2] = r1
                self.rank[r1] += 1

            self.count -= 1
--------------------------------------------------------------------

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # Initilizing Disjoint set
        root = [i for i in range(n)]
        rank = [1 for i in range(n)]
        groupsOfFriends = n
        def union(x, y):
            #Union using union-by-rank
            rootX, rootY = find(x), find(y)
            if(rootX != rootY):
                if(rank[rootX] > rank[rootY]): root[rootY] = rootX
                if(rank[rootX] < rank[rootY]): root[rootX] = rootY
                if(rank[rootX] == rank[rootY]): 
                    root[rootX] = rootY
                    rank[rootX] +=1
                return True
            return False
        def find(x):
            #Find using path compression
            if(root[x] == x):return x
            root[x] = find(root[x])
            return root[x]
        
        # Sorts logs O(nlogn)
        logs.sort()
        currTimestamp = -1
        
        for log in logs:
            if(groupsOfFriends <= 1): return currTimestamp
            
            currTimestamp = -1
            val = union(log[1], log[2])
            
            if(val): groupsOfFriends -=1
            currTimestamp = log[0]
            
        if(groupsOfFriends <= 1): return currTimestamp
        
        return -1
-----------------------------------------------------------------------------------------


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        self.count = size
    
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
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
    
    def getCount(self):
        return self.count
    
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)       
        data = sorted(logs, key = lambda x: x[0])
        for time, n1, n2 in data:
            uf.union(n1, n2)
            if uf.getCount() == 1:
                return time    
        return -1
-------------------------------------------------------------------------------

class UnionFind: 
    
    def __init__(self, n): 
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, p): 
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    
    def union(self, p, q): 
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False 
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True 
        
        
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        for t, u, v in sorted(logs): 
            if uf.union(u, v): n -= 1
            if n == 1: return t
        return -1 
      
      
            
      
