'''
A series of highways connect n cities numbered from 0 to n - 1. You are given a 2D integer array highways where highways[i] = [city1i, city2i, tolli] indicates that there is a highway that connects city1i and city2i, allowing a car to go from city1i to city2i and vice versa for a cost of tolli.

You are also given an integer k. You are going on a trip that crosses exactly k highways. You may start at any city, but you may only visit each city at most once during your trip.

Return the maximum cost of your trip. If there is no trip that meets the requirements, return -1.
'''

Take care of the corner case where the number of edges we are asked to use is too large.
Construct the graph.
Top-down

dp(current, mask) = largest travel cost from the current city, given the cities we've visited (and recorded in the bitmask). Try all possible starting points.
if we've already visited k + 1 cities, k edges have been exhausted, we are done.
Otherwise try all possible cities which have a highway with the current city. If visiting a particular city yields a valid solution (k edges used), we can use the result to that subproblem. Trying out a city involves turning on the bit which corresponds to that city in the mask, indicating that the city has been visited.
Time: O(n * 2^n * n + |highways|) - we have n * 2^n states in our dp and we do O(n + n) = O(n) work to transition to next states.
Space:O(n * 2^n + |highways|) - we have to store the graph, and we have n * 2^n states.

class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        if k + 1 > n:
            return -1
        
        graph = defaultdict(list)
        for city_a, city_b, cost in highways:
            graph[city_a].append((city_b, cost))
            graph[city_b].append((city_a, cost))
        
        @cache
        def dp(city, bitmask):
            cities_visited = bitmask.bit_count()
            if cities_visited == k + 1:
                return 0
            
            answer = -1
            for nei_city, highway_cost in graph[city]:
                if not (bitmask >> nei_city) & 1:
                    nei_answer = dp(nei_city, bitmask | (1 << nei_city))
                    if nei_answer != -1:
                        answer = max(answer, highway_cost + nei_answer)
            return answer
        
        return max(dp(city, 1 << city) for city in range(n))
Iterative approach using BFS:

Same idea, just use BFS to explore all possible solutions. Time and space complexity do not change
class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        if k + 1 > n:
            return -1
        
        graph = defaultdict(list)
        for city_a, city_b, cost in highways:
            graph[city_a].append((city_b, cost))
            graph[city_b].append((city_a, cost))
            
        answer = -1
        queue = deque([(city, 1 << city, 0) for city in range(n)])
        while queue:
            city, bitmask, cost = queue.popleft()
            
            if bitmask.bit_count() == k + 1:
                answer = max(answer, cost)
                continue
            
            for nei_city, highway_cost in graph[city]:
                if not (bitmask >> nei_city) & 1:
                    queue.append((nei_city, bitmask | (1 << nei_city), cost + highway_cost))
        
        return answer
-----------------------------------------------------

As the question says there are at most 15 cities, then we can use a bit mask to keep track of the cities that have been visited.
The benefit of a bit mask is the speed, and also it is hashable.
So we can use a top down dp with memoization to try different possibilities and find out the max.

The find_max method accepts 3 parameters:

start - the city where the exploration starts
length - the remaining number of highways we need to travel
visited - the bit mask of cities that we have visited (including the start city)
The find_max returns the max cost to travel length highways from start city after visiting cities described in visited.

class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        graph = [[] for _ in range(n)]
        for city1, city2, toll in highways:
            graph[city1].append((city2, toll))
            graph[city2].append((city1, toll))
        @lru_cache(None)
        def find_max(start, length, visited):
            if length == 0: return 0
            max_toll = -1
            for next_city, toll in graph[start]:
                if visited & (1 << next_city)\
                or (cost := find_max(next_city, length - 1, used | (1 << next_city))) == -1: 
                    continue
                max_toll = max(max_toll, cost + toll)
            return max_toll
        return max(find_max(city, k, 1 << city) for city in range(n))
      
      
      
