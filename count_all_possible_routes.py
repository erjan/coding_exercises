'''
You are given an array of distinct positive integers locations where locations[i] represents the position of city i. You are also given integers start, finish and fuel representing the starting city, ending city, and the initial amount of fuel you have, respectively.

At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|. Please notice that |x| denotes the absolute value of x.

Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more than once (including start and finish).

Return the count of all possible routes from start to finish. Since the answer may be too large, return it modulo 109 + 7.

 
 '''

	def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
		import sys
		sys.setrecursionlimit(10**9)
		
        M = 10**9+7
        @lru_cache(None)
        def helper(curr_city, curr_fuel):
            if curr_fuel<0:
                return 0 
            
            ans = 0
            if curr_city==finish:
                ans += 1
            
            for i in range(len(locations)):
                if i!=curr_city:
                    ans += helper(i, curr_fuel - abs(locations[i]-locations[curr_city]))
                    ans %= M
            
            return ans
        
        return helper(start, fuel)
      
-------------------------------------------------------------------------------------------------------------------
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # start = initial index
        # end = destination index     

        MOD = (10**9)+7 
        lenLocations = len(locations)

        @cache
        def dfs(index, fuel):
            # If you have no more fuel and you're at destination:
            # You cannot try another other routes, return 1 because you're at destination
            if fuel == 0 and index == finish:
                return 1

            # If no more fuel and not at route:
            # You cannot try another other routes, return 1 because you're not at destination
            if fuel <= 0:
                return 0
            
            # If your current index is destination index, you found an existing route
            countWays = 1 if index == finish else 0

            # Try every location index (dfs), but you cannot stay at your current index
            for nextIndex in range(len(locations)):
                if index != nextIndex:
                    cost = abs(locations[index]-locations[nextIndex])
                    countWays += dfs(nextIndex,fuel-cost)

            return countWays

        return dfs(start,fuel) % MOD

----------------------------------------------------------------------------------------------------------------------------
