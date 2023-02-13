'''
A train line going through a city has two routes, the regular route and the express route. Both routes go through the same n + 1 stops labeled from 0 to n. Initially, you start on the regular route at stop 0.

You are given two 1-indexed integer arrays regular and express, both of length n. regular[i] describes the cost it takes to go from stop i - 1 to stop i using the regular route, and express[i] describes the cost it takes to go from stop i - 1 to stop i using the express route.

You are also given an integer expressCost which represents the cost to transfer from the regular route to the express route.

Note that:

There is no cost to transfer from the express route back to the regular route.
You pay expressCost every time you transfer from the regular route to the express route.
There is no extra cost to stay on the express route.
Return a 1-indexed array costs of length n, where costs[i] is the minimum cost to reach stop i from stop 0.

Note that a stop can be counted as reached from either route.
'''



class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        results = []
        n = len(regular)
        regular_results = []
        express_results = []
        regular_results.append(regular[0])
        express_results.append(min(expressCost + express[0], regular[0] + expressCost))
        regular_results[0] = min(regular_results[0], express_results[0])
        results.append(min(regular_results[0], express_results[0]))
        for i in range(1, n):
            regular_results.append(regular_results[i-1]+regular[i])
            express_results.append(min(regular_results[i-1] + regular[i] + expressCost, express_results[i-1] + express[i]))
            regular_results[i] = min(regular_results[i], express_results[i])
            results.append(min(regular_results[i], express_results[i]))
        return results
      
-----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minimumCosts(self, red: List[int], blue: List[int], blueCost: int) -> List[int]:
        n = len(red) + 1
        R,B = 0, 1
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            dp[i][R] = min(dp[i-1][R] + red[i-1] if i else 0, dp[i-1][B] + blue[i-1] if i else 0)
            dp[i][B] = min((dp[i-1][R] + red[i-1] if i else 0) + blueCost, dp[i-1][B] + blue[i-1] if i else float('inf'))
        return [min(dp[i]) for i in range(1,n)]
      
-------------------------------------------------------------------
class Solution:
    def minimumCosts(self, regular, express, expressCost):
        n = len(regular)

        dp1, dp2 = [float("inf")]*n, [float("inf")]*n

        dp1[0], dp2[0] = regular[0], express[0] + expressCost

        for i in range(1,n):
            dp1[i] = min(dp1[i-1], dp2[i-1]) + regular[i]
            dp2[i] = min(dp1[i-1] + expressCost, dp2[i-1]) + express[i]
            
        return [min(i,j) for i,j in zip(dp1,dp2)]
