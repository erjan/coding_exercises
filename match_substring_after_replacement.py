'''
You are given two strings s and sub. You are also given a 2D character array mappings where mappings[i] = [oldi, newi] indicates that you may perform the following operation any number of times:

Replace a character oldi of sub with newi.
Each character in sub cannot be replaced more than once.

Return true if it is possible to make sub a substring of s by replacing zero or more characters according to mappings. Otherwise, return false.

A substring is a contiguous non-empty sequence of characters within a string.
'''


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        if len(s) < len(sub): 
            return False 
        maps = defaultdict(set)
        for u, v in mappings:
            maps[u].add(v)
        
        def f(s1):
            for c1, c2 in zip(s1, sub): 
                if c1 != c2 and c1 not in maps[c2]: 
                    return False 
            return True 
        
        for i in range(len(s) - len(sub) + 1):
            if f(s[i:i+len(sub)]):
                return True

        return False
      
-------------------------------------------------------------------------------------------------
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        dic = {}
        for m in mappings:
            if m[0] not in dic:
                dic[m[0]] = {m[1]}
            else:
                dic[m[0]].add(m[1])
        
        for i in range(len(s)-len(sub)+1):
            j = 0
            while j < len(sub) and (s[i+j] == sub[j] or 
                                    (sub[j] in dic and s[i+j] in dic[sub[j]])):
                j += 1

            if j == len(sub): return True
        
        return False
    
# Time: O(len(s) * len(sub))
# Space: O(len(mapping))
