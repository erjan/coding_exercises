'''
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
'''


#bfs

import math
from collections import deque

class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        # build the graph in hash table
        graph = {i: [[], []] for i in range(n)}  # node: [red edges list], [blue edges list]
        for [i, j] in red_edges:
            graph[i][0].append(j)
        for [i, j] in blue_edges:
            graph[i][1].append(j)

        res = [math.inf for _ in range(n)]  # we will keep min length in this list
        res[0] = 0  # min length for the first node is 0
        min_len = 0  # 

        queue = deque()
        queue.append((0, "r")) 
        queue.append((0, "b")) 

        seen = set() 

        while queue:
            level_size = len(queue)
            min_len += 1

            for _ in range(level_size):
                node, color = queue.popleft()

                if (node, color) not in seen:
                    seen.add((node, color))  # in addition to vertex, we need to have the color too
                                            
                    # add all opposite color children in the queue
                    if color == "r":
                        for child in graph[node][1]:
                            queue.append((child, "b"))
                            res[child] = min(min_len, res[child])  # we reached to a child, so we have to update res[child]
                    if color == "b":
                        for child in graph[node][0]:
                            queue.append((child, "r"))
                            res[child] = min(min_len, res[child]) # we reached to a child, so we have to update res[child]

        for i in range(n):
            if res[i] == math.inf:
                res[i] = -1

        return res
----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        
        # build graph
        adjList = {i:[] for i in range(n)} # {0: [(1, 'r'), 1:[], 2:[1, 'b']}
        for start, end in red_edges:
            adjList[start].append((end, 'r'))
        for start, end in blue_edges:
            adjList[start].append((end, 'b'))
        
        ans = [-1] * n
        ans[0] = 0
        
        # do bfs by increasing level every time
        stack = []
        for nextPtr, color in adjList[0]:
            stack.append((nextPtr, color)) # (position, color)
        
        visited = {(0, 'r'), (0, 'b')} # We start at vertex 0, so we don't want to go back to it.
        level = 0
        while stack:
            level += 1
            nextStack = []
            for node, color in stack:
                if ans[node] == -1:
                    ans[node] = level
                else:
                    ans[node] = min(ans[node], level)
                for nextPtr, nextColor in adjList[node]:
                    if color != nextColor and (nextPtr, nextColor) not in visited:
                        nextStack.append((nextPtr, nextColor))
                        visited.add((nextPtr, nextColor))
            
            stack = nextStack
        
        return ans
      
