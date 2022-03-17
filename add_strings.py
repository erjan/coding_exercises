'''
Given two non-negative integers, num1 and num2 represented 
as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in 
library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)

        a, b = n-1, m-1

        carry = 0
        output = ""

        while a >= 0 or b >= 0:
            i, j = 0, 0

            if a >= 0:
                i = ord(num1[a]) - 48
                a -= 1
            if b >= 0:
                j = ord(num2[b]) - 48
                b -= 1
            tmp = i + j + carry

            if tmp > 9:
                carry = 1
            else:
                carry = 0

            output = str(tmp)[-1] + output
        if carry:
            output = "1" + output
        #print(output)
        return output
