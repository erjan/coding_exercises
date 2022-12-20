'''
You are given a string s of length n where s[i] is either:

'D' means decreasing, or
'I' means increasing.
A permutation perm of n + 1 integers of all the integers in the range [0, n] is called a valid permutation if for all valid i:

If s[i] == 'D', then perm[i] > perm[i + 1], and
If s[i] == 'I', then perm[i] < perm[i + 1].
Return the number of valid permutations perm. Since the answer may be large, return it modulo 109 + 7.

 
 '''

from functools import lru_cache


class Solution:
    def __init__(self):
        self.mod = 10 ** 9 + 7

    @lru_cache(maxsize=None)
    def nCk(self, n, k):
        if k == 1: return n
        if k == 0 or n == k: return 1
        return self.nCk(n - 1, k - 1) + self.nCk(n - 1, k)

    @lru_cache(maxsize=None)
    def numPermsDISequence(self, s: str) -> int:
        if len(s) <= 1: return 1
        n = len(s) + 1
        ans = 0
		#Insert max number in every 'DI' part, left and right part are choosed from left numbers
        for i in range(n - 1):
            if s[i:i + 2] == 'ID': ans += self.nCk(n - 1, i + 1) * self.numPermsDISequence(s[:i]) * self.numPermsDISequence(s[i + 2:])
		#Insert max number at start position if s[0] == 'D'
        if s[0] == 'D': ans += self.numPermsDISequence(s[1: n - 1])
		#Same insert max number at end
        if s[n - 2] == 'I': ans += self.numPermsDISequence(s[: n - 2])
        return ans % self.mod
      
-----------------------------------------------------------------------------------------------
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        
        @cache 
        def fn(i, x): 
            """Return number of valid permutation given x numbers smaller than previous one."""
            if i == len(s): return 1 
            if s[i] == "D": 
                if x == 0: return 0 # cannot decrease
                return fn(i, x-1) + fn(i+1, x-1)
            else: 
                if x == len(s)-i: return 0 # cannot increase 
                return fn(i, x+1) + fn(i+1, x)
        
        return sum(fn(0, x) for x in range(len(s)+1)) % 1_000_000_007
