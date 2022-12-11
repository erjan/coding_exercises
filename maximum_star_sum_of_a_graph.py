'''
There is an undirected graph consisting of n nodes numbered from 0 to n - 1. You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.

You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. In other words, it is a subset of edges of the given graph such that there exists a common node for all edges.

The image below shows star graphs with 3 and 4 neighbors respectively, centered at the blue node.
'''


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        ans = -math.inf
        n = len(vals)
        for a,b in edges:
            if len(graph[a]) == k and k > 0:
                val = heappop(graph[a])
                heappush(graph[a],max(val,vals[b]))
            else:
                if vals[b] > 0:
                    heappush(graph[a],vals[b])
            if len(graph[b]) == k and k > 0:
                val = heappop(graph[b])
                heappush(graph[b],max(val,vals[a]))
            else:
                if vals[a] > 0:
                    heappush(graph[b],vals[a])
        for i in range(n):
            ans = max(ans,vals[i] + sum(graph[i]))
        return ans
        
---------------------------------------------------------------------------------------------
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
        graph = defaultdict(list)
        
        for src,dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            
        #traverse each node and find value of edges and pick the highest two 
        maxi = float('-inf')
        if not edges:
            return max(vals)
        for node in graph:
            temp = []
            for val in graph[node]:
                heapq.heappush(temp, vals[val])
                while len(temp) > k:
                    heapq.heappop(temp)
            
            tot = vals[node]
            for i in range(len(temp)):
                tot = max(tot, tot+ temp[i])
                maxi = max(maxi,tot)
        return maxi    
--------------------------------------------------------------------------------------------------------------
class Solution:
    def make_graph(self, edges):
        g = defaultdict(set)
        for f,t in edges:
            g[f].add(t)
            g[t].add(f)
        return g

    def get_k_nodes_best(self, g, curr_node, vals, k):
        k_nodes = sorted([vals[to] for to in g[curr_node]])[-k:]
        best = vals[curr_node]
        for val in k_nodes: best = max(best, best + val)
        return best        

    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        g = self.make_graph(edges)
        if k == 0 or not g: return max(vals)
        return max(self.get_k_nodes_best(g, node, vals, k) for node in g)
                
        
          
