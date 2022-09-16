'''
You are given a positive integer primeFactors. You are asked to construct a positive integer n that satisfies the following conditions:

The number of prime factors of n (not necessarily distinct) is at most primeFactors.
The number of nice divisors of n is maximized. Note that a divisor of n is nice if it is divisible by every prime factor of n. For example, if n = 12, then its prime factors are [2,2,3], then 6 and 12 are nice divisors, while 3 and 4 are not.
Return the number of nice divisors of n. Since that number can be too large, return it modulo 109 + 7.

Note that a prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. The prime factors of a number n is a list of prime numbers such that their product equals n.

 
 '''

The idea is similar to other posts but eliminating some IF condition to make it cleaner.
3*3 > 2*2*2 is the most important fact to solve the problem. So we would always prefer to use 3 as the factor.

MOD = 10**9 + 7
class Solution:
    def maxNiceDivisors(self, n: int) -> int:
        if n <= 2: return n
        i, c = divmod(n, 3)
        if not c: return pow(3, i, MOD)
        return (self.maxNiceDivisors(n-2)*2) % MOD
      
---------------------------------------------------------
MOD = 10**9 + 7
class Solution:
    def maxNiceDivisors(self, n: int) -> int:
        if n <= 2: return n
        i, c = divmod(n, 3)
        if not c: return pow(3, i, MOD)
        return (self.maxNiceDivisors(n-2)*2) % MOD
