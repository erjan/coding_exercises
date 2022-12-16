'''
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.
'''

class Solution:
    def minInsertions(self, S: str) -> int:
        L = len(S)
        DP = [[0 for _ in range(L+1)] for _ in range(L+1)]
        for i,j in itertools.product(range(L),range(L)): DP[i+1][j+1] = DP[i][j] + 1 if S[i] == S[L-1-j] else max(DP[i][j+1],DP[i+1][j])
        return L - DP[-1][-1]
      
--------------------------------------------------------------------------------------------------------------------------------------------
from functools import lru_cache

class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache(None)
        def dp(s):
            if s == s[::-1]:
                return 0
            elif s[0] == s[-1]:
                return dp(s[1:-1])
			else:
				return 1 + min(dp(s[1:]), dp(s[:-1]))
        
        return dp(s)
