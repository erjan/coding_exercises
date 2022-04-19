'''
A series of highways connect n cities numbered from 0 to n - 1. You are given a 2D integer array highways where highways[i] = [city1i, city2i, tolli] indicates that there is a highway that connects city1i and city2i, allowing a car to go from city1i to city2i and vice versa for a cost of tolli.

You are also given an integer discounts which represents the number of discounts you have. You can use a discount to travel across the ith highway for a cost of tolli / 2 (integer division). Each discount may only be used once, and you can only use at most one discount per highway.

Return the minimum total cost to go from city 0 to city n - 1, or -1 if it is not possible to go from city 0 to city n - 1.
'''

The main core of the code is Dijkstra, but the essential part here is that we prune branches.
If you ever get to the same node again, but have fewer or equal discounts, that node is a dead-end
and is pruned.

def minimumCost(self, n, highways, discounts):
	"""
	:type n: int
	:type highways: List[List[int]]
	:type discounts: int
	:rtype: int
	"""
	pq = [(0, 0, discounts)]
	graph = collections.defaultdict(list)
	visited = dict()
	cost = dict()

	for a, b, dist in highways:
		graph[a].append(b)
		graph[b].append(a)
		cost[(a, b)] = dist
		cost[(b, a)] = dist

	while pq:
		curr_cost, node, curr_disc = heapq.heappop(pq)

		# Because of how djikstra works, when we reach this node the first time,
		# we will reach there with the lowest cost.  However, we may reach this node
		# again with a highest cost, but more discount tickets, which can lead to a 
		# more optimal soln at the end.  If we ever come back to this node with the same or 
		# fewer discounts, the soln is not optimal.
		if node in visited and curr_disc <= visited[node]: continue
		visited[node] = curr_disc

		if node == n - 1:
			return curr_cost
		for neigh in graph[node]:
			if curr_disc > 0:
				heapq.heappush(pq, (cost[(node, neigh)] // 2 + curr_cost, neigh, curr_disc - 1))
			heapq.heappush(pq, (cost[(node, neigh)] + curr_cost, neigh, curr_disc))
	# no soln
	return -1


--------------------------------------
class Solution(object):
    def minimumCost(self, n, highways, discounts):
        pq = [(0, discounts, 0)]
        visited = set()
        
        adj = collections.defaultdict(list)
        for city1, city2, toll in highways:
            adj[city1].append((city2, toll))
            adj[city2].append((city1, toll))
        
        
        while pq:
            toll, d, city = heapq.heappop(pq)
            if (d, city) in visited: continue
            visited.add((d, city))
            
            if city==n-1: return toll
            
            for nei, toll2 in adj[city]:
                if (d, nei) not in visited:
                    heapq.heappush(pq, (toll+toll2, d, nei))
                if d>0 and (d-1, nei) not in visited:
                    heapq.heappush(pq, (toll+toll2/2, d-1, nei))    
        
        return -1
		
"""
For interview preparation, similar problems, check out my GitHub.
It took me a lots of time to make the solution. Becuase I want to help others like me.
Please give me a star if you like it. Means a lot to me.
https://github.com/wuduhren/leetcode-python
"""

-----------------------------------------------------------------------------------
class Solution(object):
    def minimumCost(self, n, highways, discounts):
        """
        :type n: int
        :type highways: List[List[int]]
        :type discounts: int
        :rtype: int
        """
		
        from collections import defaultdict
        
        # Create adjacency list
        adj  = defaultdict(list)
        for c1, c2, toll in highways:
            adj[c1].append((toll, c2))
            adj[c2].append((toll, c1))
            
        # Create visited set and (total cost, city, discount heap) heap
        visited = set()
        heap = [(0, 0, [])]
        

        while heap:
            cost, city, discount = heapq.heappop(heap)
            if city in visited:
                continue
            if city == dst - 1:
                return cost
            visited.add(city)

            for n_toll, n_city in adj[city]:
                temp_dis_heap = list(discount)
                if n_city in visited:
                    continue
                new_discount = (n_toll - n_toll//2)
                # If we've used all our discounts and the smallest discount is smaller than
                # our current discount, pop discount heap then push current discount
                if len(discount) == discounts:
                    if len(discount) > 0 and new_discount > discount[0]:
                        smallest_discount = heapq.heappop(temp_dis_heap)
                        new_cost = cost + n_toll//2 + smallest_discount
                        heapq.heappush(temp_dis_heap, new_discount)
                    else:
                        new_cost = cost + n_toll
                # If we haven't used all our discounts, push the current discount 
                # to the discount heap
                else:
                    heapq.heappush(temp_dis_heap, new_discount)
                    new_cost = cost + n_toll//2
                heapq.heappush(heap, (new_cost, n_city, temp_dis_heap))
        return -1 
------------------------------------------------------
At each node, visit all neighbors that have been previously visited according to node and remaining discounts. If discounts still exist, enqueue a trip to the neighboring node both with and without the discount.

import heapq
from collections import defaultdict
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        costs = {(0, 0): 0}
        mapping = defaultdict(list)
        for highway in highways:
            start, end, cost = highway[0], highway[1], highway[2]
            costs[(start, end)] = cost
            costs[(end, start)] = cost
            mapping[start].append(end)
            mapping[end].append(start)
        queue = [(0, discounts, 0)]
        target = n - 1
        visited = set()
        while queue:
            cost, rem, node = heapq.heappop(queue)
            if node == target:
                return cost
            if (node, rem) in visited:
                continue
            visited.add((node, rem))
            for neighbor in mapping[node]:
                if (neighbor, rem) not in visited:
                    heapq.heappush(queue, (cost + costs[node, neighbor], rem, neighbor))
                if rem:
                    if (neighbor, rem - 1) not in visited:
                        heapq.heappush(queue, (cost + costs[node, neighbor] // 2, rem - 1, neighbor))
        return -1
--------------------------------------------------------------------
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        pq = []
        graph = defaultdict(list)
        dp = [[float('inf')] * (discounts + 1) for _ in range(n)]
        for x, y, cost in highways:
            graph[x].append([y, cost])
            graph[y].append([x, cost])
        heappush(pq, [0, discounts, 0])
        dp[0][discounts] = 0
        while pq:
            accur, discnt, cur = heappop(pq)
            for y, cost in graph[cur]:
                if discnt > 0:
                    if accur + cost // 2 < dp[y][discnt - 1]:
                        heappush(pq, [accur + cost // 2, discnt - 1, y])
                        dp[y][discnt - 1] = accur + cost // 2
                if accur + cost < dp[y][discnt]:
                    heappush(pq, [accur + cost, discnt, y])
                    dp[y][discnt] = accur + cost
        res = min(dp[n - 1])
        return res if res != float('inf') else -1
      
      
