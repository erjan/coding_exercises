'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        def find(x: int) -> int:
            if x != par[x]: par[x] = find(par[x])
            return par[x]
        def union(x: int, y: int) -> None:
            par[find(y)] = find(x)
        for a,b in edges:
            if find(a) == find(b): return [a,b]
            else: union(a,b)
              
---------------------------------------------------------------------------------------
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(u,v):
            if u in visited:
                return False
            if u == v:
                return True
            
            visited.add(u)
            
            for i in graph[u]:
                if dfs(i, v):
                    return True
            return False
        
        
        n = len(edges)
        graph = defaultdict(list)
        
        
        ans = []
        for u, v in edges:
            visited = set()
            if dfs(u, v):
                ans = [u,v]
            graph[u].append(v)
            graph[v].append(u)
        return ans
