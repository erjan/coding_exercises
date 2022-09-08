'''
There are n servers numbered from 0 to n - 1 connected by undirected 
server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection
between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.
'''


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edgeMap = defaultdict(list)
        for a,b in connections:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        disc, low, time, ans = [0] * n, [0] * n, [1], []
        def dfs(curr: int, prev: int):
            disc[curr] = low[curr] = time[0]
            time[0] += 1
            for next in edgeMap[curr]:
                if not disc[next]:
                    dfs(next, curr)
                    low[curr] = min(low[curr], low[next])
                elif next != prev:
                    low[curr] = min(low[curr], disc[next])
                if low[next] > disc[curr]:
                    ans.append([curr, next])
        dfs(0, -1)
        return ans
