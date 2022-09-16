'''
Given a string s, return the last substring of s in lexicographical order.
'''

class Solution:
    def lastSubstring(self, s: str) -> str:
        c = max(set(s))
        res = ''
        for i,x in enumerate(s):
            if x == c:
                res = max(res, s[i:])
        return res
      
--------------------------
def lastSubstring(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        prev = s
        for i in range(1, len(s)):
            if s[i:] > prev:
                prev = s[i:]
        return prev
