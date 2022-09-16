'''
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
'''

from collections import defaultdict

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def LCS(s1, s2):
            m = len(s1)
            n = len(s2)
            dp = [[0 for j in range(n+1)] for i in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp[m][n]
        
        d = defaultdict(lambda : 0)
        strs.sort(key = lambda x : len(x), reverse=True)
        for s in strs:
            d[s] += 1
        
        for i in range(len(strs)):
            s = strs[i]
            if d[s] == 1:
                # need to check if it is subsequence in any larger strings.
                for j in range(i):
                    if LCS(s, strs[j]) == len(s):
                        break
                else:
                    return len(s)
        return -1
