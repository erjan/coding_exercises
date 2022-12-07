'''
You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

It is directly connected to the top of the grid, or
At least one other brick in its four adjacent cells is stable.
You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.
'''

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
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0]) # dimensions 
        
        seen = set()
        for i, j in hits: 
            if grid[i][j]: 
                seen.add((i, j))
                grid[i][j] = 0
        
        uf = UnionFind(m*n+1)
        for i in range(m): 
            for j in range(n): 
                if i == 0 and grid[i][j]: uf.union(j, m*n)
                if grid[i][j]: 
                    for ii, jj in (i-1, j), (i, j-1): 
                        if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]: uf.union(i*n+j, ii*n+jj)
        
        ans = []
        prev = uf.rank[uf.find(m*n)]
        for i, j in reversed(hits): 
            if (i, j) in seen: 
                grid[i][j] = 1
                if i == 0: uf.union(j, m*n)
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]: uf.union(i*n+j, ii*n+jj)
                rank = uf.rank[uf.find(m*n)]
                ans.append(max(0, rank - prev - 1))
                prev = rank
            else: ans.append(0)
        return ans[::-1]
      
------------------------------------------------------------------------------------------------------------------------
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def dfs(x, y):
            if grid[x][y] != 1: return 0 
            grid[x][y], ans = 2, 1
            for xx, yy in map(lambda pair: (pair[0]+x, pair[1]+y), ((-1, 0), (1, 0), (0, -1), (0, 1))):
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1: ans += dfs(xx, yy)
            return ans                    
        
        def is_stable(x, y):
            grid[x][y] += 1
            if grid[x][y] <= 0: return False
            if (x == 0 and grid[x][y] == 1) or grid[x][y] == 2: return True 
            return any((0 <= xx < m and 0 <= yy < n) and grid[xx][yy] == 2 for xx, yy in map(lambda pair: (pair[0]+x, pair[1]+y), ((-1, 0), (1, 0), (0, -1), (0, 1))))
        
        m, n = len(grid), len(grid[0])
        for x, y in hits: grid[x][y] -= 1
        for j in range(n): dfs(0, j)  
        return [(dfs(x,y) - 1) if is_stable(x, y) else 0 for x, y in hits[::-1]][::-1]  
      
