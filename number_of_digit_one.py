'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
'''

def countDigitOne(self, n):
    if n <= 0:
        return 0
    q, x, ans = n, 1, 0
    while q > 0:
        digit = q % 10
        q /= 10
        ans += q * x
        if digit == 1:
            ans += n % x + 1
        elif digit > 1:
            ans += x
        x *= 10
    return ans
  
-----------------------------------------------------------
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n<1: return 0
        digits=len(str(n))

        dp=[0]*digits
        for i in range(1, len(dp)):
            dp[i]=10**(i-1) + 10*dp[i-1]
        
        ans=0
        for i in range(digits):
            lead,n=divmod(n,10**(digits-i-1))

            if 2>lead>=1:
                ans+=dp[digits-i-1]+n+1
            elif lead>=2:
                ans+=lead*dp[digits-i-1]+10**(digits-i-1)
        
        return ans
