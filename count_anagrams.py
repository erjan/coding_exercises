
'''
On the math level, this is basically a test of multinomial coeffcients. The tricky part lies in the implementation.
'''

class Solution: 
    def countAnagrams(self, s: str) -> int:
        n = len(s)
        mod = 1_000_000_007
        inv = [1]*(n+1)
        fact = [1]*(n+1)
        ifact = [1]*(n+1)
        for x in range(1, n+1): 
            if x >= 2: inv[x] = mod - mod//x * inv[mod % x] % mod 
            fact[x] = fact[x-1] * x % mod 
            ifact[x] = ifact[x-1] * inv[x] % mod 
        ans = 1
        for word in s.split(): 
            ans *= fact[len(word)]
            for x in Counter(word).values(): ans *= ifact[x]
            ans %= mod 
        return ans 
      
--------------------------------------------------------------------------------------------------------
class Solution:
    def perm(self,word:str)->int:
        n=len(word)
        d=dict()
        ret=math.factorial(n)
        for i in range(n):
            if ord(word[i]) not in d:
                d.update({ord(word[i]):0})
            d[ord(word[i])]+=1
        for v in d.values():
            ret=ret//math.factorial(v)
        return ret
    def countAnagrams(self, s: str) -> int:
        i=0
        j=0
        n=len(s)
        ret=1
        while i<n and j<n:
            if s[j]==' ':
                word=s[i:j]
                ret*=self.perm(word)
                i=j+1
                j=i
            elif j==n-1:
                word=s[i:]
                ret*=self.perm(word)
                j+=1
            else:j+=1
        return ret%(10**9+7)
