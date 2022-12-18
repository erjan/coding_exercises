'''
You are given a positive integer n.

Continuously replace n with the sum of its prime factors.

Note that if a prime factor divides n multiple times, it should be included in the sum as many times as it divides n.
Return the smallest value n will take on.
'''






class Solution:
    def prime_factors(self, n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    
    def smallestValue(self, n: int) -> int:
        num = n
        seen = set()
        while num > 0:
            factors = self.prime_factors(num)
            if len(factors) == 1:
                return factors[0]
            num = sum(factors)
            if num in seen:
                break
            seen.add(num)
        return num
            
        
        
