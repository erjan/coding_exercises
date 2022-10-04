'''
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
'''

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            bitA = a & 1
            bitB = b & 1
            bitC = c & 1
			
            if bitC:
                if not bitA and not bitB:
                    flips += 1
            else:
                flips += bitA + bitB
				
            a >>= 1
            b >>= 1
            c >>= 1

        return flips
      
-------------------------------------------------------------------

Compare each bit in a, b, c in parallel.
So we will have a loop to loop through all the bits. In each iteration, let's say we have bitA, bitB, bitC.

If bitC is 1, either bitA or bitB should be 1 (or they can both be 1). Otherwise if bitA and bitB are both 0, we must flip at least either bitA or bitB to get a 1 (so "bitA OR bitB" of that bit will be 1).
If bitC is 0, both bitA and bitB should be 0. Otherwise, at least bitA or bitB is 1. To make sure "a OR b" will be 0, we flip bitA if bitA is 1 and flip bitB if bitB is 1.
Here's the most navie approach

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:        
        # convert a, b, c into binary representation
        # [2:] to get rid of the heading '0b'
        # rjust(32,'0') to make them the same length
        binaryA = bin(a)[2:].rjust(32,'0')
        binaryB = bin(b)[2:].rjust(32,'0')
        binaryC = bin(c)[2:].rjust(32,'0')
        
		# you can add print statements here to see what the binary representation looks like
		
        flips = 0
        # loop through each bit
        for i in range(len(binaryC)):
            # get the current bit in each number
            bitA = binaryA[i]
            bitB = binaryB[i]
            bitC = binaryC[i]
            
            if bitC == '1':
                if bitA == '0' and bitB == '0':
                    flips += 1 # at least one of bitA or bitB mus be 1 to make "bitA OR bitB" 1
            else: # bitC is '0'
                # bitA and bitB must be both 0
                if bitA == '1':
                    flips += 1
                if bitB == '1':
                    flips += 1

        return flips
