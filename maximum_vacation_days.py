'''
LeetCode wants to give one of its best employees the option to travel among n cities to collect algorithm problems. But all work and no play makes Jack a dull boy, you could take vacations in some particular cities and weeks. Your job is to schedule the traveling to maximize the number of vacation days you could take, but there are certain rules and restrictions you need to follow.

Rules and restrictions:

You can only travel among n cities, represented by indexes from 0 to n - 1. Initially, you are in the city indexed 0 on Monday.
The cities are connected by flights. The flights are represented as an n x n matrix (not necessarily symmetrical), called flights representing the airline status from the city i to the city j. If there is no flight from the city i to the city j, flights[i][j] == 0; Otherwise, flights[i][j] == 1. Also, flights[i][i] == 0 for all i.
You totally have k weeks (each week has seven days) to travel. You can only take flights at most once per day and can only take flights on each week's Monday morning. Since flight time is so short, we do not consider the impact of flight time.
For each city, you can only have restricted vacation days in different weeks, given an n x k matrix called days representing this relationship. For the value of days[i][j], it represents the maximum days you could take a vacation in the city i in the week j.
You could stay in a city beyond the number of vacation days, but you should work on the extra days, which will not be counted as vacation days.
If you fly from city A to city B and take the vacation on that day, the deduction towards vacation days will count towards the vacation days of city B in that week.
We do not consider the impact of flight hours on the calculation of vacation days.
Given the two matrices flights and days, return the maximum vacation days you could take during k weeks.
'''


First convert flights to a graph represented by adjacency lists. An edge exists between two cities if there is a flight connecting them. And also include the source city in destination list since we can stay at the source city.

Then dp[week][city] recurrence: dp[w][c] = days[c][w] + max(dp[w+1][dest] for dest in g[c]).
It's easier to use bottom up here since the starting point (week 0) is fixed instead of ending point. Using bottom up, we can get the maximum value for week 0 in our dp table.

Eventually since we start at city 0, answer is the max days from city 0's destinations (in day 0, you can spend rest days of week 0 in city 0 or other cities connected to city 0)

def maxVacationDays(flights, days):
	n, k = len(days), len(days[0])
	g = [[j for j, dst in enumerate(city) if dst]+[i] for i, city in enumerate(flights)]
	dp = [[0] * n for _ in range(k+1)]
	for w in range(k)[::-1]:
		for c in range(n):
			dp[w][c] = days[c][w] + max(dp[w+1][dst] for dst in g[c])
	return max(dp[0][dst] for dst in g[0])


-------------------------------------------------------------------------
Intuition:
We can tell this is a DP problem since subproblems of our original problem will overlap. For example, in some week i, we could be able to fly to some city j from multiple other cities, depending on if there valid flights or not.

We'll use what city we are in, and what week it is as our state values. So, dp(week, city) will tell us the maximum vacation time from this city and week.

Our base case will be if the week is past k, in which case we return 0.

Our recurrance relation will consider traveling to every possible city that we can fly to, and also consider not traveling at all. For each place we travel to, we can calculate the value of staying there as days[city][week], plus dp(week + 1, city), where city is our destination after traveling (or not traveling).

Then, we just need to solve for dp(0,0).

Code:

def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
	k = len(days[0])
	
	@lru_cache(None)
	def dp(week, city):
	    # we are past the amount of weeks we are traveling for
		if week == k:
			return 0 
			
		# consider not traveling (notice city is our original city)
		best = days[city][week] + dp(week + 1, city)
		
		for j in range(len(flights[0])):
			if flights[city][j] == 0:
				# if we can't travel to this city, skip it
				continue
				
			# consider traveling to city j as the answer
			best = max(best, days[j][week] + dp(week + 1, j))
			
		# return the maximal value of all possibilities
		return best
	return dp(0,0)
Analysis:

O(n^2 * k) time from n * k states values to calulate, times n time to calculate each state.
O(n * k) space, since we have n * k states to memoize.


----------------------------------------------------------------------------------------------------
Viterbi Algorithm
    # Find the longest path on a Week (Row) x City (Col) Table

def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
    
    n, k = len(days), len(days[0])                  # days: city x week
    
    dp = [[float('-inf')] * n for _ in range(k)]    # dp: week x city 
    
    dp[0][0] = days[0][0]          
    for d in range(1, n):                           # week 0 can be any city having a flight
        if flights[0][d] == 1: dp[0][d] = days[d][0]

    for t in range(1, k):
        for c in range(n):
            for d, hasflight in enumerate(flights[c]):
                if hasflight or c == d:
                    dp[t][d] = max(dp[t][d], dp[t-1][c] + days[d][t])

    return max(dp[-1])
  
  -------------------------------------------------------------------------------------------------------------
  We consider each city of each day as node. Thus, there are N * k + 2 nodes including the dummy start node and the dummy end node. We connect each node if there is a flight, or if they are the same city. (It means that he just stays at the same city.) After connecting all the possible edges, I performed BFS starting from the dummy start node to find the longest path to all the nodes. The answer is the longest path from the start node to the end node.

Note that in this problem, we are considering the maximum value, so it's not shortest path but longest path.

class Graph:
    def __init__(self, num):
        self.V = num
        self.edges = [[] for _ in range(num)]
        self.dists = [-math.inf for _ in range(num)]
        
    def add_edge(self, a, b, w):
        self.edges[a].append([b, w])
    
    def bfs(self, start):
        queue = deque([start])
        self.dists[start] = 0
        
        while queue:
            u = queue.popleft()
            for ad, dist in self.edges[u]:
                new_dist = self.dists[u] + dist
                if new_dist > self.dists[ad]:
                    self.dists[ad] = new_dist
                    queue.append(ad)
        return self.dists[-1]
         
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        N, k = len(flights), len(days[0])
        #construct graph
        g = Graph(N * k + 2)
        for i in range(N): #first day
            if i == 0 or flights[0][i]:
                g.add_edge(N * k, i, days[i][0])
        for d in range(1, k): #middle days
            for i in range(N):
                for j in range(N):
                    if i == j or flights[i][j] == 1:
                        g.add_edge(N * (d - 1) + i, N * d + j, days[j][d])
        for i in range(N): #final day
            g.add_edge(N * (k - 1) + i, N * k + 1, 0)
        
        return g.bfs(start=N * k)
-------------------------------------------------------------------------------------------------------
Let's maintain best[i], the most vacation days you can have ending in city i on week t. At the end, we simply want max(best), the best answer for any ending city.

For every flight i -> j (including staying in the same city, when i == j), we have a candidate answer best[j] = best[i] + days[j][t], and we want the best answer of those.

When the graph is sparse, we can precompute flights_available[i] = [j for j, adj in enumerate(flights[i]) if adj or i == j] instead to save some time, but this is not required.

def maxVacationDays(self, flights, days):
    NINF = float('-inf')
    N, K = len(days), len(days[0])
    best = [NINF] * N
    best[0] = 0
    
    for t in xrange(K):
        cur = [NINF] * N
        for i in xrange(N):
            for j, adj in enumerate(flights[i]):
                if adj or i == j:
                    cur[j] = max(cur[j], best[i] + days[j][t])
        best = cur
    return max(best)
  
  --------------------------------------------------------------------------------------
  hought process
Recursive backtracking

def backtrack(week, city):

backtrack(week, city) = max(stay: days[city][week] + backtrack(week+1, city), fly: max(backtrack(week+1, other) + days[other][week]) for flights[city][other] == 1)
flights can be optimized using adjacency list
base case: week == N, return 0
because there is no state change, we can use memoization

be careful that even if working in a city all week, it can still provide more opportunites for more vacation in future (because maybe you can only fly to other city and cannot come back, but future weeks in this city may have many vacations)

just try everything possible!

Iterative solution is also simple

Top-down DP
import functools


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        N, K = len(days), len(days[0])
        flights = [[i for i, can_fly in enumerate(city) if can_fly] 
		           for city in flights]
        @functools.lru_cache(None)
        def backtrack(week, city):
            if week == K:
                return 0
            stay = days[city][week] + backtrack(week+1, city)
            fly = max((days[other][week] + backtrack(week+1, other) 
                      for other in flights[city]), default=0)
            return max(stay, fly)
        return backtrack(0, 0)
Bottom-up DP
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        N, K = len(days), len(days[0])
        flights = [[i for i, can_fly in enumerate(city) if can_fly] 
		           for city in flights]
        dp = [[0] * N for _ in range(K+1)]
        for week in range(K-1, -1, -1):
            for city in range(N):
                stay = days[city][week] + dp[week+1][city]
                fly = max((days[other][week] + dp[week+1][other]
                          for other in flights[city]), default=0)
                dp[week][city] = max(stay, fly)
        return dp[0][0]
O(K) space optimization
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        N, K = len(days), len(days[0])
        flights = [[i for i, can_fly in enumerate(city) if can_fly]
                   for city in flights]
        dp = [0] * N
        cur = dp[:]
        for week in range(K-1, -1, -1):
            for city in range(N):
                stay = days[city][week] + dp[city]
                fly = max((days[other][week] + dp[other]
                          for other in flights[city]), default=0)
                cur[city] = max(stay, fly)
            dp, cur = cur, dp
        return dp[0]
      
--------------------------------------------------------------------------------
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        nexts = collections.defaultdict(list)
        for i in range(n):
            nexts[i].append(i)
            for j in range(n):
                if flights[i][j]:
                    nexts[i].append(j)
        m = len(days[0])
        minHeap = [(0,0)]
        for weeks in range(m):
            visited = set()
            temp = []
            while len(temp) < n and minHeap:
                vac,city = heapq.heappop(minHeap)
                for nxt in nexts[city]:
                    if nxt not in visited:
                        visited.add(nxt)
                        heapq.heappush(temp,(vac-days[nxt][weeks],nxt))
            minHeap = temp
        vac,city = heapq.heappop(minHeap)
        return -vac
      
  
      
  
