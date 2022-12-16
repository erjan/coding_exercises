'''
Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.
'''


'''
Algo
Define fn(i, k) to be True if s[i:] can be split into k palindromic substrings. Then,

fn(i, k) = any(fn(ii+1, k-1) where s[i:ii] == s[i:ii][::-1]

Here we create a mapping to memoize all palindromic substrings starting from any given i.
'''             


               
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        mp = {}
        for i in range(2*len(s)-1): 
            lo, hi = i//2, (i+1)//2
            while 0 <= lo <= hi < len(s) and s[lo] == s[hi]: 
                mp.setdefault(lo, set()).add(hi)
                lo -= 1
                hi += 1
        
        @lru_cache(None)
        def fn(i, k): 
            """Return True if s[i:] can be split into k palindromic substrings."""
            if k < 0: return False 
            if i == len(s): return k == 0
            return any(fn(ii+1, k-1) for ii in mp[i])
        
        return fn(0, 3)
      
