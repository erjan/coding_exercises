'''
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.
'''

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        def tarjan():
            stack = []
            vis = defaultdict(int)
            low = defaultdict(int)
            self.ts = 1
            ret = []
            
            def dfs(node):
                vis[node] = self.ts
                low[node] = self.ts
                self.ts += 1
                stack.append(node)
                
                nex = edges[node]
                if nex != -1:
                    if vis[nex] == 0:
                        dfs(nex)
                        low[node] = min(low[node], low[nex])
                    elif nex in stack:
                        low[node] = min(low[node], low[nex])
                        
                if vis[node] == low[node]:
                    tmp = []
                    while stack[-1] != node:
                        tmp.append(stack.pop())
                    tmp.append(stack.pop())
                    ret.append(tmp)
                        
            for i in range(len(edges)):
                if vis[i] == 0:
                    dfs(i)
            return ret
        
        ret = tarjan()
        cir = max(len(r) for r in ret)
        if cir == 1:
            return -1
        else:
            return cir
-----------------------------------------------------------------------------------------------------------
class Solution:
    def cycle(self, graph, visit, node, mp):
        # print(visit)
        if visit[node] == 2:
            # print(node, self.cnt)
            self.cnt = self.cnt - mp[node]
            return True
        visit[node] = 2
        mp[node] = self.cnt
        for nei in graph[node]:
            if visit[nei] != 1:
                self.cnt += 1
                if self.cycle(graph, visit, nei, mp):
                    return True
        visit[node] = 1
        return False

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        graph = {i: [] for i in range(n)}
        for u, v in enumerate(edges):
            if v != -1:
                graph[u].append(v)

        res = -1
        visit = [0] * n
        for i in range(n):
            if visit[i] == 0:
                self.cnt = 0
                mp = {i: 0 for i in range(n)}
                if self.cycle(graph, visit, i, mp):
                    res = max(res, self.cnt)

        return res
