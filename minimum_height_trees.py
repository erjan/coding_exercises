'''
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)
        
        while len(graph) > 2:
            new_leaves = []
            for leaf in leaves:
                nei = graph[leaf].pop()
                del graph[leaf]
                graph[nei].remove(leaf)
                if len(graph[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves
        
        return leaves
