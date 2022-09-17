'''
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.
'''

def countOrders(self, n: int) -> int:
    a = 1
    for i in range(2, n+1):
        a *= i*(2*i-1)
    return a % (10**9 + 7)
  
----------------------------------------------------------------------

class Solution:
    def countOrders(self, n: int) -> int:
        n=2*n
        ans=1
        while n>=2:
            ans = ans *((n*(n-1))//2)
            n-=2
            ans=ans%1000000007
        return ans
