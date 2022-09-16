'''
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
'''

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        ans = 1
        rem = n % 2
        n -= rem
        ans = pow(20, n//2, 10**9 + 7)
        if rem == 1:
            ans *= 5
        return ans % (10**9 + 7)
      
---------------------------------------------------
class Solution:
def countGoodNumbers(self, n: int) -> int:
    MOD = 10**9+7
	
	# No. of even places
    if n%2==0:
        ne=n//2
    else:
        ne=(n+1)//2
    # No. of odd places
    no=n//2
    
    te = pow(5,ne,MOD)      #Total number of even places combinations.
    tp = pow(4,no,MOD)      #Total number of odd/prime combinations.
    return (tp*te)%MOD
