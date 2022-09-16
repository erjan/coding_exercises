'''
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.
'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        k = 2**n-1
        lt = [0]
        x=0
        while(x<n):
            p = len(lt)
            two = 2**x
            for i in range(p-1, -1, -1): #Reverse the output array of n-1
                lt.append(two | lt[i])
            x+=1
        return lt
