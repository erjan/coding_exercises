'''
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
'''

class Solution:
		def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
			if roads == []: #egde case check
				return 0

			#create adjacency matrix  to check if edge present or not in O(1) time
			adj=[[0]*(n) for i in range(n)]
			for i in roads:
				adj[i[0]][i[1]] = 1
				adj[i[1]][i[0]] = 1

			node_degrees = defaultdict(int)
			for i in roads:
				node_degrees[i[0]]+=1
				node_degrees[i[1]]+=1

			maxx1, maxx2 = 0, 0
			ans = 0
			for i, k in node_degrees.items():                #O(N)
				if k >= maxx1:
					maxx1 = k
					maxx2 = 0
					for j, l in node_degrees.items():                #O(N)
						if l >= maxx2 and j!=i:
							maxx2 = l
							if adj[i][j] == 1 or adj[j][i] == 1:                #O(1)
								ans = max(ans, maxx1 + maxx2 - 1)
							else:
								ans = max(ans, maxx1 + maxx2 )
			return ans
--------------------------------------------------------------------------------
from collections import defaultdict
from itertools import combinations

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        # Variables
        rank = 0
        indegree = defaultdict(lambda: set())
        nodes = [i for i in range(n)]
        
        # Update indegree hashmap
        for x,y in roads:
            indegree[x].add(y)
            indegree[y].add(x)
            
        # Try every pair of different cities and calculate its network rank.
        # The network rank of two vertices is sum of their degrees discarding the common edge.
        # For all combinations of nodes check network rank.
        # If two nodes are connected then consider the edge between them only once,
        # that is add -1 to sum of their indegrees else add 0.
        for x,y in combinations(nodes, 2):
            rank = max(rank, len(indegree[x]) + len(indegree[y])
                       # check if there is a road connecting two different cities
                       - (1 if (([x,y] in roads) or ([y,x] in roads)) else 0))
            
        return rank
      -----------    
