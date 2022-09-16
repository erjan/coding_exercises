'''
You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Given the integer n, return the last number that remains in arr.
'''

class Solution:
	def lastRemaining(self, n: int) -> int:
		return 1 if n==1 else 2*(n//2 + 1 - self.lastRemaining(n//2))
  
---------------------------------------------------------------------------
class Solution:
    def lastRemaining(self, n: int) -> int:
        a, b, step = 1, 0, 0

        while n > 1:
            if n % 2 == 0 and step % 2 == 1:
                b -= a
            a *= 2
            step += 1
            n = (n - (n % 2 == 1)) // 2

        return a + b
      
------------------------------------------------------
class Solution:
    def lastRemaining(self, n: int):
        if n%2: n = n-1  // 2k+1 will have the same answer as 2k
        if not n: return 1 // setting up the base case
        return n - 2*(self.lastRemaining(n//2)-1) // recursion step
