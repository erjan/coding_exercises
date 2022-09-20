'''
Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.

Return the maximum possible product of the lengths of the two palindromic subsequences.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.
'''

class Solution:
    def maxProduct(self, s: str) -> int:
        """
            choose letter from s and put them in 2 arrays such that both of them are palindrome. find the longest 2 arrays that can be created
            
            q. is there a greedy way to know which letters to choose in set 1 vs set 2
            a. since s is quite small, i think maybe there might be greedy way bit its best to try all combinations. use dp/bt
        """
        
        @cache
        def dp(ci, s1, s2):
            # ci goes to s1 or s2 or none
            
            if ci == len(s):
                if s1 == s1[::-1] and s2 == s2[::-1]:
                    return len(s1) * len(s2)
                else:
                    return 0
            
            return max(
                dp(ci+1, s1, s2), # donot take
                dp(ci+1, s1 + s[ci], s2),
                dp(ci+1, s1, s2 + s[ci]),
            )
        
        return dp(0, "", "")
        
------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxProduct(self, s: str) -> int:
        
        N = len(s)
        memo = {}
        
        def isValidPalindrom(word):
            left, right = 0, len(word)-1
            while (left < right):
                if word[left] != word[right]: return False
                left += 1
                right -= 1
            
            return True
        
        def backTrack(i, word1, word2):
            
            if i > N: return float('-inf')
            
            if i == N:
                isBothValidPalindrome = isValidPalindrom(word1) and isValidPalindrom(word2)
                return len(word1)*len(word2) if isBothValidPalindrome else float('-inf')
            
            key = (i,word1, word2)
            
            if key in memo: return memo[key]
            
            memo[key] = max([
                backTrack(i+1, word1+s[i], word2),
                backTrack(i+1, word1, word2+s[i]), 
                backTrack(i+1, word1, word2)
            ])
            
            return memo[key]
        
        return backTrack(0,"","")
        
-----------------------------------------------------------------------------------------------
class Solution:
    def maxProduct(self, s: str) -> int:
        self.answer = 0
        
        def dfs(i, word, word2):
            if i >= len(s):
                if word == word[::-1] and word2 == word2[::-1]:
                    self.answer = max(len(word) * len(word2), self.answer)
                return
            
            dfs(i + 1, word + s[i], word2)
            dfs(i + 1, word, word2 + s[i])
            dfs(i + 1, word, word2)
            
        dfs(0, '', '')
        
        return self.answer
