'''
Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.
'''


I admit its not the fastest algo for this problem but, if I was in an interview this is probably how I would solve it. Building off the prior palindrome problems, would just try different iterations and see which one works. Use LRU cache for caching already seen input/output.

Idea:
If you see two letters that are not equal, you know one of them must be deleted, so lets just try recursing into both ways (choice restriction is 2).

Time Complexity: O(n^2) Since we have two choices and we are not re computing already seen choices.

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        if s == s[::-1]: return True
        
        @lru_cache(None)
        def validPalindrome(s,l,r,numOfChoices):
            nonlocal k
            while l < r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    if numOfChoices <k:
                        return validPalindrome(s,l+1,r,numOfChoices+1) or validPalindrome(s,l,r-1,numOfChoices+1)
                    elif numOfChoices ==k:  #cannot afford more mistakes
                        return False
            
            return True
            
        
        return validPalindrome(s,0,len(s)-1,0)
      
      
----------------------------------------------------------------------
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        ## RC ##
        ## APPROACH : DP ##
        ## LOGIC ##
        ## 1. Draw Bottom Up DP Table
        ##      a) when length == 1, no change required, so dp[i][j] = 0
        ##      b) when length == 2, if string is aa or bb, we donot require any k, so take previous substring value i.e from diagonal. else we take as 1. i.e we require 1 char to change
        ##      c) when length > 2, we can generalize it as, if s[i] == s[j] then we can remove ith character which requires one operation and take previous s[i+1][j] value or 1 + dp[i][j-1] or we remove both chars take previous substring i.e 2 + dp[i+1][j-1]
        
        ##  STACK TRACE ##
        ## EXAMPLE : BACABAAA ##
        # [
        #     [0, 1, 2, 1, 0, 1, 2, 3], 
        #     [0, 0, 1, 0, 1, 2, 1, 2], 
        #     [0, 0, 0, 1, 2, 1, 2, 2], 
        #     [0, 0, 0, 0, 1, 0, 1, 1], 
        #     [0, 0, 0, 0, 0, 1, 1, 1], 
        #     [0, 0, 0, 0, 0, 0, 0, 0], 
        #     [0, 0, 0, 0, 0, 0, 0, 0], 
        #     [0, 0, 0, 0, 0, 0, 0, 0]
        # ]

        
        dp = [ [0 for _ in s ] for _ in s]
        
        for i in range(len(dp)-1, -1, -1):
            for j in range(i+1,len(dp)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min( 1+dp[i][j-1], 1+dp[i+1][j], 2+dp[i+1][j-1] )
        # print(dp)
        return dp[0][-1] <= k
      
-----------------------------------------------------------------
class Solution:
    
    @cache
    def dp(self, i, j):
        if i==j:
            return 1
        if i>j:
            return 0
        if self.s[i] == self.s[j]:
            return self.dp(i+1, j-1)+2
        else:
            return max(self.dp(i+1, j), self.dp(i, j-1))
    
    def isValidPalindrome(self, s: str, k: int) -> bool:
        self.s = s
        cnt = self.dp(0, len(s)-1)
        remain = len(s) - cnt
        return k>=remain
      
-----------------------------------------------------------------------------
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        return self.longestCommonSubsequence(s, s[::-1]) >= len(s) - k
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        imap = defaultdict(list)
        for i, case in enumerate(text2):
            imap[case].append(-i)

        tail = []
        for case in text1[::-1]:
            for idx in imap[case]:
                j = bisect_left(tail, idx)
                if j == len(tail):
                    tail.append(idx)
                else:
                    tail[j] = idx

        return len(tail)
      
-------------------------------------------------------------------
In each state, k means number of char we can ignore, left and right is the index of the s.

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        @lru_cache(None)
        def dp(l, r, k):
            if l == r or (s[l] == s[r] and r - l == 1): 
                return True
            while r > l:
                if s[l] != s[r]:
                    if k == 0: return False
                    k -= 1
                    return dp(l + 1, r, k) or dp(l, r - 1, k)
                r -= 1
                l += 1
                
            return True            
        return dp(0, len(s) - 1, k)
