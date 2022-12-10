'''
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.
'''

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 0, 1, 2, 3, 4
        mod = 10**9 + 7
        dp = [1, 1, 1, 1, 1]
    
        for _ in range(2, n + 1):
            temp = dp
            dp = [0, 0, 0, 0, 0]
    
            dp[a] = (temp[e] + temp[i] + temp[u]) % mod
            dp[e] = (temp[a] + temp[i]) % mod
            dp[i] = (temp[e] + temp[o]) % mod
            dp[o] = temp[i]
            dp[u] = (temp[i] + temp[o]) % mod
    
        return sum(dp) % mod
    
----------------------------------------------------------------------------------------------------
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp={'a':1,'e':1,'i':1,'o':1,'u':1}
        
        for i in range(n-1):
            dp1={}
            for c in 'aeiou':
                if c=='a':
                    dp1[c]=dp['e']
                elif c=='e':
                    dp1[c]=dp['a']+dp['i']
                elif c=="i":
                    dp1[c]=dp['a']+dp['e']+dp['o']+dp['u']
                elif c=='o':
                    dp1[c]=dp['i']+dp['u']
                elif c=='u':
                    dp1[c]=dp['a']
                    
            dp=dp1
        mod=10**9+7    
        return sum(dp.values())%mod
      
-----------------------------------------------------------------------------
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        x = [1, 1, 1, 1, 1]
        for i in range(n - 1):
            new = [x[1], x[0] + x[2], x[0] + x[1] + x[3] + x[4], x[2] + x[4], x[0]]
            x = new
        res = sum(x) % (pow(10, 9) + 7)
        return res
