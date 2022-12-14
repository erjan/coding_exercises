'''
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.
'''


#Runtime: 28 ms, faster than 87.88% of Python3 online submissions for Nth Magical Number.
#Memory Usage: 14 MB, less than 92.93% of Python3 online submissions for Nth Magical Number.
class Solution:
    import math
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        
        #initialize u to an overestimate; l to an underestimate
        u, l = n*a, n
        
        #apply binary search to find the right magical number
        while u > l+1:
            mid = l + (u-l)//2
            index = mid//a + mid//b - mid//((a*b)/math.gcd(a,b))
            u, l = mid if index >= n else u, mid if index < n else l
        
        #return solution
        return int((l if l//a + l//b - l//((a*b)/math.gcd(a,b)) == n else u) % (math.pow(10,9) + 7))
      
----------------------------------------------------------------------------------------------------------
