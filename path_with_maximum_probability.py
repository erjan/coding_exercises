'''
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
'''

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)
        # Make adjacency List in the form {A : [B, W]}
        # Here adjacency list represents a map that represents and edge from A to B with W weight 
        for edge,probablity in zip(edges, succProb):
            a, b = edge[0], edge[1]
            # -1 multiplied as we would be using a min-heap functioning as a max-heap since we are required to return the max-probabilty
            adj[a].append((b,-1*probablity))
            adj[b].append((a,-1*probablity))    
            
        # Use of a min-Heap for Dijkstra's Algorithm    
        heap = [(-1,start)]
        visited = {}
        while heap:
            prob,node = heapq.heappop(heap)
            visited[node] = prob
            if node == end: #Return Probability when we reach the destination Node
                return -1 * prob
            for nei,weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (-1*prob*weight,nei))
        # Return Zero when we were never able to reach the destination node            
        return 0
-------------------------------------------------------      
import heapq as hq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj_list = {i: [] for i in range(0, n)}
        
        for e, w in zip(edges, succProb):
            v1, v2 = e
            adj_list[v1].append((w, v2))
            adj_list[v2].append((w, v1))
        
        max_heap = [(-1, start)]
        seen = set()

        
        while max_heap:
            weight, v = hq.heappop(max_heap)            
            
            if v in seen: continue
            if v == end: return -weight
            
            seen.add(v)
            
            for neighbor_weight, neighbor in adj_list[v]:
                if neighbor not in seen:
                    hq.heappush(max_heap, (weight * neighbor_weight, neighbor))
        
        return 0.0
