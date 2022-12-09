'''
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
'''

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def fn(x): 
            """Return node counts in denary trie."""
            ans, diff = 0, 1
            while x <= n: 
                ans += min(n - x + 1, diff)
                x *= 10 
                diff *= 10 
            return ans 
        
        x = 1
        while k > 1: 
            cnt = fn(x)
            if k > cnt: k -= cnt; x += 1
            else: k -= 1; x *= 10 
        return x
      
------------------------------------------------------------------------------------------------------------
class Solution:
    def binmatch(self,A,k):
        i,s = 0,0
        for i,x in enumerate(A):
            s += x
            if s>=k:
                s -= x
                break
        return i,s
    def bincount(self,n,r):
        A = [0]*r
        s = 1
        while n>0:
            for i in range(r):
                s     = min(n,s)
                A[i] += s
                n    -= s
                if n<=0:
                    break
            s *= 10
        return A  
    def remainder(self,t,c): # target, container size
        if t==1:
            return # t=1 is always Null Zero (1,10,100,etc..)
        t -= 1 # subtract Null Zero
        c -= 1
        A  = self.bincount(c,r=10)
        i,s = self.binmatch(A,t)
        yield i
		# yield from self.remainder(t-s,A[i]) # only works in Python 3
        for j in self.remainder(t-s,A[i]): 
            yield j
    def findKthNumber(self, n, k): #-> int:
        # Find first digit:
        A   = self.bincount(n,r=9)
        i,s = self.binmatch(A,k)
        res = i+1
        # Find Upcoming Digits
        for x in self.remainder(k-s,A[i]):
            res = 10*res + x
        return res
