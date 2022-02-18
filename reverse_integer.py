'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

class Solution:
    def reverse(self, x: int) -> int:
        reversed_int = 0
        if x < 0:
            str_x = str(x)
            str_x = str_x[::-1]
            str_x = str_x[:-1]
            reversed_int = -int(str_x)
        else:
            str_x = str(x)
            str_x = str_x[::-1]
        
            reversed_int = int(str_x)
          
        if reversed_int > (2**31-1) or reversed_int < -(2**31):
            return 0
        return reversed_int
        
