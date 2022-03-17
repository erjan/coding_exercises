'''
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
'''

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        for n1 in edges[0]:
            c = 0
            for i in range(len(edges)):

                edge = edges[i]

                if edge[0] == n1 or edge[1] == n1:
                    c += 1
            if c == len(edges):
                return n1
        
