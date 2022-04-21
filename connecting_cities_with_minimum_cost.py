'''
There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,

The cost is the sum of the connections' costs used.
'''



use a dictionary to store the information.
The key is a city.
The value is a tuple. The first element in the tuple is the neighbor to the key's city, and the second element in the tuple is the cost from the neighbor city to the key's city. There will be multiple cities connected to the key's city.
Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]

neighbor = {
			1: (2,5),(3,6)
			2: (1,5),(3,1)
			3: (1,6),(2,1)
			}
Use a minimum heap to store the cost and neighbors of the current city. The minimum heap sorts the cost in ascending order. So each time the neighbor pop from the heap will be the neighbor who has the least cost to the current city.
mini_heap = [(cost from current city to neighbor to current city, neighbor to current city )]
from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        neighbor = defaultdict(list)
        for i, j, c in connections:
            neighbor[i].append((j, c))
            neighbor[j].append((i, c))
        #print(nbrs)    
        res = 0
        mini_heap = [(0,1)]
        visited = set()
        while mini_heap:
            c, i = heappop(mini_heap)
            if i in visited:
                continue
            else:
                visited.add(i)
                res += c
                if len(visited) == N: 
                    return res
                else:
                    for j, c in neighbor[i]:
                        if j in visited: 
                            continue
                        else:
                            heappush(mini_heap, (c, j))
        return -1
      
---------------------------------------------------------------------------------    

Questions are welcome.

Steps:

Sort connections by cost (ascending).
If city a and city b are not connected, spend cost c to connect them.
Keep track of which cities are connected in a union find data structure.
Check if all N cities are connected.
Detailed Approach: (click to show)

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda c: c[2])
        uf = UnionFind()
        for a, b, c in connections:
            uf.union(a, b, c)
        return uf.cost if len(uf.group) == 1 and len(uf.group[uf.id[a]]) == N else -1

class UnionFind:
    def __init__(self):
        self.group_id = 0
        self.group = {}
        self.id = {}
        self.cost = 0
        
    def union(self, a, b, c):
        """
        City a and city b are connected by a road that costs c to build.
        If a and b are not already in the same group, connect the two cities with a new road for cost c.
        """
        A, B = a in self.id, b in self.id
        if A and B and self.id[a] != self.id[b]:
            self.merge(a, b)
        elif A and B:
            self.cost -= c
        elif A or B:
            self.add(a, b)
        else:
            self.create(a, b)
        self.cost += c
    
    def merge(self, a, b):
        """City a and city b belong to different groups, connect the two groups with a road to form one big group."""
        obs, targ = sorted((self.id[a], self.id[b]), key = lambda i: len(self.group[i]))
        for node in self.group[obs]:
            self.id[node] = targ
        self.group[targ] |= self.group[obs]
        del self.group[obs]
    
    def add(self, a, b):
        """Either city a or city b does not have a group, add the new city to the existing group."""
        a, b = (a, b) if a in self.id else (b, a)
        targ = self.id[a]
        self.id[b] = targ
        self.group[targ] |= {b}
    
    def create(self, a, b):
        """Neither city a nor city b is part of a group, make a new group {a, b}."""
        self.group[self.group_id] = {a, b}
        self.id[a] = self.id[b] = self.group_id
        self.group_id += 1
        
---------------------------------------------------------------------------

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        if len(connections) < N - 1:
            return -1
        
        self.createSets(N)

        total = 0
        for c1, c2, cost in sorted(connections, key=itemgetter(2)):
            if self.find(c1) == self.find(c2):
                continue
                
            total += cost
            
            self.union(c1, c2)
            if self.num_sets == 1:
                break
            
        return total if self.num_sets == 1 else -1

    def createSets(self, N):
        self.parent = list(range(0, N + 1))
        self.rank = [0] * (N + 1)
        self.num_sets = N 
    
    def find(self, c):  # find with path compression
        root = c        
        while self.parent[root] != root:
            root = self.parent[root]
            
        # path compression
        while self.parent[c] != c:
            c, self.parent[c] = self.parent[c], root
                
        return root
    
    def union(self, c1, c2):  # union by rank
        root1 = self.find(c1)
        root2 = self.find(c2)
       
        if self.rank[root1] == self.rank[root2]:
            self.parent[root1] = root2
            self.rank[root2] += 1
        else:            
            if self.rank[root1] > self.rank[root2]:
                root1, root2 = root2, root1 
                
            self.parent[root1] = root2
        
        self.num_sets -= 1
----------------------------------------------------------

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)] #initially each node is parent of itself, i.e., self.parent[i] = i
        self.components = n # no. of connected components
        self.size = [1] * n # size of different groups, which can be found by self.size[self.find(i)]
    
    def find(self, p):
        root = p
        while root != self.parent[root]:
            root = self.parent[root]
        
        # path compression
        while p != root:
            p, self.parent[p] = self.parent[p], root
            
        return root
    
    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return
			
		# combining the group with smaller no. of elements to the larger group
        if self.size[parent_u] > self.size[parent_v]:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        else:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        self.components -= 1
    
    def isConnected(self, u, v):
        return self.find(u) == self.find(v)


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda x : x[2])
        uf = UF(N)
        minCost = 0
        for city1, city2, cost in connections:
            if not uf.isConnected(city1 - 1, city2 - 1):
                uf.union(city1 - 1, city2 - 1)
                minCost += cost
        
        if all(uf.isConnected(i, i + 1) for i in range(N - 1)):
            return minCost
        else:
            return -1
----------------------------------------------------------------------------

def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # greedy, sort by cost and try to union edge if not already connected
        def find(i: int) -> int:
            if roots[i] != i:
                roots[i] = find(roots[i])
            return roots[i]

        if N < 2 or not connections:
            return 0
        connections.sort(key=lambda l: l[2])

        roots = [i for i in range(N + 1)]
        res = 0
        for x, y, v in connections:
            rx, ry = find(x), find(y)
            if rx != ry:
                res += v
                roots[rx] = ry
        return res if len({find(i) for i in range(1, N + 1)}) == 1 else -1
          
        
        
