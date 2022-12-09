'''
There is an undirected graph with n nodes numbered from 0 to n - 1 (inclusive). You are given a 0-indexed integer array values where values[i] is the value of the ith node. You are also given a 0-indexed 2D integer array edges, where each edges[j] = [uj, vj, timej] indicates that there is an undirected edge between the nodes uj and vj, and it takes timej seconds to travel between the two nodes. Finally, you are given an integer maxTime.

A valid path in the graph is any path that starts at node 0, ends at node 0, and takes at most maxTime seconds to complete. You may visit the same node multiple times. The quality of a valid path is the sum of the values of the unique nodes visited in the path (each node's value is added at most once to the sum).

Return the maximum quality of a valid path.

Note: There are at most four edges connected to each node.


Start dfs at 0th node
If time taken by dfs path exceeds max limit then stop exploring (base condition)
If you have traversed back to 0th node update the result as max(result, pathValue) where pathValue is total of all values of node
Keep exploring further path with new set of visited nodes. Each set is exclusive for the path traversed.
'''

class Solution:
    def dfs(self, node, visited, pathValue, pathTime):
        if pathTime > self.maxTime:
            return
        if node == 0:
            self.result = max(self.result, pathValue)
        for childNode, childTime in self.adjList[node]:
            newVisited = {_ for _ in visited}
            newPathValue = pathValue
            if childNode not in newVisited:
                newPathValue = pathValue + self.values[childNode]
                newVisited.add(childNode)
            self.dfs(childNode, newVisited, newPathValue, pathTime + childTime)

    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        self.adjList = {i:set() for i in range(len(values))}
        self.maxTime = maxTime
        self.values = values
        self.result = values[0]
        for source, dest, time in edges:
            self.adjList[source].add((dest, time))
            self.adjList[dest].add((source, time))
        visited = set()
        visited.add(0)
        self.dfs(0, visited, values[0], 0)
        return self.result
        
        
-----------------------------------------------------------------------------------------------------------------
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        for outgoing, incoming, distance in edges:
            graph[outgoing].append((incoming, distance))
            graph[incoming].append((outgoing, distance))
        # At each node, we have at most four possible moves
        # dp[loc][maxTime] = max(*[dp[adj][maxTime - dist(adj)] for adj in adjs], value[loc])

        # as many unique nodes as possible..
        # able to return to start
        # maximize value

        # compute shortest path from all nodes to 0
        # dijktra
        distance_to_origin = defaultdict(lambda: inf)
        distance_to_origin[0] = 0
        visited = set()
        to_visit = [(0, 0)]
        while len(to_visit) > 0:
            dist, cur = heappop(to_visit)
            if cur in visited or dist != distance_to_origin[cur]:
                continue
            for neighbor, distance in graph[cur]:
                if distance_to_origin[cur] + distance < distance_to_origin[neighbor]:
                    distance_to_origin[neighbor] = distance_to_origin[cur] + distance
                    heappush(to_visit, (distance_to_origin[neighbor], neighbor))
            visited.add(cur)

        #  start from 0, reach out (how to determine returnability?)
        # with the shortest path map, we can prune branches that cannot return to the start
        d = deque([(0, maxTime, set(), 0)])
        best = values[0]
        while len(d) > 0:
            for _ in range(len(d)):
                cur, time, unique, val = d.popleft()
                if cur == 0:
                    best = max(best, val)
                if distance_to_origin[cur] > time:
                    # no way home
                    continue
                for to, distance in graph[cur]:
                    if distance > time:
                        continue
                    new_val = values[to] + val if to not in unique else val
                    # Conditionally copy the unique set
                    new_unique = set(unique) | set([to]) if to not in unique else unique
                    d.append((to, time - distance, new_unique, new_val))
        return best
