'''
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.
'''

 
  
  class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(32):
            if Counter(str(n))==Counter(str(2**i)):
                return True
        return False
      
---------------------------------
		l = sorted(list(str(n)))
        for i in range(30):
            a = 2**i
            b = sorted(list(str(a)))
            if l == b:
                return True
