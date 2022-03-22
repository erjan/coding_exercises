'''
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.
'''

#my own solution

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        n = bin(n)
        print(n, type(n))
        n = n[2:]

        n = list(n)
        for i in range(len(n)):
            if n[i] == '1':
                n[i] = '0'
            else:
                n[i] = '1'
        n = ''.join(n)
        n = int(n, 2)
        print(n)
        return n
      
      
class Solution(object):
    def bitwiseComplement(self, n):
		return ((2 << int(math.log(max(n, 1), 2))) - 1) - n
        # return ((2 << int(math.log(max(n, 1), 2))) - 1) ^ n  # also work
        # return ((2 << int(math.log(max(n, 1), 2))) - 1) & (~n)  # also work      
