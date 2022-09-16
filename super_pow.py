'''
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
'''

class Solution:
    def calc_pow(self,x,n):
        if n == 0: return 1
        
        mid = self.calc_pow(x,n//2)
        
        if n%2==0:
            return (mid*mid)%1337
        else:
            return (x*mid*mid)%1337
        
    def superPow(self, a: int, b: List[int]) -> int:
        b_str = "".join([str(i) for i in b])
        power = int(b_str)        
        return self.calc_pow(a,power)
      
-------------------------------------------------------
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a==1:
            return 1
        c=0
        for i in b:
            c=10*c+i
        return pow(a,c,1337)
