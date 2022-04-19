'''
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
'''


If s and t are one distance away then no matter it is insert or delete or replace the count of common characters must be max(m, n) - 1, where m is the length of s and n is the length of t. It is easy to see that the reverse is also true.

Assume the length of common prefix (from left to right) is i and the length of common suffix after i (from right to left) is j, the answer is then max(m, n) - 1 == i + j

Example 1 (1 replace)

s = "abcdefg", m = 7
t = "abcxefg", n = 7 
i = 3, j = 3
max(m, n) - 1 == i + j is true
Example 2 (0 edit)

s = "abcdefg", m = 7
t = "abcdefg", n = 7 
i = 7, j = 0
max(m, n) - 1 == i + j is false
Example 3 (1 insert)

s = "abcdefg", m = 7
t = "abcefg", n = 6 
i = 3, j = 3
max(m, n) - 1 == i + j is true
Example 4 (1 delete 1 insert)

s = "abcdefg", m = 7
t = "abcefgh", n = 7 
i = 3, j = 0
max(m, n) - 1 == i + j is false
The method is O(m+n) since any character is visited at most once.


def isOneEditDistance(self, s, t):
    n, m = len(s), len(t)
    if abs(n - m) > 1:
        return False
    k = min(n, m)
    i = j = 0
    while i < k and s[i] == t[i]:
        i += 1
    while j < k - i and s[~j] == t[~j]:
        j += 1
    return max(n, m) - (i + j) == 1
  
------------------------------------------------
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        lengthS = len(s)
        lengthT = len(t)
        if lengthS > lengthT:
            return self.isOneEditDistance(t, s)
        if lengthT - lengthS > 1:
            return False
        for i in range(lengthS):
            if s[i] != t[i]:
                if s == t[:i] + t[i+1:]:
                    return True
                elif s[:i] + s[i+1:] == t[:i] + t[i+1:]:
                    return True
                else:
                    return False
        return lengthS + 1 == lengthT
                
----------------------------------------------------------------
  def isOneEditDistance(self, s: str, t: str) -> bool:
        LS, LT = len(s), len(t)
        if s == t or LS - LT >1 or LT - LS >1: return False
        
        def rec(si,ti, e):
            if e > 1: return False
            
            if si == LS and ti == LT:
                return e == 1
            
            if si == LS:
                return not e and (LT-ti == 1)
                
            if ti == LT:
                return not e and (LS-si == 1)
            
            if s[si] == t[ti]:
                return rec(si+1,ti+1, e)
            else:
                return rec(si+1,ti, e+1) or rec(si,ti+1, e+1) or rec(si+1,ti+1, e+1)
            
            
        return rec(0, 0, 0)
----------------------------------------------------------------------------
# Worst case: O(n) time | O(1) space
#Best Case: O(1) time + space
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        
        i = j = 0
        edited = False
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if edited: return False
                edited = True
                if len(s) < len(t): 
                    j += 1
                elif len(s) > len(t): 
                    i += 1
                else: 
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1
        
        return True
      
      
--------------------------------------------------
class Solution(object):
    def isOneEditDistance(self, s, t):
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        
        if len(t) - len(s) > 1:
            return False 
        
        cnt = 0
        if len(s) == len(t):
            for i in xrange(len(s)):
                if s[i] != t[i]:
                    cnt += 1
                    if cnt > 1:
                        return False
            return cnt == 1
        else:
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    cnt += 1
                    if cnt > 1:
                        return False
                    j += 1
                else:
                    i += 1
                    j += 1
            return (cnt == 1 and i == len(s) and j == len(t)) or len(t) - j == 1
        
