
'''

Given an integer n, return its base 3 representation as a string.

'''


class Solution:
    def solve(self, n):
        num = n
        if num == 0: return '0'
        
        map = '012'
        result = ''
        neg = False
        if num < 0: 
            neg= True
            num = -num
            
        while num > 0:
            digit = num% 3
            num = (num-digit)//3
            result += str(map[digit])
        
        res =result[::-1]
        
        if neg:
            res = '-' + res
        return res
        
