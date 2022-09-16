'''
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.
'''

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k % 2 or not k % 5: return -1
        n = length = 1
        while True:
            if not n % k: return length
            length += 1
            n = 10*n + 1
            
-------------------------------------------

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        #edge case
		if k % 2 == 0 or k % 5 == 0: return -1
		
		#keep track of the remainder
        remain, length = 0, 0
        found_so_far = set()
        while remain not in found_so_far:
            found_so_far.add(remain)
            remain = (remain * 10 + 1) % k
            length += 1
        return length if remain == 0 else -1
