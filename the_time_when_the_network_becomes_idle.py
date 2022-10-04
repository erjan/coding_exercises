'''
There is a network of n servers, labeled from 0 to n - 1. You are given a 2D integer array edges, where edges[i] = [ui, vi] indicates there is a message channel between servers ui and vi, and they can pass any number of messages to each other directly in one second. You are also given a 0-indexed integer array patience of length n.

All servers are connected, i.e., a message can be passed from one server to any other server(s) directly or indirectly through the message channels.

The server labeled 0 is the master server. The rest are data servers. Each data server needs to send its message to the master server for processing and wait for a reply. Messages move between servers optimally, so every message takes the least amount of time to arrive at the master server. The master server will process all newly arrived messages instantly and send a reply to the originating server via the reversed path the message had gone through.

At the beginning of second 0, each data server sends its message to be processed. Starting from second 1, at the beginning of every second, each data server will check if it has received a reply to the message it sent (including any newly arrived replies) from the master server:

If it has not, it will resend the message periodically. The data server i will resend the message every patience[i] second(s), i.e., the data server i will resend the message if patience[i] second(s) have elapsed since the last time the message was sent from this server.
Otherwise, no more resending will occur from this server.
The network becomes idle when there are no messages passing between servers or arriving at servers.

Return the earliest second starting from which the network becomes idle.
'''


The idea is very simple:

First we calculate the shortest latency ( amount of time it takes for a message to reach the master server plus the time it takes for a reply to reach back the server ) for every node.
Then from their patience time, we calculate for each node, the last time it sends a message before it recieves a reply.
Finally our answer is the maximum of the time for each node from the time they send the first message to the time they recieve a reply for their last message
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            
        dis = {}
        queue = deque([(0, 0)])
        visited = set([0])
        while queue:
            cur, length = queue.popleft()
            dis[cur] = length * 2
            for nxt in graph[cur]:
                if nxt not in visited:
                    queue.append((nxt, length + 1))
                    visited.add(nxt)
        
        ans = -float("inf")
        for i in range(1, len(patience)):
            if patience[i] < dis[i]:
                rem = dis[i] % patience[i]
                lastCall = dis[i] - (rem) if rem > 0 else dis[i] - patience[i]
                ans = max(ans, lastCall + dis[i]) 
            else:
                ans = max(ans, dis[i])
        return ans + 1
      
---------------------------------------------------------------------------------------

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = {}
        for u, v in edges: 
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        
        dist = [-1]*len(graph)
        dist[0] = 0 
        val = 0
        queue = [0]
        while queue: 
            val += 2
            newq = []
            for u in queue: 
                for v in graph[u]: 
                    if dist[v] == -1: 
                        dist[v] = val
                        newq.append(v)
            queue = newq
        
        ans = 0
        for d, p in zip(dist, patience): 
            if p: 
                k = d//p - int(d%p == 0)
                ans = max(ans, d + k*p)
        return ans + 1
