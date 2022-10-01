'''
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
'''


I am using the Floyd-Warshall algorithm to calculate the minimum distance between each pair of cities.
Then all that is left to do is counting the neighbors within the distance threshold and return the city with the minimum count and maximum id.

Time complexity: O(n³)
Space complexity: O(n²)

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Minimum distance graph between all the cities
        minDistance = collections.defaultdict(lambda: collections.defaultdict(lambda: math.inf))
        
        # set the distance from a city to itself to 0
        for i in range(n):
            minDistance[i][i] = 0
            
        # set the initial distances between the cities
        for u, v, weight in edges:
            minDistance[u][v] = weight
            minDistance[v][u] = weight
            
        # Floyd-Warshall calculates the minimum distance between each pair of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    minDistance[i][j] = min(minDistance[i][j], minDistance[i][k] + minDistance[k][j])
        
        minNeighborCount = math.inf
        minCity = -1
        
        for i in range(n):
            # Count how many of city i's neighbors are within the distance threshold.
            neighborCount = sum(minDistance[i][j] <= distanceThreshold for j in range(n) if j != i)
            
            # Update the result if a city with less neighbors has been found or the id is higher
            if neighborCount <= minNeighborCount:
                minNeighborCount = neighborCount
                minCity = i
        
        return minCity
      
-------------------------------------------------------------------------------------------------------------------
import heapq

def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
	adj = build_graph(n, edges)

	min_city, min_reach = None, math.inf
	for node in range(n):
		reach = dijkstra(node, adj, distanceThreshold)
		if reach <= min_reach:
			min_city = node
			min_reach = reach
	return min_city
     

def build_graph(n, edges):
    adj = [[] for _ in range(n)]
    
    for source, dest, weight in edges:
        adj[source].append((dest, weight))
        adj[dest].append((source, weight))
    
    return adj


# return the reachability
def dijkstra(source, adj, distanceThreshold) -> int:
    n = len(adj)
    
    dest = [math.inf] * n
    dest[source] = 0
    
    visited = [0] * n
    
    pq = [(0, source)]
    
    while pq:
        node_dest, node = heapq.heappop(pq)
        visited[node] = 1
        
        for neigh, edge_weight in adj[node]:
            if visited[neigh] == 0:
                new_dest = node_dest + edge_weight
                if new_dest < dest[neigh]:
                    dest[neigh] = new_dest
                    heapq.heappush(pq, (new_dest, neigh))
    
    reach = 0
    for d in dest:
        if d <= distanceThreshold:
            reach += 1
    return reach
