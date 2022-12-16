'''
Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.
'''

class Solution(object):
    def countPalindromicSubsequences(self, S):
        memo = {}
        def recurs(subs):    
            if subs not in memo:
                count = 0
                for c in set(subs):
                    left, right = subs.find(c), subs.rfind(c)
                    count += 1 if left==right else 2+recurs(subs[left+1:right])
                memo[subs] = count 
            return memo[subs]
        return recurs(S) % 1000000007  
      
------------------------------------------------------------------------------------------------------
class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)
        pos = dict()
        nexts = [n]*n
        prev = [-1]*n
        for i, c in enumerate(S):
            if c in pos: prev[i] = pos[c]
            pos[c] = i
        pos = dict()
        for j in range(n-1, -1, -1):
            if S[j] in pos: nexts[j] = pos[S[j]]
            pos[S[j]] = j
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for D in range(1, n):
            for i in range(n-D):
                j = i + D
                if S[i] != S[j]:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                else:
                    if nexts[i] > prev[j]: # a...a
                        dp[i][j] = dp[i+1][j-1] * 2 + 2
                    elif nexts[i] == prev[j]: # a..a...a
                        dp[i][j] = dp[i+1][j-1] * 2 + 1
                    else: # a...a....a....a
                        dp[i][j] = dp[i+1][j-1] * 2 - dp[nexts[i]+1][prev[j]-1]
        return dp[0][n-1] % (10**9+7)
