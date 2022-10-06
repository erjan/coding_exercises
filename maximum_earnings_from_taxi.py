'''
There are n points on a road you are driving your taxi on. The n points on the road are labeled from 1 to n in the direction you are going, and you want to drive from point 1 to point n to make money by picking up passengers. You cannot change the direction of the taxi.

The passengers are represented by a 0-indexed 2D integer array rides, where rides[i] = [starti, endi, tipi] denotes the ith passenger requesting a ride from point starti to point endi who is willing to give a tipi dollar tip.

For each passenger i you pick up, you earn endi - starti + tipi dollars. You may only drive at most one passenger at a time.

Given n and rides, return the maximum number of dollars you can earn by picking up the passengers optimally.

Note: You may drop off a passenger and pick up a different passenger at the same point.
'''

#dp
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        ans = [0 for i in range(n + 1)] #storage for answer on each point
        end = 0
        
        for p in sorted(rides, key = lambda x: x[1]): #sort list by ends of rides in ascending order
            for i in range(end + 1, p[1]): ans[i] = ans[i - 1] #set maximum earning for points from last end until the end of current ride
            s = p[1] - p[0] + p[2] + ans[p[0]] #calculate earning, in ans[p[0]] we have maximum earning in the start of current ride
            ans[p[1]] = max(ans[p[1]], ans[p[1] - 1], s) #ans[p[1]] is included for cases when the last end is equal to current
			end = p[1]
        
        return ans[end]
      
-----------------------------------------------------------------------
Idea : Start to think in this way that we can track the maximum earning at each point .
eg : n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]

We want to loop from i = 1 to n and at each step check if this i is an end point or not .
if it is an end point then we check all of its corresponding start points and get the maximum earning we can make .

i | 0 | 1 | 2 | 3 | 4 | 5
dp| 0 | 0 | 0 | 0 | 0 | 0

When i=6 ,
we check if 6 is an end point in the given array of rides
yes it is
(Note : -In order to quickly check if this number is an end point or not I am maintaining a dictionary where
key=end point and the value is [start_point,tip])

now I loop through all the corresponding start points whose end point is i
temp_profit = i(end_point) - start_point + tip
but in order to get the total profit at this end point (i) I also have to consider adding dp[start_point]

What this means is max_profit achieved till the start point (i.e dp[start])+ profit achieved from start_point to this end_point(i)
(i.e end_point(i)-start_point+tip)

Hence the eqn :

dp[i] = max(dp[i-1],end_point-start_point+tip+dp[start])

Solution :

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        d = {}
        for start,end,tip in rides:
            if end not in d:
                d[end] =[[start,tip]]
            else:
                d[end].append([start,tip])
        
       
        dp = [0]*(n+1)
        dp[0] = 0
        
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            if i in d:
                temp_profit = 0
                for start,tip in d[i]:
                    if (i-start)+tip+dp[start] > temp_profit:
                        temp_profit = i-start+tip+dp[start]
                dp[i] = max(dp[i],temp_profit)
                
                
        return dp[-1]
