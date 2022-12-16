'''
You are given two strings, word1 and word2. You want to construct a string in the following manner:

Choose some non-empty subsequence subsequence1 from word1.
Choose some non-empty subsequence subsequence2 from word2.
Concatenate the subsequences: subsequence1 + subsequence2, to make the string.
Return the length of the longest palindrome that can be constructed in the described manner. If no palindromes can be constructed, return 0.

A subsequence of a string s is a string that can be made by deleting some (possibly none) characters from s without changing the order of the remaining characters.

A palindrome is a string that reads the same forward as well as backward
'''


Algo
Find common characters in word1 and word2 and use the anchor to find longest palindromic subsequence.

Implementation

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        
        @cache
        def fn(lo, hi):
            """Return length of longest palindromic subsequence."""
            if lo >= hi: return int(lo == hi)
            if word[lo] == word[hi]: return 2 + fn(lo+1, hi-1)
            return max(fn(lo+1, hi), fn(lo, hi-1))
        
        ans = 0
        word = word1 + word2
        for x in ascii_lowercase: 
            i = word1.find(x) 
            j = word2.rfind(x)
            if i != -1 and j != -1: ans = max(ans, fn(i, j + len(word1)))
        return ans 
      
----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s1 = word1 + word2
        n = len(s1)
        dp = [[0] * n for i in range(n)]
        ans = 0
        for i in range(n-1,-1,-1):
		# mark every character as a 1 length palindrome
            dp[i][i] = 1
            for j in range(i+1,n):
			# new palindrome is found
                if s1[i] == s1[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
					# if the palindrome includes both string consider it as a valid
                    if i < len(word1) and j >= len(word1):
                        ans = max(ans,dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])
        
        return ans
