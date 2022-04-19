'''
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.

 
 '''

# O(n*3) space
def minCost1(self, costs):
    if not costs:
        return 0
    r, c = len(costs), len(costs[0])
    dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
    dp[0] = costs[0]
    for i in xrange(1, r):
        dp[i][0] = costs[i][0] + min(dp[i-1][1:3])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][:2])
    return min(dp[-1])
 
# change original matrix   
def minCost2(self, costs):
    if not costs:
        return 0
    for i in xrange(1, len(costs)):
        costs[i][0] += min(costs[i-1][1:3])
        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
        costs[i][2] += min(costs[i-1][:2])
    return min(costs[-1])

# O(1) space    
def minCost3(self, costs):
    if not costs:
        return 0
    dp = costs[0]
    for i in xrange(1, len(costs)):
        pre = dp[:] # here should take care
        dp[0] = costs[i][0] + min(pre[1:3])
        dp[1] = costs[i][1] + min(pre[0], pre[2])
        dp[2] = costs[i][2] + min(pre[:2])
    return min(dp)

# O(1) space, shorter version, can be applied 
# for more than 3 colors
def minCost(self, costs):
    if not costs:
        return 0
    dp = costs[0]
    for i in xrange(1, len(costs)):
        pre = dp[:] # here should take care
        for j in xrange(len(costs[0])):
            dp[j] = costs[i][j] + min(pre[:j]+pre[j+1:])
    return min(dp)
  
  -----------------------------------------------
  class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        ## RC ##
        ## APPROACH : DP ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

        n = len(costs)
        if(n==0) : return 0
        for i in range(1,n):
            costs[i][0] += min(costs[i-1][1],costs[i-1][2])
            costs[i][1] += min(costs[i-1][0],costs[i-1][2])            
            costs[i][2] += min(costs[i-1][1],costs[i-1][0])            
        return min(costs[-1])
------------------------------------------------------------------------
Idea:
This is a classic example of a state machine problem. As we iterate through costs, we can consider there to be three distinct states:

We're going to use red this turn
We're going to use blue this turn
We're going to use green this turn
Then we can consider the different ways we can arrive at these three states. For example, if we plan to use red this turn, we can either have used blue or green last turn.

With all this in mind, we can solve this problem using a dynamic programming (DP) approach. Since we're only ever checking one iteration back, we don't need to create a whole DP matrix, we just need to create some variables to hold the current best cost at each state (a, b, c).

If a represents a red turn, then the best new value for a will be the cost of painting red (costs[i][0]) in addition to the lowest value between the blue and green states from last turn (b, c). Then we can use the same process to update the values for b and c. If necessary to not override the previous turn values for a or b before they're used in the other equations, we can store the first two results in temporary variables until the third is done.

Once we finish iterating through costs, the lowest value between a, b, and c should be our final answer, so we can return it.

Time Complexity: O(N) where N is the length of costs
Space Complexity: O(1)
Javascript Code:
The best result for the code below is 72ms / 38.7MB (beats 100% / 30%).

var minCost = function(costs) {
    let a = 0, b = 0, c = 0
    for (let [x,y,z] of costs)
        [a,b,c] = [x + Math.min(b,c), y + Math.min(a,c), z + Math.min(a,b)]
    return Math.min(a,b,c)
};
Python Code:
The best result for the code below is 48ms / 14.1MB (beats 99% / 90%).

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        a,b,c = 0,0,0
        for x,y,z in costs:
            a,b,c = x + min(b,c), y + min(a,c), z + min(a,b)
        return min(a,b,c)
----------------------------------------------------------------------------------------
Update the costs array with the current value + the minimum of the above row excluding the current column (i.e. the minimum cost of painting a color that is not the same as the current color/column). At the end, return the minimum cost in the last row.

class Solution(object):
    def minCost(self, costs):
        if not costs or not costs[0]:
            return 0
        m, n = len(costs), len(costs[0])
        
        for i in range(1, m):
            for j in range(n):
                costs[i][j] += min(costs[i-1][:j] + costs[i-1][j+1:])
        
        return min(costs[-1])
      
--------------------------------------------------
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not len(costs):
            return 0
        lastR, lastG, lastB = costs[0][:]
        for i in range(1, len(costs)):
            curR = min(lastG, lastB) + costs[i][0]
            curG = min(lastR, lastB) + costs[i][1]
            curB = min(lastR, lastG) + costs[i][2]
            lastR, lastG, lastB = curR, curG, curB
        
        return min(min(lastR, lastG), lastB)
      
------------------------------------------------------------------
# DP
# time O(n)
# space O(1)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0][:]
        
        for i in range(1, len(costs)):
            dp[0], dp[1], dp[2] = min(dp[1], dp[2]) + costs[i][0], min(dp[0], dp[2]) + costs[i][1], min(dp[0], dp[1]) + costs[i][2]
        
        return min(dp)
      
      
