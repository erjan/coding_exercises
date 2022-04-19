'''
You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.

Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.
'''

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        @cache
        def fn(i, k):
            """Return probability of obtaining k heads from coins[i:]."""
            if k < 0: return 0 
            if i == len(prob): return k == 0
            return prob[i]*fn(i+1, k-1) + (1-prob[i])*fn(i+1, k)
        
        return fn(0, target)
Bottom-up implementation

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [[0]*(1 + target) for _ in range(1 + len(prob))]
        dp[-1][0] = 1
        for i in reversed(range(len(prob))): 
            for j in range(target+1): 
                if j: dp[i][j] = prob[i]*dp[i+1][j-1]
                dp[i][j] += (1-prob[i])*dp[i+1][j]
        return dp[0][-1]
      
-----------------------------------------------
class Solution:
  def probabilityOfHeads(self, prob: List[float], t: int) -> float:
    hel = [0]*(t+2)
    hel[0] = 1
    for p in prob:
      for ii in reversed(range(t+1)):
        hel[ii+1] += hel[ii]*p
        hel[ii] *= (1-p)
    return hel[t]
  
---------------------------------------------------------
dp[i] represents the prob of i heads

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [0] * (target+1)
        dp[0] = 1
        for n in range(len(prob)):
            head = prob[n]
            for i in range(target, 0, -1): #inverse order
                dp[i] = dp[i] * (1-head) + dp[i-1] * head
            dp[0] = dp[0] * (1-head)
        return dp[-1]
-------------------------------------------------------------------------
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [1-prob[0]]
        for i in range(1, n):
            dp.append(dp[-1]*(1-prob[i]))
       
        for i in range(target):
            x = [0 for _ in range(n)]
            if i == 0:
                x[0] = prob[0]
            for j in range(1, n):
                x[j] = prob[j]*dp[j-1] + (1-prob[j])*x[j-1]
            dp = x
        return dp[n-1]
                 
---------------------------------------------
class Solution:
    def probabilityOfHeads(self, p: List[float], t: int) -> float:
        n, DP = len(p), [1 - p[0], p[0]*(t > 0)]+[0]*t
        for i in range(1,n):
            d = 0
            for j in range(min(i+2,t+1)): DP[j], d = (1-p[i])*DP[j] + p[i]*d, DP[j]
        return DP[t]
        
      
  
