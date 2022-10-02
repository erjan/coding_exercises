'''
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.
'''


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        
        m = max(a,b)#this is wrong!!!  # No common divisor will not greater than minimum
        res = 0
        for i in range(1, m+1):
            if a%i == 0 and b%i == 0:
                res+=1
        return res
      
----------------------------------------------------------------
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        x = min(a,b)
        for i in range(1, x+1, 1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count
