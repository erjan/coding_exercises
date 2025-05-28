'''
There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.
'''

from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_graph(edges):
            n = len(edges) + 1
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def bfs_count_max(graph, max_dist):
            n = len(graph)
            result = [0] * n
            for start in range(n):
                visited = [False] * n
                q = deque()
                q.append((start, 0))
                visited[start] = True
                count = 1
                while q:
                    node, dist = q.popleft()
                    if dist == max_dist:
                        continue
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append((neighbor, dist + 1))
                            count += 1
                result[start] = count
            return result

        g1 = build_graph(edges1)
        g2 = build_graph(edges2)

        if k == 0:
            return [1] * len(g1)

        cnt1 = bfs_count_max(g1, k)
        cnt2 = bfs_count_max(g2, k - 1)
        max_cnt2 = max(cnt2)

        return [cnt + max_cnt2 for cnt in cnt1]
