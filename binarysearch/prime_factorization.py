'''

You can write out a number as a product of prime numbers, which are its prime factors. The same prime factor may occur more than once.

Given an integer n greater than 1, find all of its prime factors and return them in sorted order.

'''


class Solution:
    def solve(self, n):
            i = 2

            prime_factors = []
            while i*i <= n:
                if n % i == 0:
                    prime_factors.append(i)
                    n //= i
                else:
                    i += 1

            if n > 1:
                prime_factors.append(n)

            return prime_factors
