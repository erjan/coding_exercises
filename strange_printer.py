'''
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.
'''

class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(ch for i, ch in enumerate(s) if i == 0 or s[i-1] != ch)
        
        @cache
        def fn(lo, hi): 
            """Return min ops to print s[lo:hi]."""
            if lo == hi: return 0
            ans = 1 + fn(lo+1, hi)
            for mid in range(lo+1, hi): 
                if s[lo] == s[mid]: 
                    ans = min(ans, fn(lo, mid) + fn(mid+1, hi))
            return ans 
        
        return fn(0, len(s))
