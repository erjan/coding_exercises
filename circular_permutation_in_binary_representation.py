'''
Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :

p[0] = start
p[i] and p[i+1] differ by only one bit in their binary representation.
p[0] and p[2^n -1] must also differ by only one bit in their binary representation.
 
 '''

  def circularPermutation(self, n, start):
        return [start ^ i ^ i >> 1 for i in range(1 << n)]
    
---------------------------------------------------------------
class Solution:
    def solve(self, n, s, res):
        if n == 0:
            res.append(s)
            return s
        s1 = self.solve(n-1, s^0, res)
        s2 = self.solve(n-1, s1^(1<<n-1), res)
        return s2
        
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = []
        self.solve(n, start, res)
        return res
--------------------------------------------------------------------------
def circularPermutation(self, n: int, start: int) -> List[int]:
    res = [i ^ (i // 2) for i in range(pow(2, n))]   #store gray code
    for i in range(len(res)):            
        if start == res[i]:             #match with start value
            return res[i:]+res[:i]
    
    
