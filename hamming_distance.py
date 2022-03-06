'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 
 '''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        x = bin(x)
        y = bin(y)

        diff = abs(len(y) - len(x))

        if len(x) != len(y):
            m = min(len(x), len(y))

            if len(x) < len(y):
                x = str(x)

                x = x[:2] + str(0) * diff + x[2:]
            else:
                y = str(y)
                y = y[:2] + str(0) * diff + y[2:]
   
        c = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                c += 1
        print(c)
        return c
