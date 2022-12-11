'''
You are given a string s consisting of only lowercase English letters. In one operation, you can:

Delete the entire string s, or
Delete the first i letters of s if the first i letters of s are equal to the following i letters in s, for any i in the range 1 <= i <= s.length / 2.
For example, if s = "ababc", then in one operation, you could delete the first two letters of s to get "abc", since the first two letters of s and the following two letters of s are both equal to "ab".

Return the maximum number of operations needed to delete all of s.
'''

class Solution:
    def deleteString(self, s: str) -> int:
        if min(s) == max(s):
            return len(s)
        n = len(s)
        eq = [[0]*(n+1) for i in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == s[j]:
                    eq[i][j] = 1 + eq[i+1][j+1]
        
        dp = [0]*n
        for i in range(n-1, -1, -1):
            dp[i] = 1
            j = 1
            while i+2*j <= n:
                if eq[i][i+j] >= j:
                    dp[i] = max(dp[i], dp[i+j]+1)
                j += 1

        return dp[0]
