'''
You are given a very large integer n, represented as a string,​​​​​​ and an integer digit x. The digits in n and the digit x are in the inclusive range [1, 9], and n may represent a negative number.

You want to maximize n's numerical value by inserting x anywhere in the decimal representation of n​​​​​​. You cannot insert x to the left of the negative sign.

For example, if n = 73 and x = 6, it would be best to insert it between 7 and 3, making n = 763.
If n = -55 and x = 2, it would be best to insert it before the first 5, making n = -255.
Return a string representing the maximum value of n​​​​​​ after the insertion.
'''

If the number is greater than 0 we will iterate from index 0 if the target is greater than the current element we will add it before that.

Else if the number is less than 0 we will iterate from index 0 if target is less than the current we will replace add it there.

We will also keep a flag to check if we have placed the taget number or not if the flag was not striked in the end we will simply add the target number in the end.

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if int(n)>0:
            ans = ""
            flag = False
            for i in range(len(n)):
                if int(n[i])>=x:
                    ans += n[i]
                else:
                    a = n[:i]
                    b = n[i:]
                    ans = a+str(x)+b
                
                    flag = True
                    break
            if not flag:
                ans += str(x)
        else:
            n = n[1:]
            ans = ""
            flag = False
            for i in range(len(n)):
                if int(n[i])<=x:
                    ans += n[i]
                else:
                    a = n[:i]
                    b = n[i:]
                    ans = a+str(x)+b
            
                    flag = True
                    break
            if not flag:
                ans += str(x)
            ans = "-"+ans
        
        return ans
      
