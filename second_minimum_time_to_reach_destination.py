'''
A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the minimum value.

For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:

You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.
 
 '''

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        G = defaultdict(set)
        
        for x,y in edges:
            G[x].add(y)
            G[y].add(x)
        
        T1, T2 = [math.inf] * n, [math.inf] * n
        
        Q = [(0,1)]
        while Q:
            t, i = heappop(Q) 
            if T1[i-1] >= t: T1[i-1] = t
            elif T2[i-1] >= t:
                if i==n: return t
                T2[i-1] = t
                
            q,r = divmod(t, change)
            if q%2==0: lag = 0
            else: lag = change-r
            
            for j in G[i]:
                if t+time+lag<min(T2[j-1],T2[-1]) and t+time+lag != T1[j-1]:
                    if T1[j-1] >= t+time+lag:
                        T1[j-1] = t+time+lag
                    elif T2[j-1] >= t+time+lag:
                        T2[j-1] = t+time+lag                    
                    heappush(Q,(t+time+lag,j))
                    
------------------------------------------------------------------------------------------------------------
Dijkstra's algo is an overkill for this problem as the weights on edges are identical per the one time variable. BFS is enough for this problem.

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        least = None
        queue = deque([(0, 0)])
        seen = [[] for _ in range(n)]
        while queue: 
            t, u = queue.popleft()
            if u == n-1: 
                if least is None: least = t
                elif least < t: return t 
            if (t//change) & 1: t = (t//change+1)*change # waiting for green
            t += time
            for v in graph[u]: 
                if not seen[v] or len(seen[v]) == 1 and seen[v][0] != t: 
                    seen[v].append(t)
                    queue.append((t, v))
