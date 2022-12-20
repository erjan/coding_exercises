'''
You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.
'''




'''
If there is a odd-length cycle, it is impossible to divide the nodes, which is checked by the DFS part;
If it is possible, then we can enumerate all nodes via BFS to check for the largest number of division along each connected component, which is computed by the BFS part.
'''

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        seen = [0]*n
        group = []
        for i in range(n): 
            if not seen[i]: 
                seen[i] = 1
                stack = [i]
                group.append([i])
                while stack: 
                    u = stack.pop()
                    for v in graph[u]: 
                        if not seen[v]: 
                            seen[v] = seen[u] + 1
                            stack.append(v)
                            group[-1].append(v)
                        elif seen[u] & 1 == seen[v] & 1: return -1

        def bfs(x): 
            """Return the levels starting from x."""
            ans = 0
            seen = {x}
            queue = deque([x])
            while queue: 
                ans += 1
                for _ in range(len(queue)): 
                    u = queue.popleft()
                    for v in graph[u]: 
                        if v not in seen: 
                            seen.add(v)
                            queue.append(v)
            return ans 
                            
        ans = 0 
        for g in group: ans += max(bfs(x) for x in g)
        return ans 
