'''
You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1. You decide to subdivide each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates that there is an edge between nodes ui and vi in the original graph, and cnti is the total number of new nodes that you will subdivide the edge into. Note that cnti == 0 means you will not subdivide the edge.

To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes. The new nodes are x1, x2, ..., xcnti, and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [xcnti-1, xcnti], [xcnti, vi].

In this new graph, you want to know how many nodes are reachable from the node 0, where a node is reachable if the distance is maxMoves or less.

Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.
'''

from collections import defaultdict
from heapq import heappush,heappop

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        visited = [False]*n
        nei = [ [] for _ in range(n)]
        
        for u,v,cnt in edges:
            nei[u].append((v,cnt))
            nei[v].append((u,cnt))
        # edges is converted to list of neighbors of each node
        
        newreached = defaultdict(int)
        # newreached[(u,v)] will be the number of new nodes reachable from u on the way to v
        
        H = [(0,0)] # distance,node
        while H:
            dist,node = heappop(H)
            if visited[node]: 
                continue
            visited[node] = True
            moves = maxMoves-dist
            if moves>0:
                for v,cnt in nei[node]:
                    newreached[(node,v)] = min(cnt,moves)
                    if not visited[v] and moves>=cnt+1:
                        heappush(H,(dist+cnt+1,v))
        S = sum(visited) # reachable original nodes
        for u,v,cnt in edges:
            S += min(cnt,newreached[(u,v)]+newreached[(v,u)])
        return S
