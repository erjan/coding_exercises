'''
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.
'''

import math
class Solution:
    def isThree(self, n: int) -> bool:
        primes = {3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1, 23:1, 29:1, 31:1, 37:1, 41:1, 43:1, 47:1, 53:1, 59:1, 61:1, 67:1, 71:1, 73:1, 79:1, 83:1, 89:1, 97:1}
        if n == 4:
            return True
        else:
            a = math.sqrt(n)

            if primes.get(a,0):
                return True
            else:
                return False

            
            
class Solution:
    def isThree(self, n: int) -> bool:
        #check if exactly 1 divisor exists apart from 1 and number itself
        if n <= 3:
            return False
        count = 0
        for i in range(2,n//2 + 1):
            #print(i)
            if n % i == 0:
                count += 1
            if count > 1:
                return False
        if count == 0:
            return False
        return True    
    
    
import math
class Solution:
    def isThree(self, n: int) -> bool:
        
        count = 0
        
        for i in range(1,n+1):
            
            if n %i == 0:
                count+=1
        return count == 3    
    
    
    
class Solution:
    def isThree(self, n: int) -> bool:
        #check if exactly 1 divisor exists apart from 1 and number itself
        if n <= 3:
            return False
        count = 0
        for i in range(2,n//2 + 1):
            #print(i)
            if n % i == 0:
                count += 1
            if count > 1:
                return False
        if count == 0:
            return False
        return True    
