You are given a positive integer n representing the number of nodes in a connected undirected graph containing exactly one cycle. The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [node1i, node2i] denotes that there is a bidirectional edge connecting node1i and node2i in the graph.

The distance between two nodes a and b is defined to be the minimum number of edges that are needed to go from a to b.

Return an integer array answer of size n, where answer[i] is the minimum distance between the ith node and any node in the cycle.



class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        
        # step 1: backtracking DFS to find the cycle
        circle = []
        vis = set()
        
        def find_circle(node, par):
            if node in vis:
                return (True, node)
            for nei in g[node]:
                if nei == par: continue
                vis.add(node)
                circle.append(node)
                status, res = find_circle(nei, node)
                if status: return status, res
                circle.pop()
                vis.remove(node)

            return False, None

        
        _, node = find_circle(0, None)
        # get the circle from start "node"
        circle = circle[circle.index(node):] 

        # step 2: BFS to get rest of the nodes from each node in the cycle
        ans = [0] * n        
        vis = set(circle)

        steps = 0
        while circle:
            new_q = []
            steps += 1
            for x in circle:
                for nei in g[x]:
                    if nei in vis: continue
                    ans[nei] = steps
                    vis.add(nei)
                    new_q.append(nei)
            circle = new_q
        return ans     
      
----------------------------------------------------------------
This algorithm consists of two parts:

Find nodes in cycle with topological sorting
Find distances from the nodes in cycle using BFS
We can use topological sorting to find nodes that are not in cycle. Based on this information, we know the other nodes are in cycle for sure.

Then we can use BFS to measure the distance from the nodes that are in cycle.

class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
		# part 0, build graph
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[u] += 1
            graph[v].append(u)
            indegree[v] += 1
		# part 1 topological sorting
        stack = [node for node in range(n) if indegree[node] == 1]
        out_of_cycle = set()
        while stack:
            node = stack.pop()
            out_of_cycle.add(node)
            for neighbour in graph[node]:
                if neighbour not in out_of_cycle:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 1:
                        stack.append(neighbour)
		# part 2 bfs
        from collections import deque
        queue = deque(node for node in range(n) if node not in out_of_cycle)
        ans = [0] * n
        steps = 0
        visited = set(queue)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                ans[node] = steps
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            steps += 1
        return ans
