'''
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.
'''



from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        colors = dict()
        
        for fromnode in range(len(graph)):
            if fromnode in colors:
                continue
            
            queue = deque([fromnode])
            colors[fromnode] = 1
            
            while queue:
                fromnode = queue.popleft()
                
                for tonode  in graph[fromnode]:
                    if tonode in colors:
                        if colors[tonode] == colors[fromnode]:
                            return False
                    else:
                        queue.append(tonode)
                        colors[tonode] = colors[fromnode] * -1
        return True
                
--------------------------------------------------------------------------
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for node_from in range(len(graph)):
            if node_from not in colors and not self.bfs(graph, node_from, colors):
                return False
        return True

    def bfs(self, graph, node, colors):
        queue = deque([node])
        colors[node] = 1
        while queue:
            node_from = queue.popleft()
            for node_to in graph[node_from]:
                if node_to in colors:
                    if colors[node_to] == colors[node_from]:
                        return False
                else:
                    colors[node_to] = colors[node_from] * -1
                    queue.append(node_to)
        return True
--------------------------------------------------------------------------------------------
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colors = {}
        
        for from_node in range(len(graph)):
            if from_node in colors:
                continue

            stack = [from_node]
            colors[from_node] = 1  # 1 is just starting color, could be -1 also

            while stack:
                from_node = stack.pop()

                for to_node in graph[from_node]:
                    if to_node in colors:
                        if colors[to_node] == colors[from_node]:
                            return False
                    else:
                        stack.append(to_node)                        
                        colors[to_node] = colors[from_node] * -1
        return True
