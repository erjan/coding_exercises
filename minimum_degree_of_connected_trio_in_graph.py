'''
You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.

A connected trio is a set of three nodes where there is an edge between every pair of them.

The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.

Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.
'''

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        result = n ** 2 # placeholder value
        adj = [set() for _ in range(n + 1)]
        visited = set()
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        for first in range(1, n + 1): # iterate through every node
            for second in adj[first]: # iterate through every neighbor of the first node
                e1 = tuple(sorted((first, second)))
                if e1 in visited:
                    continue
                visited.add(e1) # mark e1 (first -> second) as visited because we don't want to visit (second -> first) again
                for third in adj[second]:
                    if third == first: # skip if the third node is the first node (we need the first node to be its neighbor rather than itself!)
                        continue
                    e2 = tuple(sorted((first, third)))
                    if first in adj[third]: # we don't check if e2 is in visited because the third node is not the current node being explored
                        visited.add(e2) # we need to mark e2 as visited because one end of e2 is the first node and if we have checked (third -> first), we don't need to check (first -> third) again
                        degree = len(adj[first]) - 2 + len(adj[second]) - 2 + len(adj[third]) - 2
                        result = min(result, degree)
        return -1 if result == n ** 2 else result
      
------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # make everython 0-indexed
        edges = [(a-1, b-1) for a, b in edges]
        
        
        # maintain two graphs, one for fast querying and another for
        # quickly finding node with least edges
        graph = defaultdict(set)
        graph_list = defaultdict(list)
        
        for a, b in edges:
            graph_list[a].append(b)
            graph_list[b].append(a)
            graph[a].add(b)
            graph[b].add(a)

        for k, v in graph_list.items():
            # sort graph_list on basis of total_edges
            v.sort(key=lambda x: len(graph_list[x]))
            
            
        min_degree = math.inf   
        
        for a, b in edges:
            for i in graph_list[a]:
                if i == b:
                    continue
                if i in graph[b]:
                    degree = len(graph[a]) - 2
                    degree += len(graph[b]) - 2
                    degree += len(graph[i]) - 2
                    min_degree = min(min_degree, degree)
                
                    if min_degree == 0:
                        return 0
                    # we can stop because graph_list is sorted and other options will have more edges than this one.
                    break 
                    
        if min_degree == math.inf:
            return -1
        
        return min_degree
