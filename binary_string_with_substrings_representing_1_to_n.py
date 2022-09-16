'''
Given a binary string s and a positive integer n, return true if the binary representation of all the integers in the range [1, n] are substrings of s, or false otherwise.

A substring is a contiguous sequence of characters within a string.
'''


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1,n+1):
            if (bin(i)[2:]) not in s:
                return False
        return True
      
------------------------

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        leng_s = len(s)
        for i in range(1,n+1):
            binary = str(bin(i)[2:])
            leng_b = len(binary)
            flag = False
            for j in range(leng_s - leng_b + 1):
                if s[j:j + leng_b] == binary:
                    flag = True
                    break
            if flag == False:return False
        return True
      
----------------------------------------------------------------------------------
class Solution(object):
    def queryString(self, S, N):
        for n in xrange(1, N+1):
            if self.toBinary(n) in S:
                continue
            else: return False
        
        return True
        
    def toBinary(self, n):
        digits = []
        while n:
            digits.append(str(n%2))
            n//=2
        return ''.join(digits[::-1])
