'''
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= nums1 < nums2 <= right .
nums1 and nums2 are both prime numbers.
nums2 - nums1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [nums1, nums2]. If there are multiple pairs satisfying these conditions, return the one with the minimum nums1 value or [-1, -1] if such numbers do not exist.

A number greater than 1 is called prime if it is only divisible by 1 and itself.
'''


Intuition
Sieve's algo is one of the most efficient algos to find prime numbers from 2 to n. We find all these primes and store the results in a prime array. Initially all numbers are considered as primes. Then we start marking multiples of any prime marked number as non-prime.

We repeat this process starting from 2 till we reach n. In the end the prime array indicates the prime numbers.

Once we have the primes, we sort the result according to the difference between consecutive prime pairs followed by the first number in the pair. And return the first pair.

Upvote if you like the solution :)

Code
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def solve(start, end):
            prime = [True for i in range(end + 1)] # initially mark all numbers as prime
            p = 2
            
            while(p * p <= end):
                if prime[p]:
                    for i in range(p * p, end + 1, p):
                        prime[i] = False # mark all multiples except for the first number as non-prime
                p += 1
            
            res = deque()
            ans = []
            
            for p in range(max(2, start), end + 1):
                if prime[p]:
                    res.append(p)
                    if len(res) == 2:
                        ans.append((res[1] - res[0],  res[0], res[1]))
                        res.popleft()
            ans.sort()
            return (ans[0][1],ans[0][2]) if ans else [-1, -1]
        
        return solve(left, right)
    
# class Solution: # TLE
#     def closestPrimes(self, left: int, right: int) -> List[int]:
#         def isPrime(n):
#             x = ceil(sqrt(n))
            
#             for i in range(2, x + 1):
#                 if n % i == 0: return False
            
#             return True
        
#         ans = []
#         res = deque()
        
#         for n in range(left, right + 1):
#             if isPrime(n):
#                 res.append(n)
#                 if len(res) == 2:
#                     ans.append((res[1] - res[0],  res[0], res[1]))
#                     res.popleft()
        
#         ans.sort()
#         return (ans[0][1],ans[0][2]) if ans else [-1, -1]
