'''
Given an m x n integer matrix grid where each entry is only 0 or 1, return the number of corner rectangles.

A corner rectangle is four distinct 1's on the grid that forms an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1's used must be distinct.

 
 '''

Algorithm:
For a given row i, loop through rows i+1 to m-1 to find matching column pairs. Here, I convert grid to list of sets representation in which each set contains the columns for a given row whose value is 1.

Implementation (692ms, 91.19%):

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid = [{i for i in range(n) if row[i]} for row in grid] #list of sets representation
        
        ans = 0
        for i in range(m):
            for j in range(i+1, m):
                ans += (lambda n: n*(n-1)//2)(len(grid[i] & grid[j]))
        return ans 
Analysis:
Time complexity O(M^2 N)
Space complexity O(MN) (for the list of sets representation)

Edited on 1/29/2021

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) # dimensions 
        ans = 0
		seen = {}
        for i in range(m):
            for j in range(n): 
                if grid[i][j]: 
                    for jj in range(j): 
                        if grid[i][jj]: 
                            ans += seen.get((jj, j), 0)
                            seen[jj, j] = 1 + seen.get((jj, j), 0)
        return ans 
      
      
      -------------------------------------------------------------------------
      
      We iterate over each row and count the number of lines starting in position i and ending in j.
If the number of lines between any two coordinates is more than 1 then we can form a rectange (think about it).
To be specific, if the number of lines is v we can form v * (v-1) / 2 number of rectangles (math).

def countCornerRectangles(self, grid: List[List[int]]) -> int:
	hlines = Counter() # number of horizontal lines between i and j coordinates of a row
	for row in grid:
		ones = [i for i, v in enumerate(row) if v]
		pairs = [(ones[i], ones[j]) for i in range(len(ones)-1) for j in range(i+1, len(ones))]
		hlines.update(pairs)
	return sum(v * (v-1) // 2 for v in hlines.values())
---------------------------------------------------------------

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        ans = 0
        d = defaultdict(int)
        for i in range(len(grid)):
            for a, b in itertools.combinations([j for j in range(len(grid[0])) if grid[i][j]], 2):
                ans += d[a, b]
                d[a, b] += 1
        return ans 
---------------------------------------------------------------

In the original Approach #1, in each row, corners are searched by brutal search, incuring O(R*C^2).
My solution is iterate each row to find 1, if the candidates are less than 2, the row could not contribute to any rectangle.
Using itertools.combinations to test the combinations, so the complexity is O(R*C).

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        if h == 1 or w == 1:
            return 0
        
        res = 0
        cnt = defaultdict(int)
        for y in range(h):
            cands = [x for x in range(w) if grid[y][x] == 1]
            length = len(cands)
            if length < 2:
                continue
            for x1, x2 in itertools.combinations(cands, 2):
                res += cnt[(x1, x2)]
                cnt[(x1, x2)] += 1
        
        return res
      
      
      
