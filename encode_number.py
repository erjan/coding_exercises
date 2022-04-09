'''
Given a non-negative integer num, Return its encoding string.

The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:
'''

class Solution:
    def encode(self, num: int) -> str:
        return str(bin(num+1))[3:]
      
---------------------

class Solution:
    def encode(self, n: int) -> str:
        def addbin(a,b):
            if len(a) > len(b):
                return addbin(b,a)
            diff=len(b)-len(a)
            j = ''.join(['0' for _ in range(diff)])
            a=j+a
            carry='0'
            res = []
            for i in range(len(b)-1,-1,-1):
                if a[i]=='1' and b[i]=='1' :
                    if carry=='0' :
                        res.append('0')
                        carry='1'
                    else :
                        res.append('1')
                        carry='1'
                if a[i]=='0' and b[i]=='0' :
                    if carry=='0' :
                        res.append('0')
                        carry='0'
                    else :
                        res.append('1')
                        carry='0'
                if a[i]!=b[i] :
                    if carry=='1' :
                        res.append('0')
                        carry='1'
                    else :
                        res.append('1')
                        carry='0'
            if carry=='1' :
                res.append('1')
            res.reverse()
            return ''.join(res)
        
        if (n&(n+1))==0 :
            return "0"*(int(log(n+1,2)))
        
        i=0
        while (1<<i) < n :
            i+=1
        if (1<<i) > n : i-=1
        B="0"*(i)
        return addbin(bin(n-(1<<i)+1)[2:],B)
They key in this approach is :

If n is of the form (2^x)-1 { n&(n+1) = 0 } then we simply return 'x' zeroes
We take the biggest power of 2 <= n and add number of zeroes (example in 23 biggest power is 16 so we take 4 zeroes)
Now take difference of biggest power and n+1
Perform binary addition of this difference with the initial x '0' string
Example :
n = 23
biggest power of 2 = 16
so base string = 0000
difference = 24-16 = 8 = 1000
binary addition of 0000 and 1000 = 1000

Answer = 1000

Do Upvote if you understood and found this approach better
