'''
You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.
 
'''


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ## RC ##
        ## APPROACH: UNDIRECTED GRAPH ##
        graph = collections.defaultdict(list)
        for u,v,w in roads:
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        res = float('inf')
        def dfs(node):
            nonlocal res
            if node in cache:
                return
            for v, w in graph[node]:
                if v == node:
                    continue
                res = min(res, w)
                cache[node] = res
                dfs(v)
            
        cache = collections.defaultdict(int)
        dfs(1)
        return res
      
------------------------------------------------------------------------------------------------
from typing import list
from collections import deque, defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        # Creating of Weighted Graph
        graph = defaultdict(list)
        weights = defaultdict()
        
        for u, v, i in roads:
            graph[u].append(v)
            graph[v].append(u)
            
            weights[(u,v)] = i
            weights[(v,u)] = i
            
        # Score will keep track of each score to the node
        score = [float("inf") for i in range (n+1)]
        queue = deque([(1,float("inf"))])
        
        
        while queue:
            node, distance = queue.popleft()
            
            for children in graph[node]:
                
                w1 = weights[(node,children)]
                w2 = score[children]

                if w1 < w2:
                    queue.append([children, w1])

                score[children] = min(w1, w2)
                    
        return(min(score))
