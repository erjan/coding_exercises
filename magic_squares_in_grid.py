'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).
'''

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        squares = [
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        ]
        
        ans = 0
        
        for x, y, z in itertools.product(range(len(grid[0]) - 2), range(len(grid) - 2), range(8)):
            for dx, dy in itertools.product(range(3), range(3)):
                if grid[y+dy][x+dx] != squares[z][dy][dx]:
                    break
            else:
                ans += 1
        
        return ans
      
---------------------------------------------------------
class Solution:
    def numMagicSquaresInside(self, G: List[List[int]]) -> int:
    	M, N, S, t, s = len(G), len(G[0]), set(range(1,10)), range(3), 0
    	for i in range(M-2):
    		for j in range(N-2):
    			g = [G[i+k][j:j+3] for k in t]
    			if set(sum(g,[])) != S or g[1][1] != 5: continue
    			if any(sum(g[k]) != 15 for k in t) or any(sum([g[k][l] for k in t]) != 15 for l in t): continue
    			if sum([g[k][k] for k in t]) != 15 or sum([g[k][2-k] for k in t]) != 15: continue
    			s += 1
    	return s
