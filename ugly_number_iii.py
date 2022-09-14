'''
An ugly number is a positive integer that is divisible by a, b, or c.

Given four integers n, a, b, and c, return the nth ugly number.
'''

from math import gcd

class Solution:
    

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        
        def lcm( x, y):
            
            # From number theory,
            # gcd(x,y) * lcm(x,y) = x * y
            
            return  x * y  // gcd(x,y)        
        
        # -----------------------------------
        
        def total_num_of_multiples( number, a, b, c):
            
            # From set theory,
            # count the total number of mutiples of a, b, c, range from 1 to number.
            ab = lcm(a,b)
            bc = lcm(b,c)
            ac = lcm(a,c)

            abc = lcm(a, bc)

            result = number // a + number // b + number // c 
            result -= number // ab + number // bc + number // ac
            result += number // abc

            return result        
        
        # -----------------------------------
        
        # Goal:
        # Find the smallest number k, such that k has n multiples of a, b, or c.
        
        # Binary search approach
        lower = 1
        upper = 2 * (10 ** 9)
        
        while lower < upper:
            
            mid = lower + (upper - lower) // 2
            
            count_of_u_number = total_num_of_multiples(mid, a, b, c)

            if count_of_u_number >= n:
                upper = mid
                
            else:
                lower = mid+1
            
        return lower
