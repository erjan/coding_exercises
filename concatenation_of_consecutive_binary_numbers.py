'''
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.
'''

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binaryString = "" #our result in form of a string
        for i in range(1,n+1):
            #cast integer i into binary, and then to string, and remove the "0b" component in the front
            binaryString += str(bin(i))[2:]
        #cast from binary to integer
        decimal = int(binaryString, 2)

        return decimal % 1000000007
      
----------------------------------------------------
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        final_number = ''
        for x in range(1, n+1):
            final_number += bin(x)[2:]
        
        return int(final_number, 2) % (10**9 + 7)
