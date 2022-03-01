'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written 
as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral 
for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

#my own solution

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = ["I", "V", "X", "L", "C", "D", "M"]
        values = [1, 5, 10, 50, 100, 500, 1000]

        d = dict(zip(symbols, values))
        num = 0
        i = 0

        while i < len(s):
            #print('current letter is ', s[i], ' index i %d' % i)
            if s[i] == "I":

                if (i+1) < len(s) and s[i+1] == "V":
                    num += 4
                    i += 2
                elif (i+1) < len(s) and s[i+1] == "X":
                    num += 9
                    i += 2
                else:
                    num += 1
                    i += 1

            elif s[i] == "V":
                num += 5
                i += 1

            elif s[i] == "X":
                if (i+1) < len(s) and s[i+1] == "L":
                    num += 40
                    i += 2
                elif (i+1) < len(s) and s[i+1] == 'C':
                    num += 90
                    i += 2
                else:
                    num += 10
                    i += 1

            elif s[i] == 'L':
                num += 50
                i += 1

            elif s[i] == "C":
                if (i+1) < len(s) and s[i+1] == "D":
                    num += 400
                    i += 2
                elif (i+1) < len(s) and s[i+1] == 'M':
                    num += 900
                    i += 2
                else:
                    num += 100
                    i += 1
            elif s[i] == 'D':
                num += 500
                i += 1
            elif s[i] == 'M':
                num += 1000
                i += 1

        print('total roman integer is %d' % num)
        return num
