'''
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.
'''

class Solution:
    
    def checkPowersOfThree(self, n: int) -> bool:
                
        def ternary(n):
            e = n//3
            q = n%3
            if n == 0:
                return '0'
            elif e == 0:
                return str(q)
            else:
                return ternary(e) + str(q)
        
        
        s = ternary(n)
        
        if '2' in s:
            return False
        return True
--------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
         
        while n!=0:
            rem = n%3
            if rem not in (0,1):
                return False
            n = n//3
        
        return True
