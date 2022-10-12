'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.
'''



class Solution:
    def numDistinct(self, s, t):
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for col in range(len(dp[0])):
            dp[0][col] = 1
        for x in range(1, len(s) + 1):
            for y in range(1, len(t) + 1):
                if s[x - 1] == t[y - 1]:
                    dp[y][x] = dp[y - 1][x - 1] + dp[y][x - 1]
                else:
                    dp[y][x] = dp[y][x - 1]
        return dp[-1][-1]
      
----------------------------------------------------------------------
def numDistinct(self, s, t):
    state = [1]+[0]*len(t)
    for c in s:
        new = state[:]
        for i,k in enumerate(t):
            if k==c: new[i+1] += state[i]
        state = new
    return state[-1]
  
---------------------------------------------------------------------------------------------------
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ## RC ##
		## APPROACH : DP ##
		## LOGIC ##
		#	1. Point to be noted, empty seq is also subsequence of any sequence i.e "", "" should return 1. so we fill the first row accordingly
		#	2. if chars match, we get the maximum of [diagonal + upper, upper + 1] (Try below example)
		#	3. if no match, we pull the upper value
		
        ## EXAMPLE : "axacccax" "aca"	##
		## STACK TRACE ##
        # [      ""  a  c  a
        #     "" [1, 0, 0, 0], 
        #     a  [1, 1, 0, 0], 
        #     x  [1, 1, 0, 0], 
        #     a  [1, 2, 0, 0], 
        #     c  [1, 2, 2, 0], 
        #     c  [1, 2, 4, 0], 
        #     c  [1, 2, 6, 0], 
        #     a  [1, 3, 6, 6], 
        # ]
        
		## TIME COMPLEXITY : O(MxN) ##
		## SPACE COMPLEXITY : O(MxN) ##

        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        
        for k in range(len(dp)):
            dp[k][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if(s[i-1] == t[j-1] and dp[i-1][j-1]):
                    dp[i][j] = max(dp[i-1][j-1] + dp[i-1][j], dp[i-1][j]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[-1][-1]
