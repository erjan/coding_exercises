'''
A super ugly number is a positive integer whose prime factors are in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.



Instead of checking the numbers one by one, here we are generating the numbers from the already available ugly numbers and keeping a count.
For example: primes = [2,3,5] and n = 16
Here catch is there are multiple additions to heap like 6 = 2*3 and also 6 = 3*2
so what we do is :
for 2, we find multiples of 2 like 2*2 = 4
for 3, we find multiples of 2 and 3 like 3*2 , 3*3 = 6,9
for 5, we find multiples of 2, 3 and 5 like 5*2, 5*3, 5*5 = 10,15,25

'''

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = primes.copy() # do a deep copy 
        heapq.heapify(nums) #create a heap
        p = 1
        for i in range(n - 1):
            p = heapq.heappop(nums) #take the smallest element
            for prime in primes:
                heapq.heappush(nums, p * prime) #add all those multiples with the smallest number
                if p % prime == 0:
					break
        return p
      
