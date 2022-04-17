You are given a 0-indexed binary matrix grid. In one operation, you can flip any 1 in grid to be 0.

A binary matrix is well-isolated if there is no 1 in the matrix that is 4-directionally connected (i.e., horizontal and vertical) to another 1.

Return the minimum number of operations to make grid well-isolated.



Treat all 1's as a bipartite graph, those with ( row % 2 ) == ( col % 2 ) are in one party, and those with ( row % 2) != ( col % 2) are in the other party, like this:

1 0 1
0 1 0
1 0 1

vs.

0 1 0
1 0 1
0 1 0

Find the maximum matching in this graph, which equals the mininum numbers of 1 to be removed to separate those two parties.
Implmentation of Hungarian Algorithm below. Time complexity upper bound O(N^3) with N as the total number of 1 in the grid.

It took me a while to understand the Hungarian Algorithm (or actually Kuhn's Algorithm ?? ) after learning Max Flow Algorithms since the thought process is quite different.
I recommend reading Yasen Hu's blog in this link: https://yasenh.github.io/post/hungarian-algorithm-1/

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        matching = defaultdict(lambda: None)
        
		
		# dfs to find any alternating path from (r, c) between the two parties
		# alternating path means included edges are "matching - unmatching - matching" or "unmatching - matching - unmatching".
		# if one alternating path is found, the max matching can be increased by 1.
        def dfs(r, c, visited):
            visited.add((r, c))
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if not (0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1) or (nr, nc) in visited: continue
                
				# this step is not in typical dfs but required here, otherwise it will get TLE
				# this is because if (nr, nc) node is already in a matching, we need to skip this node to start dfs again from its matching node, instead of starting dfs from (nr, nc) directly.
                visited.add((nr, nc))
                
				# if (nr, nc) is already in a matching, start dfs from its matching node (let's call it Bob)
				# this is to check if Bob can form another matching and give up the current matching with (nr, nc), so (r, c) can match with (nr, nc) 
                if not matching[nr, nc] or dfs(*matching[nr, nc], visited):
                    matching[r, c] = (nr, nc)
                    matching[nr, nc] = (r, c)
                    return True
            return False
        
        max_matching = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0: continue
                if (r % 2) == (c % 2) and dfs(r, c, set()):       # only need to start dfs from cells in one party
                    max_matching += 1
        
        return max_matching
                                                          
-------------------------------------------------------------------------------------
                                                          class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        seen = [[0] * len(grid[0]) for _ in range(len(grid))] 
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and seen[i][j] == 0:
                    option1 = self.dfs(i, j, 0, seen, grid, 1)
                    option2 = self.dfs(i, j, 1, seen, grid, 2)
                    res += min(option1, option2)
        
        return res
    
    def dfs(self, i, j, curr_color, seen, grid, marker):
        if not self.is_valid(i, j, grid) or grid[i][j] == 0 or seen[i][j] == marker:
            return 0
        
        seen[i][j] = marker
        res = 0 if grid[i][j] == curr_color else 1
        next_color = 1 - curr_color
        for x, y in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
            res += self.dfs(x, y, next_color, seen, grid, marker)
        
        return res
        
    def is_valid(self, i, j, grid):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])
