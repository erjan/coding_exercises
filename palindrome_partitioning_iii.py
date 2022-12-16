'''
You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
Return the minimal number of characters that you need to change to divide the string.
'''

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        if len(s) <= k or s == "":
            return 0
        if len(s) == 1:
            return 1
        
        def minChangePalandrome(s): # This will be max function on the previous question
            cnt = 0
            n = len(s)
            
            for i in range(int(n/2)):
                if s[i] != s[n-i-1]:
                    cnt += 1
            
            return cnt
        
        n = len(s)
        dp = [[float("inf")] * k for _ in range(n)]
        
        dp[0][0] = minChangePalandrome(s[0])
        
        for i in range(1, len(s)):
            dp[i][0] = minChangePalandrome(s[0:i+1])
        
        for i in range(n):
            for d in range(1, min(i + 1, k)):
                for l in range(i):
                    dp[i][d] = min(dp[i][d], dp[l][d-1] + minChangePalandrome(s[l+1:i+1]))

        return dp[-1][-1]
      
--------------------------------------------------------------------------------------------------------
Math:
Define dp[i][j] as the minimal number of characters that one needs to change to divide the substring s[i:] when it can be divided into j non-empty disjoint substrings. The recursion eqution is
dp[i][j] = min(cost[i,l] + dp[l+1][j-1] for l in range(i, len(s)-j+1)
where dp[i][1] = cost[i, len(s)-1] and dp[i][len(s)-i] = 0.

Implemenation 1: top-down implementation with memoization

from functools import lru_cache

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        @lru_cache(None)
        def cost(i, j=len(s)-1): 
            """Return cost of converting string[i:j+1] to palindrome"""
            return 0 if i >= j else cost(i+1, j-1) + (s[i]!=s[j])
        
        @lru_cache(None)
        def dp(i, j): 
            """Return minimal char change for string[i:] dividing into j substring
            dp(i, j) = min(cost(i, l) + dp(l+1, j) for l in range(i, len(s)-j))
            dp(i, 0) = cost(i)
            dp(i, len(s)-i) = 0 
            """
            if j == 1: return cost(i)
            return min((cost(i, l)+dp(l+1, j-1) for l in range(i, len(s)-j+1)), default=0)
        
        return dp(0, k)
               
------------------------------------------------------------------------------------------------------------
#bottom up
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        if len(s) <= k or s == "":
            return 0
        if len(s) == 1:
            return 1
        
        def minChangePalandrome(s): # This will be max function on the previous question
            cnt = 0
            n = len(s)
            
            for i in range(int(n/2)):
                if s[i] != s[n-i-1]:
                    cnt += 1
            
            return cnt
        
        n = len(s)
        dp = [[float("inf")] * k for _ in range(n)]
        
        dp[0][0] = minChangePalandrome(s[0])
        
        for i in range(1, len(s)):
            dp[i][0] = minChangePalandrome(s[0:i+1])
        
        for i in range(n):
            for d in range(1, min(i + 1, k)):
                for l in range(i):
                    dp[i][d] = min(dp[i][d], dp[l][d-1] + minChangePalandrome(s[l+1:i+1]))

        return dp[-1][-1]
