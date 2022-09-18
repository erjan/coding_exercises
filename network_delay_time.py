'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel 
times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum 
time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:        
        adj_list = defaultdict(list)
        
        for x,y,w in times:
            adj_list[x].append((w, y))
        
        visited=set()
        heap = [(0, k)]
        while heap:
            travel_time, node = heapq.heappop(heap)
            visited.add(node)
            
            if len(visited)==n:
                return travel_time
            
            for time, adjacent_node in adj_list[node]:
                if adjacent_node not in visited:
                    heapq.heappush(heap, (travel_time+time, adjacent_node))
                
        return -1

---------------------------------------------------------------------------------------------------------------
import heapq

from collections import defaultdict


def f(times, N, K):
    elapsedTime = [0] + [float("inf")] * N
    graph = defaultdict(list)   # it's a min-heap
    heap = [(0, K)]

    for u, v, w in times:
        graph[u].append((v, w))

    print(graph)

    while heap:
        time, node = heapq.heappop(heap)
        if time < elapsedTime[node]:
            elapsedTime[node] = time
            for v, w in graph[node]:
                heapq.heappush(heap, (time + w, v))
    mx = max(elapsedTime)
    return mx if mx < float("inf") else -1


if __name__ == '__main__':

    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    f(times, n, k)
