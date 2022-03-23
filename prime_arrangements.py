'''
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot 
be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.
'''

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def sieveOfEratosthenes(n):
            primes = [1] * (n + 1)
            for i in range(2, int(math.sqrt(n))+1):
                if primes[i]:
                    primes[i*i:n+1:i] = [0] * len(primes[i*i:n+1:i])            
            return sum(primes) - 2
        
        count = sieveOfEratosthenes(n)        
        return math.factorial(n-count) * math.factorial(count) % (10**9 + 7)
      
      
from math import factorial

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        num_primes = len([x for x in primes if x <= n])  #cleaned up per comment
        return ( factorial(num_primes) * factorial(n - num_primes) ) % (10**9 + 7)      
