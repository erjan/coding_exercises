'''
Given a string s, return the longest palindromic substring in s.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
                        
        res = ''
        resLen = 0
        
        for i in range(len(s)):
            l,r = i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if  (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l = l-1
                r = r+1
            
            l,r = i,i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if  (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l = l-1
                r = r+1
        return res
            
------------------------------------------
#dp

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        longest_palindrome_start, longest_palindrome_len = 0, 1

        for end in range(0, n):
            for start in range(end - 1, -1, -1):
                # print('start: %s, end: %s' % (start, end))
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        palindrome_len = end - start + 1
                        if longest_palindrome_len < palindrome_len:
                            longest_palindrome_start = start
                            longest_palindrome_len = palindrome_len
        return s[longest_palindrome_start: longest_palindrome_start + longest_palindrome_len]
            
