'''
Given lowercase alphabet strings s, 
and t return whether you can create a 1-to-1 mapping for 
each letter in s to another letter (could be the same letter) such
that s could be mapped to t, with the ordering of characters preserved.
'''


class Solution:
    def solve(self, s, t):
        return s.translate(str.maketrans(s, t)) == t and len(set(s)) == len(set(t))
      
-----------------------------------      
class Solution:
    def solve(self, s, t):
        ds, dt = {}, {}
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]] = t[i]
            else:
                if ds[s[i]] != t[i]:
                    return False
            if t[i] not in dt:
                dt[t[i]] = s[i]
            else:
                if dt[t[i]] != s[i]:
                    return False
        return True 
      
-------------------------------------------------
class Solution:
    def solve(self, s, t):
        i = 0
        s_map = {}
        t_map = {}
        while i < len(s):
            sc = s[i]
            tc = t[i]
            if sc in s_map:
                if s_map[sc] != tc:
                    return False
            if tc in t_map:
                if t_map[tc] != sc:
                    return False
            s_map[sc] = tc
            t_map[tc] = sc
            i += 1
        return True
