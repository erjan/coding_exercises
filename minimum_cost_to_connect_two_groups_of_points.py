'''
You are given two groups of points where the first group has size1 points, the second group has size2 points, and size1 >= size2.

The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost of connecting point i of the first group and point j of the second group. The groups are connected if each point in both groups is connected to one or more points in the opposite group. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.

Return the minimum cost it takes to connect the two groups.
'''


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        mn = [min(x) for x in cost] # min cost of connecting points in 1st group 
        
        @lru_cache(None)
        def fn(j, mask):
            """Return min cost of connecting group1[i:] and group2 represented as mask."""
            if j == n: return sum(mn[i] for i in range(m) if not (mask & (1<<i)))
            return min(cost[i][j] + fn(j+1, mask | 1<<i) for i in range(m))
                
        return fn(0, 0)
      
--------------------------------------------------------------------------------------------------
class Solution:
	def connectTwoGroups(self, cost: List[List[int]]) -> int:        
		n,m=len(cost),len(cost[0])
		mini=[min([cost[i][j] for i in range(n)]) for j in range(m)]

		@cache
		def solve(i,mask2):
			if i==n:
				a=0
				for j in range(m):
					if mask2&(1<<j):
						a+=mini[j]
				return a 
			b=float('inf')
			for j in range(m):
				b=min(b,cost[i][j]+solve(i+1,mask2&~(1<<j)))
			return b
		return solve(0,2**m-1)
