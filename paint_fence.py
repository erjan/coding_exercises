'''
You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.
There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.
'''

If n == 1, there would be k-ways to paint.

if n == 2, there would be two situations:

2.1 You paint same color with the previous post: k*1 ways to paint, named it as same
2.2 You paint differently with the previous post: k*(k-1) ways to paint this way, named it as dif
So, you can think, if n >= 3, you can always maintain these two situations,
You either paint the same color with the previous one, or differently.

Since there is a rule: "no more than two adjacent fence posts have the same color."

We can further analyze:

from 2.1, since previous two are in the same color, next one you could only paint differently, and it would form one part of "paint differently" case in the n == 3 level, and the number of ways to paint this way would equal to same*(k-1).
from 2.2, since previous two are not the same, you can either paint the same color this time (dif*1) ways to do so, or stick to paint differently (dif*(k-1)) times.
Here you can conclude, when seeing back from the next level, ways to paint the same, or variable same would equal to dif*1 = dif, and ways to paint differently, variable dif, would equal to same*(k-1)+dif*(k-1) = (same + dif)*(k-1)

So we could write the following codes:

    if n == 0:
        return 0
    if n == 1:
        return k
    same, dif = k, k*(k-1)
    for i in range(3, n+1):
        same, dif = dif, (same+dif)*(k-1)
    return same + dif
------------------------------------------------------------------------------------


Number of ways to paint 1 fence with k colour = k

Number of ways to paint 2 fence with k colour = k * k (2 Adjacenct fence can be same colour)

Number of ways to paint 3 fence with k colour - there are two posibilities

Fence 1 and Fence 2 are different colours = k * (k-1) * k
Fence 1 and Fence 2 are same colours = k * 1 * (k - 1) - Fence 2 is set 1 once becuase we can chose only 1 colour . Fence 3 is k-1 because we cannot choose the color chosen for fence 2 and 3
Generalising the above step

If f(n) is number of ways to paint n fences with k colour
f(3) = k * (k-1) * k + k * 1 * (k -1) = (k-1) (k + k * k)
f(3) = (k-1) (f(1) + f(2))
This implies f(n) = (k-1) (f(n-1) +f(n-2))

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        if n == 0 or k == 0:
            return 0
        
        mem = [0] * (n + 1)
        mem[0] = k
        mem[1] = k * k
        
        for i in range(2, n):
            mem[i] = (k-1) * (mem[i-1] + mem[i-2])
        
        return mem[n-1]
		```
--------------------------------------------------------------------------------------------------

It's not too hard to figure out the pattern if you play with it.

Suppose k == 3, let's say the 3 colors are a, b, c.

If n == 1, then the result is a b c.
If n == 2, then the result is ab ac ba bc ca cb aa bb cc.

If n > 2, then the result can be derived by appending 2 posts with the same color that is different from the last one to the result of n-2 and appending 1 post with a color that's different from the last one to the result of n-1.

For example, if n == 3, the result is:

abb acc baa bcc caa cbb

and

aba abc aca acb bab bac bca bcb cab cac cba cbc aab aac bba bbc cca ccb

class Solution:
    def numWays(self, n: int, k: int) -> int:
        arr = [0, k, k*k]
        while len(arr) <= n:
            arr.append(arr[-2]*(k-1) + arr[-1]*(k-1))
        return arr[n]
      
----------------------------------------------------------------------
class Solution:
    def numWays(self, n: int, k: int) -> int:
        ## RC ##
        ## APPROACH : DP ##
        """
            No 2 colors should be together.
            Number of ways to paint 1 fence with k colour = k
            Number of ways to paint 2 fence with k colour = k * k (2 Adjacenct fence can be same colour)
            Number of ways to paint 3 fence with k colour - there are two posibilities
            Fence 1 and Fence 2 are different colours = k * (k-1) * k
            Fence 1 and Fence 2 are same colours = k * 1 * (k - 1) - Fence 2 is set 1 once becuase we can chose only 1 colour . Fence 3 is k-1 because we cannot choose the color chosen for fence 2 and 3
            Generalising the above step
            If f(n) is number of ways to paint n fences with k colour
            f(3) = k * (k-1) * k + k * 1 * (k -1) = (k-1) (k + k * k)
            f(3) = (k-1) (f(1) + f(2))
            This implies f(n) = (k-1) (f(n-1) +f(n-2))
            
            ## TIME COMPLEXITY : O(N) ##
		    ## SPACE COMPLEXITY : O(N) ##
        """
        if n == 0 or k == 0:    return 0
        dp = [k, k*k] + [0] * (n - 1)
        for i in range(2, n):
            dp[i] = (k-1) * (dp[i-1] + dp[i-2])
        return dp[n-1]

-------------------------------------------------------------------
There are already some good analysis about this problem in the forum. However, maybe my own way of analyzing this problem can also help.

For a fence, there are only two cases: either it's the same color with the previous fence, or different color with the previous fence. Hence we can create an array of n*2, in which n represents the total number of fences and the column is 2 for two states (same color or different color). We give this array the name "dp".

Now what's the meaning of dp[i][0]? In detail, it means that if we have in total i fences, the number of ways to paint when ith fence has the same color as the i-1 fence. Similarly, dp[i][1] means the number of ways to paint when ith fence has the different color as the i-1 fence. The total ways to paint the in total i fences equals dp[i][0] + dp[i][1].

With this in mind, we have the following equation:

dp[i][0] = dp[i-1][1]   
Translation of the above equation: the count of possibilities when ith fence has the same color as the i-1 fence equals count of possibilities when i-1 th fence has a different color with the i-2 th fence. Because:
--1. The i-1 th fence cannot have the same color as i-2 fence, otherwise there will be 3 colors adjacent. That's why we only have one item : dp[i-1][1] in which the second bracket contains "1" or to say, "different" state.
--2. Now we are just adding the same color at ith fence using i-1's fence color.

Following this logic we would also have:

dp[i][1] = dp[i-1][1]*(k-1) + dp[i-1][0]*(k-1)
Notice that there are two items on the right of the equation. Reason is that when i fence has different color with i-1 fence. We can include cases where i-1 and i-2 fence color to be either same or different.

Below is the python code:

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n<=0: return 0
        if n == 1: return k
        dp = [[0,0] for _ in range(n)]
        dp[0] = [0, k]  # tricky part. Imagine that there is a virtual extra fence on the left.
        
        # dp[i][0] means at i fence, it's same color with the i-1 fence. At this case how many possibilities.
        for i in range(1, n):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][1]*(k-1) + dp[i-1][0]*(k-1)
        return sum(dp[-1])
The disadvantage of this approach maybe that I may use more memories(O(n)) than some of other solutions(O(1)). But I intentionally sacrifice the memory for explaining the questions clearer since I consider a matrix would give us better image of what's going on.


      
      
    
    
  
