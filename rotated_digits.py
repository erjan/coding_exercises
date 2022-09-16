'''
An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].
'''

class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            p = ''
            if '3' in str(i) or '4' in str(i) or '7' in str(i):
                continue
            for j in str(i):
                if j == '0':
                    p += '0'
                elif j == '1':
                    p += '1'
                elif j == '8':
                    p += '8'
                
                elif j == '2':
                    p += '5'
                elif j == '5':
                    p += '2'
                
                elif j == '6':
                    p += '9'
                elif j == '9':
                    p += '6'
                    
            if p != str(i):
                ans += 1
        
        return ans
      
------------------------------------------------------------------
class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        for i in range(n+1):
            tmp = set(str(i))
            if (tmp - {'1', '0', '8'}) and not tmp & {'3', '7', '4'}:
                res += 1
        return res
-----------------------------------------------
def rotatedDigits(self, N: int) -> int:
        count = 0
        for d in range(1, N+1):
            d = str(d)
            if '3' in d or '4' in d or '7' in d:
                continue
            if '2' in d or '5' in d or '6' in d or '9' in d:
                count+=1
        return count
