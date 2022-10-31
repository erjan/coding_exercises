'''
You are given two positive integers n and target.

An integer is considered beautiful if the sum of its digits is less than or equal to target.

Return the minimum non-negative integer x such that n + x is beautiful. The input will be generated such that it is always possible to make n beautiful.
'''







'''
Explanation
While the current sum of digits is bigger than target,
we do n = n // 10 + 1
Take example of n = 123456, the process is
123456 -> 123460 -> 123500 -> 124000 -> 130000 -> 2000000

We find the valid n with digits sum no bigger than target,
then we return the final value of n minus its original value n0.
'''


def makeIntegerBeautiful(self, n, target):
      n0 = n
      i = 0
      while sum(map(int, str(n))) > target:
          n = n // 10 + 1
          i += 1
      return n * (10 ** i) - n0
    
-------------------------------------------------------------------------------
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        #function for finding the sum of the digits of a number
        def digit_sum(n):
            return sum([int(c) for c in str(n)])
        
        lst = 1 # the number of zeros we want to leave at the end
        add = 0
        
        #A problem for one idea: 
        #if the sum of digits is greater than target, it is most optimal to make the last few digits equal to zero
        
        while digit_sum(n + add) > target:
            x = 10 ** lst
            add = x - n % x
            lst += 1
        
        return add
        #O(n * lg(n)) - Time
        #O(1) - Space
