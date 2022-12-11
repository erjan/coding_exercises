'''
You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.

You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.

Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.

Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.

A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.
'''

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        forward, backward = dict(), dict()
        for start, end, weight in edges:
            if start in forward:
                if end in forward[start]:
                    forward[start][end] = min(weight, forward[start][end])
                else:
                    forward[start][end] = weight
            else:
                forward[start] = {end: weight}
            if end in backward:
                if start in backward[end]:
                    backward[end][start] = min(weight, backward[end][start])
                else:
                    backward[end][start] = weight
            else:
                backward[end] = {start: weight}

        def travel(origin: int, relations: dict, costs: list) -> None:
            level = {origin}
            costs[origin] = 0
            while level:
                new_level = set()
                for node in level:
                    if node in relations:
                        for next_node, w in relations[node].items():
                            if w + costs[node] < costs[next_node]:
                                new_level.add(next_node)
                                costs[next_node] = w + costs[node]
                level = new_level

        from_src1 = [inf] * n
        from_src2 = [inf] * n
        from_dest = [inf] * n

        travel(src1, forward, from_src1)
        travel(src2, forward, from_src2)
        travel(dest, backward, from_dest)

        combined_cost = min(sum(tpl)
                            for tpl in zip(from_src1, from_src2, from_dest))

        return combined_cost if combined_cost < inf else -1
      
-------------------------------------------------------------------------------

import heapq

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [[] for _ in range(num)]
        self.dist = [float('inf')] * num

    def add_edge(self, a, b, weight):
        self.graph[a].append((b, weight))

    def dijkstra(self, source):
        self.dist[source] = 0
        heap = [(self.dist[i], i) for i in range(self.V)]
        heapq.heapify(heap)
        while heap:
            cur_dist, u = heapq.heappop(heap)
            for ad, weight in self.graph[u]:
                new_dist = cur_dist + weight
                if new_dist < self.dist[ad]:
                    self.dist[ad] = new_dist
                    heapq.heappush(heap, (new_dist, ad))

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        g1, g2, g3 = Graph(n), Graph(n), Graph(n)
        minimum_dist_map = dict()
        for node_from, node_to, weight in edges:
            if (node_from, node_to) in minimum_dist_map:
                minimum_dist_map[(node_from, node_to)] = min(minimum_dist_map[(node_from, node_to)], weight)
            else:
                minimum_dist_map[(node_from, node_to)] = weight
        
        for (node_from, node_to), weight in minimum_dist_map.items():
            g1.add_edge(node_from, node_to, weight)
            g2.add_edge(node_from, node_to, weight)
            g3.add_edge(node_to, node_from, weight)
        
        g1.dijkstra(src1); g2.dijkstra(src2); g3.dijkstra(dest);
        
        res = min(g1.dist[mid] + g2.dist[mid] + g3.dist[mid] for mid in range(n))
        res = min(res, g1.dist[dest] + g2.dist[dest])
        
        return res if res != float('inf') else -1
