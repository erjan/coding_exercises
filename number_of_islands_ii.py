'''
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

Union Find
is an abstract data structure supporting find and unite on disjointed sets of objects, typically used to solve the network connectivity problem.

The two operations are defined like this:

find(a,b) : are a and b belong to the same set?

unite(a,b) : if a and b are not in the same set, unite the sets they belong to.

With this data structure, it is very fast for solving our problem. Every position is an new land, if the new land connect two islands a and b, we combine them to form a whole. The answer is then the number of the disjointed sets.

The following algorithm is derived from Princeton's lecture note on Union Find in Algorithms and Data Structures It is a well organized note with clear illustration describing from the naive QuickFind to the one with Weighting and Path compression.
With Weighting and Path compression, The algorithm runs in O((M+N) log* N) where M is the number of operations ( unite and find ), N is the number of objects, log* is iterated logarithm while the naive runs in O(MN).

For our problem, If there are N positions, then there are O(N) operations and N objects then total is O(N log*N), when we don't consider the O(mn) for array initialization.

Note that log*N is almost constant (for N = 265536, log*N = 5) in this universe, so the algorithm is almost linear with N.

However, if the map is very big, then the initialization of the arrays can cost a lot of time when mn is much larger than N. In this case we should consider using a hashmap/dictionary for the underlying data structure to avoid this overhead.

Of course, we can put all the functionality into the Solution class which will make the code a lot shorter. But from a design point of view a separate class dedicated to the data sturcture is more readable and reusable.

I implemented the idea with 2D interface to better fit the problem.


class Solution(object):
    def numIslands2(self, m, n, positions):
        ans = []
        islands = Union()
        for p in map(tuple, positions):
            islands.add(p)
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands.id:
                    islands.unite(p, q)
            ans += [islands.count]
        return ans

class Union(object):
    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        self.count -= 1

-------------------------------------------------------------------------------------
Pretty much just Wikipedia's Disjoint-set forests, using "union by rank" and "path compression". I don't see the point of m and n, so I ignore them.

def numIslands2(self, m, n, positions):
    parent, rank, count = {}, {}, [0]
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = x
            rank[x] += rank[x] == rank[y]
            count[0] -= 1
    def add((i, j)):
        x = parent[x] = i, j
        rank[x] = 0
        count[0] += 1
        for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if y in parent:
                union(x, y)
        return count[0]
    return map(add, positions)
Too bad Python 2 doesn't have nonlocal yet, hence the somewhat ugly count[0] "hack". Here's a different way:

def numIslands2(self, m, n, positions):
    parent, rank = {}, {}
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return 0
        if rank[x] < rank[y]:
            x, y = y, x
        parent[y] = x
        rank[x] += rank[x] == rank[y]
        return 1
    counts, count = [], 0
    for i, j in positions:
        x = parent[x] = i, j
        rank[x] = 0
        count += 1
        for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if y in parent:
                count -= union(x, y)
        counts.append(count)
    return counts
  
----------------------------------------------------------------
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if positions == None or len(positions) == 0 or 
			m == 0 or n == 0: return 0 # can pass without this standard boundary check
        
        dsu = DSU(m * n)
        res = []
        
        # union an island with its adjacent islands
        for i, j in positions:            
            if dsu.isl[i * n + j] == 0:
                
                # add this island first
                dsu.isl[i * n + j] = 1
                dsu.numIsl += 1
                
                # union 4 adjacent islands if exist
                if i - 1 >= 0 and dsu.isl[(i - 1) * n + j] == 1:
                    dsu.union((i - 1) * n + j, i * n + j)
                if i + 1 < m and dsu.isl[(i + 1) * n + j] == 1:
                    dsu.union(i * n + j, (i + 1) * n + j)
                if j - 1 >= 0 and dsu.isl[i * n + (j - 1)] == 1:
                    dsu.union(i * n + (j - 1), i * n + j)
                if j + 1 < n and dsu.isl[i * n + (j + 1)] == 1:
                    dsu.union(i * n + j, i * n + (j + 1))

            res.append(dsu.numIsl)
        return res    
        
class DSU:
    def __init__(self, num):
        self.par = list(range(num))
        self.rnk = [0] * num
        self.isl = [0] * num
        self.numIsl = 0
        
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
			return
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        self.numIsl -= 1
        
-----------------------------------------------------------------------------
class UnionFind(object):
    def __init__(self, m, n, positions):
        self.n = n
        self.size = [0] * (m * n)
        self.id = [None] * (m * n)
        self.count = 0

    def genIndex(self, i, j):
        return self.n * i + j

    def add(self, i, j):
        index = self.genIndex(i, j)

        self.size[index] = 1
        self.id[index] = index
        self.count += 1

    def find(self, p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        idp, idq = map(self.find, (p, q))
        if idp == idq:
            return

        less, more = (
            (idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))

        self.id[less] = self.id[more]
        self.size[more] += self.size[less]

        self.count -= 1


class Solution(object):
    def numIslands2(self, m, n, positions):
        uf, r = UnionFind(m, n, positions), []

        for i, j in positions:
            uf.add(i, j)
            index = uf.genIndex(i, j)

            neighbors = zip(
                (j > 0, i > 0, j + 1 < n, i + 1 < m),
                (uf.genIndex(x, y) for x, y in ((i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)))
            )

            [uf.union(index, neighbor) for condition, neighbor in neighbors
             if condition and uf.id[neighbor] is not None]

            r.append(uf.count)

        return r
-----------------------------------------------------------------------------------------------------
The intuition here is that I use a Map, with key as one of the coordinates of a single island and values as a Set : all coordinates of that island + all the surrounding neighbors of that island.

For every new position:
Check if it is alread in a neighbor list of some previous island.
IF TRUE:
Merge all those islands, their neighbors, new position and new neighbors into one single entry in the Map
ELSE:
Add it to a Map along with its new neighbors ((0,1),(1,0),(0,-1),(-1,0)).


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        # get surrounding neighbors of position
        def getNeighbors(position):
            all_pos = set()
            all_pos.add(position)
            for neigh in ((0,1),(1,0),(0,-1),(-1,0)):
                a, b = position[0] + neigh[0], position[1] + neigh[1]
                if 0 <= a < m and 0 <= b < n:
                    all_pos.add((a,b))
            return all_pos
        
        # maintain list of islands with key as one of the coordinates of island
        # and values as the other coords along with their neighbors
        islands = {}
        res = []
        for p in positions:
            pos = (p[0],p[1])
            new = set()
            common = []
            
            # get neighbors of the new position
            neighbors = getNeighbors(pos)
            new = new.union(neighbors)
            
            # check if new position is in the neighbor list of previous islands
            for i in islands:
                if pos in islands[i]:
                    common.append(i)
            
            # remove the previous common islands and merge them in a new entry
            if len(common) > 0:
                for c in common:
                    new = new.union(islands.pop(c))
            
            islands[pos] = new
            res.append(len(islands))
        return res

Time: O(k log(mn))
Space: O(mn)
  
-----------------------------------------------------------------------------------------
from collections import defaultdict

class DisjoinSet:
    def __init__(self, size):
        self.size = size
        self.parents = list(range(size))
        self.groups = size
        self.ranks = [0] * size
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def is_joined(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        return roota == rootb
    
    def join(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        
        if roota == rootb:
            return False
        
        if self.ranks[b] > self.ranks[a]:
            a, b = b, a
            roota, rootb = rootb, roota
            
        self.parents[rootb] = roota
        self.groups -= 1
        if self.ranks[b] == self.ranks[a]:
            self.ranks[a] += 1
            
        return True

class Solution:    
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def rcindex(row, col):
            return row * n + col
        djs = DisjoinSet(m*n)
        grid = [[0] * n for i in range(m)]
        island = 0
        
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        islands = []
        for row, col in positions:
            if grid[row][col] == 1:
                islands.append(island)
                continue
            grid[row][col] = 1
            surround = []
            for dr, dc in dirs:
                nr = dr + row
                nc = dc + col
                if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1:
                    surround.append((nr, nc))
            nsurround = len(surround)
            if not nsurround:
                island += 1
            elif nsurround == 1:
                djs.join(rcindex(*surround[0]), rcindex(row, col))
            else:
                for r, c in surround:
                    if djs.join(rcindex(row, col), rcindex(r, c)):
                        island -= 1
                island += 1
            
            islands.append(island)
                    
        return islands
