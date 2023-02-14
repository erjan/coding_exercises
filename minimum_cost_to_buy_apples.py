'''
You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads, where roads[i] = [ai, bi, costi] indicates that there is a bidirectional road between cities ai and bi with a cost of traveling equal to costi.

You can buy apples in any city you want, but some cities have different costs to buy apples. You are given the array appleCost where appleCost[i] is the cost of buying one apple from city i.

You start at some city, traverse through various roads, and eventually buy exactly one apple from any city. After you buy that apple, you have to return back to the city you started at, but now the cost of all the roads will be multiplied by a given factor k.

Given the integer k, return an array answer of size n where answer[i] is the minimum total cost to buy an apple if you start at city i.
'''




class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, w in roads: 
            graph[u-1].append((v-1, w))
            graph[v-1].append((u-1, w))
        ans = [inf]*n
        for i in range(n): 
            dist = [inf]*n
            dist[i] = 0 
            pq = [(0, i)]
            while pq: 
                x, u = heappop(pq)
                ans[i] = min(ans[i], appleCost[u]+(1+k)*x)
                for v, w in graph[u]: 
                    xx = x + w
                    if xx < dist[v]: 
                        dist[v] = xx
                        heappush(pq, (xx, v))
        return ans 
      
------------------------------------------------------------------------------------------------------------
Intuition
For node i, we don't have to find out cost to buy an apple from nodes other than i. We only need to find the cheapest buy.
So far, it sounds like a greedy problem, which can be done by a BFS or more appropriate Dijkstra's Algorithm with a some tuning
Approach
Use Dijkstra with help of heap (min-heap in Python)
For each node i, you can either:
visited & buy apple from here
pass by, but not buy apple from here
Add above condition for each neighbor node of node i
Stop the search after you made your first purchase
Apply the above method for all nodes
Complexity
Time complexity: O(n2logn)O(n^2logn)O(n 
2
 logn)
Space complexity: O(N)O(N)O(N)
Code
class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
      graph = collections.defaultdict(list)                # build graph
      for s, e, v in roads:
        graph[s].append((e, v * (1+k)))
        graph[e].append((s, v * (1+k)))
      ans = []        
      def dijkstra(node):                                  # Dijkstra variation, quit on the first buy (greedy)
        nonlocal graph, visited
        heap = [(0, node, 0)]                              # (current cost, current node, bought?)
        res = appleCost[node-1]                            # Buy from self
        while heap:
          cur_val, cur_node, bought = heapq.heappop(heap)
          if bought:                                       # Stop on first buy
            res = min(res, cur_val)
            break
          if cur_node in visited: continue                 # avoid revisit
          visited.add(cur_node)
          for nei, cost in graph[cur_node]:
            heapq.heappush(heap, (cur_val + cost, nei, 0)) # bypass this node (without buying)
            heapq.heappush(heap, \
              (cur_val + cost + appleCost[nei-1], nei, 1)) # bought the apple here
        return res
      for i in range(1, n+1):                              # For each node O(n)
        visited = set()
        ans.append(dijkstra(i))                            # Find the best buy O(nlgn)
      return ans
