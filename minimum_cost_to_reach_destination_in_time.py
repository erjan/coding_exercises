'''
There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

Each time you pass through a city, you must pay a passing fee. This is represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay when you pass through city j.

In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the summation of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).

Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it within maxTime minutes.
'''


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        mat = {}
        for x, y, time in edges:
            if x not in mat: mat[x] = set()
            if y not in mat: mat[y] = set()
            mat[x].add((y, time))
            mat[y].add((x, time))

        h = [(passingFees[0], 0, 0)]
        visited = set()
        while h:
            fees, time_so_far, city = heappop(h)
            if time_so_far > maxTime: continue
            if city == n - 1: return fees

            if (city, time_so_far) in visited: continue
            visited.add((city, time_so_far))
            
            for nxt, time_to_travel in mat[city]:
                # Check if we are retracing a visited path
                if (nxt, time_so_far - time_to_travel) in visited: continue
                heappush(h, (fees + passingFees[nxt], time_so_far + time_to_travel, nxt))
        return -1
      
-------------------------------------------------------------------------------------------------
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        fee = [float("inf") for i in range(n)]# the final fee
        heap, graph = [(0, passingFees[0], 0)], collections.defaultdict(list)
        for start, end, time in edges:
            graph[start].append((end, time))
            graph[end].append((start, time))
        while heap:
            curTime, curFee, curNode = heappop(heap)
            if fee[curNode] <= curFee:
                continue
            fee[curNode] = curFee
            for neighbor, time in graph[curNode]:
                if time + curTime <= maxTime:
                    heappush(heap, (time + curTime, curFee + passingFees[neighbor], neighbor))
        return fee[-1] if fee[-1] != float("inf") else -1
      
