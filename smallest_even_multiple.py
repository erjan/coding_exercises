'''
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
 
 '''

def smallestEvenMultiple(self, n):
        return n << (n & 1)
----------------------------------------------------------    
return n if n % 2 == 0 else n * 2

-----------------------------------------------
def smallestEvenMultiple(self, n: int) -> int:
        x=2*n
        i=2
        while (i%n!=0 and i%x!=0):
            i+=2
        return i
-----------------------------------------------------------------
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n*1
        return n*2
