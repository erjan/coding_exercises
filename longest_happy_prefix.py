'''
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.
'''


class Solution:
    def longestPrefix(self, s: str) -> str:
        table = [0 for _ in range(len(s))]
        longest_prefix = 0
        for j in range(1, len(s)):
            while longest_prefix>0 and s[longest_prefix]!=s[j]:
                longest_prefix = table[longest_prefix-1]
            if s[longest_prefix]==s[j]:
                longest_prefix+=1
                table[j] = longest_prefix
        return s[:table[-1]]
      
-------------------------------------------------------------------------------------
class Solution:
    def longestPrefix(self, s: str) -> str:
        a, m, p = 1103515245, 2**31, 1
        ans = -1
        prefix_hash, suffix_hash = 0, 0
        for i in range(len(s)-1):
            prefix_hash = (prefix_hash * a + ord(s[i])) % m
            suffix_hash = (suffix_hash + ord(s[-i-1]) * p) % m
            p = p * a % m
            if prefix_hash == suffix_hash and s[:i+1] == s[-i-1:]:
                ans = i
        return s[:ans+1]
