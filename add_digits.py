'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

'''

#my own solution!!!!!!

class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        
        num = str(num)
        if len(num) == 1:
            return int(num)
        
        while len(num)!= 1:
            
            temp = 0
            for i in range(len(num)):
                
                temp += int(num[i])
            
            print(temp)
            num = str(temp)
        
        print(temp)
        return temp
                
