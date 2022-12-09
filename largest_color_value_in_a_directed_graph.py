'''
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
'''

from collections import defaultdict

class Solution:
    def ts(self, colors, edges):
        N = len(colors)
        indegree = [0]*N
        graph = defaultdict(list)
        dp = [defaultdict(int) for _ in range(N)]
        lindex = {}
        S = []
        V = {}    

		# edge case - no edges in input at all,
        if not edges and colors:
            return 1
        
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        for idx, value in enumerate(letters):
            lindex[value] = idx

        for s, e in edges:
		    # if there is a loop to same number, return error right away. 
            if s == e:
                return -1
            graph[e].append(s)  
            indegree[s] += 1
            
        for a in range(N):
            if indegree[a] == 0:
                ld = [0 for _ in range(27)]
                ld[lindex[colors[a]]] = 1
                dp[a][lindex[colors[a]]] = 1
                S.append(a)
                V[a] = True
				
        ans = -1
                
        while S:
            node = S.pop()
            V[node] = True

            for nei in graph[node]:
                if nei not in V:
                    indegree[nei] -= 1 

                    letter_index = lindex[colors[nei]]
					
					## copy all the attributes to the new nodes, but only copy max values. 
                    for n in dp[node]:
                        dp[nei][n] = max(dp[nei][n], dp[node][n] if n != letter_index else dp[node][n]+1)
                        ans = max(dp[nei][n], ans)

                    if not dp[nei][letter_index]:
                        dp[nei][letter_index] = 1

                    if not indegree[nei]:
                        S.append(nei)
                else:
                    return -1

        return ans if len(V) == len(colors) else -1
    
    def largestPathValue(self, colors: str, edges) -> int:
        return self.ts(colors, edges)
      
------------------------------------------------------------------------------------------------------------------
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for v1, v2 in edges:
            d[v1].append(v2)
        visited = {}
        counts = [[0] * 26 for _ in range(len(colors))]
        stack = []
        global_max = 0
        for root in d.keys():
            if root in visited:
                continue
            stack.append(root)
            while stack:
                v1 = stack[-1]
                if v1 in visited:
                    if visited[v1] == 1:
                        visited[v1] = 2
                        stack.pop()
                        if v1 in d:
                            for v2 in d[v1]:
                                for c in range(26):
                                    counts[v1][c] = max(counts[v1][c], counts[v2][c])
                        counts[v1][ord(colors[v1])-ord('a')] += 1
                else:
                    visited[v1] = 1
                    if v1 in d:
                        for v2 in d[v1]:
                            if v2 in visited:
                                if visited[v2] == 1:
                                    return -1
                            else:
                                stack.append(v2)
            global_max = max(global_max, max(counts[root]))
        if global_max == 0 and len(d) < len(colors): # in case input is like ("abcde", [])
            global_max = 1
        return global_max
