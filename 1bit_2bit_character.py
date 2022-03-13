'''
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.
'''
#stupid question

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        
        # if bits[i] == 0 means it's a 1-bit char
        # if bits[i] == 1 means it's the start of a 2-bit char
        i = 0
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
                
        return i == n - 1 and bits[i] == 0
