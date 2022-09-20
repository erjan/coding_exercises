'''
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".
'''


class Solution(object):
    def repeatedStringMatch(self, A, B):
        times = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a))
        for i in range(2):
            if B in (A * (times + i)):
                return times + i
        return -1
      
-------------------------------------------------------------------------
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(b) // len(a)
        
        if b in a * n: return n
        if b in a * (n + 1): return n + 1
        if b in a * (n + 2): return n + 2
        
        return -1
