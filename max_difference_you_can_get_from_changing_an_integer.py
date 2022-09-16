'''
You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b.
'''

class Solution:
    def maxDiff(self, num: int) -> int:
        a = b = str(num)

        for digit in a:
            if digit != "9":
                a = a.replace(digit, "9")
                break
        
        if b[0] != "1":
            b = b.replace(b[0], "1")
        else:
            for digit in b[1:]:
                if digit not in "01":
                    b = b.replace(digit, "0")
                    break
        
        return int(a) - int(b)
--------------------------------------------------
class Solution:
    def maxDiff(self, num: int) -> int:
        i=0
        while i<len(str(num)):
            change = (str(num)[i])
            if change!='9':
                break
            i+=1
        
        i=0
        flag = False
        while i<len(str(num)):
            sc = (str(num)[i])
            if sc!='1' and sc!='0':
                if i>0:
                    flag =True
                break
            i+=1
        small = str(num)
        num = str(num)
        m=''
        for i in range(len(str(num))):
            if num[i]==change:
                m+='9'
            else:
                m+=num[i]
        m = int(m)
        s =''
        for i in range(len(num)):
            if small[i]==sc:
                if flag:
                    s+='0'
                else:
                    if small[i]=="0":
                        s+='0'
                    else:
                        s+='1'
            else:
                s+=small[i]
        small = int(s)
        return m - small
------------------------------------------
class Solution:
    def maxDiff(self, num: int) -> int:
        
        size = len(str(num))
        max_val = min_val = str(num)
        
        i = 0
        while i < size and max_val[i] == '9':
            i += 1    
        if i < size:
            max_val = max_val.replace(max_val[i], '9')
        
        i = 0
        while i < size and (min_val[i] == '1' or min_val[i] == '0'):
            i += 1
        if i < size:
            min_val = min_val.replace(min_val[i], '0' if i else '1')

        return int(max_val) - int(min_val)
      
      
