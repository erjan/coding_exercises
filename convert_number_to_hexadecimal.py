'''
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.
'''

class Solution:
    def toHex(self, num: int) -> str:
        
               
        if num == 0: return '0'
        
        map = '0123456789abcdef'
        
        result = ''
        
        if num < 0: num+=2**32
            
        while num >0:
            digit = num%16
            num = (num-digit)//16
            result += str(map[digit])
        return result[::-1]
        
       
