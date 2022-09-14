'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
'''

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        res = []
        nl = len(str(low))
        nh = len(str(high))
        
        for i in range(nl, nh + 1):
            for j in range(0, 10 - i):
                num = int(digits[j: j + i])
                if num >= low and num <= high: res.append(num)
        return res
    
---------------------------------------------------------------------------
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s='123456789'
        ans=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                st=int(s[i:j+1])
                if(st>=low and st<=high):
                    ans.append(st)
        ans.sort()            
        return ans 
