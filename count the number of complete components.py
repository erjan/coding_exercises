'''
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no 
vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.
'''



class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:                       
        adj=defaultdict(list)
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        
        def dfs(i):
            
            component.add(i)
            for child in adj[i]:
                if child not in visited:
                    visited.add(child)
                    dfs(child)
        
        
        ans=0
        visited=set()
        
        for i in range(n):
            if i not in visited:
                component=set()
                visited.add(i)
                dfs(i)
                if all(len(adj[node]) == len(component)-1 for node in component):
                    ans+=1
                    
        
        return ans
-------------------------------------------------------------------------------------------------------------------      


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # 1. build graph
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # 2. util fn to find connected componnet
        def dfs(src):
            visited = set()
            s = [src]
            while s:
                node = s.pop()
                if node not in visited:
                    visited.add(node)
                    for nb in graph[node]:
                        if nb not in visited:
                            s.append(nb)
            return visited
        
        # 3. call dfs to get the connected components
        visited = set()
        
        clusters = []
        for i in range(n):
            if i not in visited:
                c = dfs(i)
                clusters.append(c)
                visited |= c
        
        
        # 4. util fn to check completeness
        def complete(c):
            for i in c:
                for j in c:
                    if j == i:
                        continue
                    if j not in graph[i]:
                        return 0
            return 1
        
        # 5. return
        return sum(complete(c) for c in clusters)
