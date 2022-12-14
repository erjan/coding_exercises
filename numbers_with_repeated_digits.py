'''
Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.
'''

class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        limit, s = list(map(int, str(N + 1))), set()
        n, res = len(limit), sum(9 * perm(9, i) for i in range(len(limit) - 1))
        for i, x in enumerate(limit):
            for y in range(i == 0, x):
                if y not in s:
                    res += perm(9 - i, n - i - 1)
            if x in s: 
                break
            s.add(x)
        return N - res
      
----------------------------------------------------------------------------------------------

class Solution:
    def numDupDigitsAtMostN(self, n):
        ans = [int(i) for i in str(n)]
        
        @lru_cache(None)
        def dp(pos,tight,mask):
            if pos == len(ans):
                return 1

            total = 0

            upperlimit = ans[pos] if tight else 9

            for d in range(upperlimit+1):
                if mask&(1<<d):
                    continue

                new_tight = tight and d == upperlimit
                new_mask = mask if mask == 0 and d == 0 else mask|(1<<d)

                total += dp(pos+1,new_tight,new_mask)

            return total

        return n - (dp(0,True,0) - 1)
