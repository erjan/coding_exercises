'''
Given an integer n, return a binary string representing its representation in base -2.

Note that the returned string should not have leading zeros unless the string is "0".
'''

class Solution:
    def baseNeg2(self, N: int) -> str:
        if N in [0, 1]: return str(N)
        if N % 2 == 0:
            return self.baseNeg2(N // -2) + '0'
        else:
            return self.baseNeg2((N - 1) // -2) + '1'
          
-----------------------------------------------------------------------
class Solution:
    def baseNeg2(self, n: int) -> str:
        s = ''
        if n == 0:
            return '0'
        while n != 0:
            if n % 2 != 0:
                s = '1' + s
                n = (n - 1)//-2
            else:
                s = '0' + s
                n = n//-2
        return s
