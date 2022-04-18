'''
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
'''



Solution 1

Collect everybody's x-coordinate in order, then sum the distances to the median. Do it for the original grid and for the diagonally flipped one.

def minTotalDistance(self, grid):
    total = 0
    for grid in grid, zip(*grid):
        X = []
        for x, row in enumerate(grid):
            X += [x] * sum(row)
        total += sum(abs(x - X[len(X)/2])
                     for x in X)
    return total
Solution 2

Same thing, just written with generator expressions and a list comprehension.

def minTotalDistance(self, grid):
    return sum(sum(abs(x - X[len(X)/2]) for x in X) for X in
               ([x for x, row in enumerate(grid) for _ in range(sum(row))]
                for grid in (grid, zip(*grid))))
  
  
  ---------------------------------------------------------------------------------------------------
  def minTotalDistance(self, grid):
    if not grid:
        return 0
    r, c = len(grid), len(grid[0])
    sumr = [i for i in xrange(r) for j in xrange(c) if grid[i][j]]
    sumc = [j for i in xrange(r) for j in xrange(c) if grid[i][j]]
    sumr.sort()
    sumc.sort()
    mid_row = sumr[len(sumr)/2]
    mid_col = sumc[len(sumc)/2]
    return sum([abs(r-mid_row) for r in sumr]) + sum([abs(c-mid_col) for c in sumc])
  
----------------------------------------------------------------------------------------------------------------------------
def minTotalDistance(self, grid):
    x = sorted([i for i, row in enumerate(grid) for v in row if v == 1])
    y = sorted([j for row in grid for j, v in enumerate(row) if v == 1])
    return sum([abs(x[len(x)/2]-i)+abs(y[len(y)/2]-j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == 1])
  
  
-----------------------------------------------------------------------------------------------
def minTotalDistance(self, grid: List[List[int]]) -> int:

	def manhattan(a,b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1])

	# 1. Make a list of all the houses
	houses = []
	R, C = len(grid), len(grid[0])
	for r in range(R):
		for c in range(C):
			if grid[r][c]:
				houses.append((r,c))

	# 2. Start in the middle of the grid and calculate the distance to all houses from this point
	#    The distance to all houses from a point is (cost)
	r, c = (R//2, C//2)
	cost = sum(manhattan(h, (r,c)) for h in houses)
	visited = set([(r,c)])

	prev = -1
	while cost != prev:

		prev = cost

		# 3. Check if any neighbor has a lower cost than the current location
		for (i,j) in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
			if (0 <= i < R) and (0 <= j < C) and ((i,j) not in visited):
				visited.add((i,j))
				next_cost = sum(manhattan(h, (i,j)) for h in houses)
				if next_cost < cost:
					r, c = i, j
					cost = next_cost
					break

	return cost
For those who like to know the intuition behind each solution, here are my notes leading up to this approach:

	# Inuition:
	#
	# Let's call our loss function the sum of the manhattan distance to every house
	#
	# Then let's assume that the loss function is convex in shape meaning that
	# if we greedily choose the next location to check based on whether or not
	# it has a lower cost than the current location we will eventually stumble into
	# a global minimum.  
	#
	# Once we find a local minima (all surrounding points have a higher cost) we
	# treat it as the global minima since the loss function is assumed to be convex, 
	# and return this location
  
--------------------------------------------------------------------

Similar to other DP approaches. The basic idea is to treat it as optimization of two 1-D problem. Here is the skeleton of the algorithm

iterate the grid and find the number of homes at given x (column) and y (row) respectively
For each 1-D problem (e.g., x direction), the distance of meeting point at x is given by
d(x) = d(x-1) + N(x-1) - (N - P(x-1))
where
N(x): # of homes <= x
N: total # of homes
You can simply iterate along the 1-D array once to compute both N and d, and minimum distance can be obtained during the process. In fact, there is no need to keep an array for N[] or d[].
class Solution:
    def minDistance1D(self, numOfHomesAt, N):
        n = len(numOfHomesAt)
        prev_N, prev_d = numOfHomesAt[0], 0
        d0 = 0
        minDistance = 0
        for i in range(1, n):
            d0 += i * numOfHomesAt[i]
            prev_d = prev_d + prev_N * 2 - N
            prev_N += numOfHomesAt[i]
            minDistance = min(minDistance, prev_d)
        return d0 + minDistance
    
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        N_x = [0] * n
        N_y = [0] * m
        N = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    N_x[col] += 1
                    N_y[row] += 1
                    N += 1
        
        return self.minDistance1D(N_x, N) + self.minDistance1D(N_y, N)
