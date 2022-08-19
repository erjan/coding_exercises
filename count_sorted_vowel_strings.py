'''
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
'''

class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        dp = [[0 for j in range(6)] for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, 6):
                if i > 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 1 + dp[i][j-1]


        
        return dp[n][5]
      
------------------------------------------
class Solution:
    def countVowelStrings(self, n: int) -> int:        
        dp = [1] * 5
        
        for i in range(2, n+1):
            for j in range(4, -1, -1):
                dp[j] += sum(dp[:j])            
        
        return sum(dp)
      
--------------------------------------------------------
class Solution:
    def countVowelStrings(self, n: int) -> int:        
        dp = [[0] * 6 for _ in range(n+1)]
        for i in range(1, 6):
            dp[1][i] = i
        
        for i in range(2, n+1):
            dp[i][1]=1
            for j in range(2, 6):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[n][5]
      
----------------------------------------
class Solution:
    def countVowelStrings(self, n: int) -> int:        
        return math.comb(n + 4, 4)
