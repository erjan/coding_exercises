'''
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.
'''



Almost same as my original Paint House solution:

return min(reduce(lambda x, y: [y[i] + min(x[i+1:]+x[0:i] or [0]) for i in range(len(x))], costs)) if costs else 0
O(nk) solution:

class Solution:
    # @param {integer[][]} costs
    # @return {integer}
    def minCostII(self, costs):
        return min(reduce(lambda x, y: self.combine(y, x), costs)) if costs else 0

    def combine(self, house, tmp):
        m, n, i = min(tmp), len(tmp), tmp.index(min(tmp))
        tmp = [m]*i + [min(tmp[0:i]+tmp[i+1:])] + [m]*(n-i-1)
        return [sum(i) for i in zip(house, tmp)]
      
      
---------------------------------------------------------------------
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n, k = len(costs), len(costs[0])
        dp = [[float('inf') for _ in range(k)] for _ in range(n)]
        for i in range(k):
            dp[0][i] = costs[0][i]
        
		
        for i in range(1,n):
            for j in range(k):
                for z in range(k):
                    if z != j:
                        dp[i][j] = min(dp[i][j], dp[i-1][z] + costs[i][j])       
        return min(dp[-1])
      
      
-------------------------------------------------------------------------------
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        ## RC ##
        ## APPROACH : BRUTEFORCE - DP ##
        ## Similar to leetcode : Minimum Falling Path Sum II ##
        
		## TIME COMPLEXITY : O(MxNxM) ##
		## SPACE COMPLEXITY : O(1) ##

        if not costs: return 0
        M = len(costs)
        N = len(costs[0])
        for i in range(1, M):
            for j in range(N):
                costs[i][j] = costs[i][j] + min(costs[i-1][:j] + costs[i-1][j+1:])
        return min(costs[-1])
        
        ## APPROACH : DP - OPTIMIZED ##
        ## LOGIC ##
        ## 1. Instead of finding the Minimum everytime, you can save 2 minimums from the prev row initially
        ## 2. while going through j loop, you can directly use first minimum if the first minimum column and current column are not same.
        ## 3. If the first minimum and current column are same THEN ONLY use second minimum
        
		## TIME COMPLEXITY : O(MxN) ##
		## SPACE COMPLEXITY : O(1) ##

        if not costs : return 0
        for i in range(1, len(costs)):
            mins = heapq.nsmallest(2, costs[i - 1])
            for j in range(len(costs[0])):
                costs[i][j] += mins[1] if costs[i - 1][j] == mins[0] else mins[0]
        return min(costs[-1])
      
---------------------------------------------------------------------------------------
Draw a recursion decision tree.
Should the nodes be indexes to houses or colors chosen?

      0
   /  | \
1   1    1

complicated looking to make work with colors

      red                            green
   /  | \                                \
red   green    blue                     ...

colors makes sense 
we always i+1 in each step
return min color the next should be
if we reach end return our value

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(i,color):
            if i==n-1:return costs[i][color]
            min_color=float('inf')
            for new_color in range(k):
                if color==new_color:continue
                min_color= min(min_color,dp(i+1,new_color))
            return costs[i][color]+min_color
        
        min_color=float('inf')
        n=len(costs)
        k=len(costs[0])
        for new_color in range(k):
            min_color= min(min_color,dp(0,new_color))
        return min_color
      
      
----------------------------------------------------------------------
This may not be the best or the most efficient solution but I am posting this on the discussion form because this is the first problem that I solved on my own since I started my leetcode journey two weeks ago. It made me really happy and thought that I will share with others. Please do let me know if I can improve this in anyway. I am open to suggestions.

Time complexity - O(nk)
Space complexity - O(1)

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        m = len(costs[0])

        dp = costs[0]   # first row is stored  in the dp one dimensional array and this will be updated everytime. So use of constant space.
        
        if n == 0: return 0
        
        for i in range(1, n):
            for j in range(m):
                if j == 0: 
                    costs[i][j] += min(dp[j+1 : m]) # minimum from dp's index 1 to last index of dp since j = 0 (2 house can't have same color) 
                elif j == len(costs[0]) - 1:
                    costs[i][j] += min(dp[: j]) # min from dp's  index 0 to last index - 1 because j == last index
                else:
                    costs[i][j] += min(dp[:j] + dp[j+1:]) 
            dp = costs[i] # update dp everytime after the inner loop is over
            
        return min(dp) # return the minimum
