#Given an integer num, return a string of its base 7 representation.

class Solution:
    def convertToBase7(self, num: int) -> str:
        
        
        if num == 0: return '0'
        
        map = '0123456'
        result = ''
        neg = False
        if num < 0: 
            neg= True
            num = -num
            
        while num > 0:
            digit = num% 7
            num = (num-digit)//7
            result += str(map[digit])
        
        res =result[::-1]
        
        if neg:
            res = '-' + res
        return res
            
        

        
     
