'''
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.
'''

Solution
LOGIC
Suppose we have a = [8,1,5,2,6]
create a dp = [0, 0, 0, 0] where dp[i] represents the best possible answer if we consider all pairs forming with a[i] (like i = 3 then it will be (0, 3),(1, 3), (2, 3))

For d[0] it will be 0
For d[1] it will be a[0] + a[1] + 0 - 1
For d[2] it will be max((a[0] + a[2] + 0 - 2), (a[1] + a[2] + 1 - 2))
For d[3] it will be max((a[0] + a[3] + 0 - 3), (a[1] + a[3] + 1 - 3), (a[2] + a[3] + 2 - 3))
For d[4] it will be max(a[0] + a[4] + 0 - 4), (a[1] + a[4] + 1 - 4), (a[2] + a[4] + 2 - 4), (a[3] + a[4] + 3 - 4))
Rewriting above by taking about common term out of max() function

For d[0] it will be 0
For d[1] it will be a[0] + 0 + a[1] - 1
For d[2] it will be max((a[0] + 0), (a[1] + 1)) + a[2] - 2
For d[3] it will be max((a[0] + 0 ), (a[1] + 1), (a[2] + 2)) + a[3] - 3
For d[4] it will be max(a[0] + 0 ), (a[1] + 1), (a[2] + 2), (a[3] + 3 )) + a[4] - 4
For a minute lets ignore the part outside the max function and drop it for now, So make a new series and call it dp

For dp[0] it will be 0
For dp[1] it will be a[0] + 0
For dp[2] it will be max((a[0] + 0), (a[1] + 1))
For dp[3] it will be max((a[0] + 0 ), (a[1] + 1), (a[2] + 2))
For dp[4] it will be max(a[0] + 0 ), (a[1] + 1), (a[2] + 2), (a[3] + 3 ))
Here is the catch
dp[i] = max(dp[i-1], a[i-1] + i - 1)
You can Clearly see this pattern in above dp series

Combining this to d series we can get:

For d[0] it will be 0
For d[1] it will be dp[0]+ a[1] - 1
For d[2] it will be max(dp[1], (a[1] + 1)) + a[2] - 2
For d[3] it will be max(dp[2], (a[2] + 2)) + a[3] - 3
For d[4] it will be max(dp[3], (a[3] + 3 )) + a[4] - 4
Now our answer can simply the maximum of d that is max(d), but for improving space complexity i used maxVal to keep track of maximum value

Code
Approach : 1
  
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:      
      dp = [0]*(len(values))
      dp[0] = values[0]
      maxVal = 0
      
      for i in range(1, len(values)):
        dp[i] = max(dp[i-1], values[i-1]+i-1)
        maxVal = max(maxVal, dp[i]+values[i]-i)
      
      return maxVal
    
-------------------------------------------------------------------------------------------------------------------------------------------------------
See you only want to find the maximum value of ((val[i] + i) + (val[j]-j)) which is easy if we have our maximum value of (val[i] + i) being precalculated at every index. So just add (val[j]-j) to that at that "j".
Here is a simple 8 line code for the same.
For better undestanding please take a simple test case and go through each and every line in the code. If you like the solution, please like and upvote it, so it can help other young coders like you.
ThankYou and Have a nice day.

class Solution:
    def maxScoreSightseeingPair(self, values) -> int:
        maxAns = float("-inf") 
        # precalculating the i value
        currPrevMax = values[0]+0
        for j in range(1,len(values)):
            maxAns = max(maxAns,currPrevMax+values[j]-j)
            # Update the previous max incase the current j is the new i
            currPrevMax = max(currPrevMax, values[j]+j) 
        return maxAns
