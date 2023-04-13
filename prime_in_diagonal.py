'''
You are given a 0-indexed two-dimensional integer array nums.

Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.

Note that:

An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.
'''

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:


        def checkPrime(n):
            if n<=1:
                return False
            for i in range(2, int(math.sqrt(n))+1):
                if n%i ==0:
                    return False
            return True
        diag = []
        n = len(nums)
        for i in range(n):
            for j in range(n):

                if i == j:
                    diag.append(nums[i][j])
                if i == n-j-1:
                    diag.append(nums[i][j])
        
        primes = []
        found = False
        for el in diag:
            if checkPrime(el):
                found = True
                primes.append(el)
        
        
        if not found:
            return 0
        else:
            return max(primes)
          
-----------------------------------------------------------------------------------------------------
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        largest_prime = 0
        n = len(nums)
        for i in range(n):
            if is_prime(nums[i][i]):
                largest_prime = max(largest_prime, nums[i][i])
            if is_prime(nums[i][n-i-1]):
                largest_prime = max(largest_prime, nums[i][n-i-1])
        return largest_prime
