'''
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
'''

def minimumDeleteSum(self, s1: str, s2: str) -> int:
    # dp definition
	# dp[i][j] = lowest ASCII sum of deleted char to make s[0...i] and t[0...j] equal.    
    
    # base case
    
    # dp[0][j] = '' to make empty string and t[0...j] equal --> sum of ASCII in t[0...j]
    # dp[i][0] = similarly, sum of ASCII in s[0...i]
    
    
    # case 1: s[i-1] == t[j-1]
    
    # The last characters are identical, so no need to delete anything, and the ASCII sum is same as dp[i-1][j-1]
    # Thus, dp[i][j] = dp[i-1][j-1]
    
    # case 2: s[i-1] != t[j-1]
    
    # The last characters are different. We have 3 sub cases, and we choose the minimum value of these three:
    # subcase 1: delete s[i-1] --> dp[i][j] = dp[i-1][j] + ASCII(s[i-1])
    # subcase 2: delete t[j-1] --> dp[i][j] = dp[i][j-1] + ASCII(t[j-1])
    # subcase 3: delete both s[i-1] and t[j-1] --> dp[i][j] = dp[i-1][j-1] + ASCII(s[i-1]) + ASCII(t[i-1])



    # Code:
    
    
    l1 = len(s1) + 1
    l2 = len(s2) + 1
    
    dp = [[0 for _ in range(l2)] for _ in range(l1)]
    
    for i in range(1, l1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])
    
    for j in range(1, l2):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])
    
    for i in range(1, l1):
        for j in range(1, l2):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]), dp[i-1][j-1] + ord(s1[i-1]) + ord(s2[j-1]))
    
    return dp[-1][-1]
  
---------------------------------------------------------------------------------------------------------------------------------------

'''
This question is a combination of 1143 Longest Increasing Subsequence and 583 Delete Operation for two strings.
It makes sense to solve them first.

Idea:
We will find a longest common subsequence, calcluate its ord value and subtract 2 times this value from the sum of ord of both given strings s1 and s2.
Why do we subtact twice?
Imagine that we found the longest common subsequence for sea and eat. This is ea.
We need to remove it from sea and then from eat, and we do it exactly twice! Thus, we're left with s and t. As a result, we need to return ord(s) + ord(t).

We can copy-paste a dp solution from 1143. The only difference is when two letters are the same:
'''

if s2[c - 1] == s1[r - 1]:
	dp[r][c] = dp[r - 1][c - 1] + ord(s1[r - 1])
instead of 1, we add ord(s1[r - 1]).

For space optimization, we need to maintain only two rows in dp instead of having a large matrix len(s1) * len(s2).

def minimumDeleteSum(s1, s2):  # O(mn) both, where m and n are lengths 
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for r in range(1, len(s1) + 1):
        for c in range(1, len(s2) + 1):
            if s2[c - 1] == s1[r - 1]:
                dp[r][c] = dp[r - 1][c - 1] + ord(s1[r - 1])
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
    return sum(ord(ch) for ch in s1) + sum(ord(ch) for ch in s2) - 2 * dp[-1][-1]
  
--------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)+1
        n = len(s2)+1
        dp=[[0 for i in range(m)]for j in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                if s1[j-1]==s2[i-1]:
                    dp[i][j] = ord(s1[j-1])+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        tot = 0
        for i in s1:
            tot+=ord(i)
        for i in s2:
            tot+=ord(i)
        return tot-2*dp[-1][-1]
  
