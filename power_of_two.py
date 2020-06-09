#Given an integer, write a function to determine if it is a power of two.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        b = bin(n)
        b = b[2:]
        #print(b)
        binary = True
        b = b[1:]
        #print(b)
        for c in b:
            if c!= '0':
                binary = False
        #print(binary)
        return binary
