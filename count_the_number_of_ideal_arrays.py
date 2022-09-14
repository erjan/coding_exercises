'''
You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.
'''

class Solution:
    def idealArrays(self, n: int, mx: int) -> int:
        
        @lru_cache(None)
        def gen(k):            
            return math.comb(n-1, k-1)
        
        q = deque([[i, 1] for i in range(1, mx+1)])
        res = 0
        
        while q:
            cur, l = q.popleft()
            res += gen(l)
            nxt = cur * 2
            if l == n or nxt > mx:
                continue
            while nxt <= mx:
                q.append([nxt, l+1])
                nxt += cur
                
        return res % (10**9 + 7)
      
------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7
        ans = maxValue
        freq = {x: 1 for x in range(1, maxValue + 1)}
        for k in range(1, n):
            if not freq:
                break
            nxt = collections.defaultdict(int)
            for x in freq:
                for m in range(2, maxValue // x + 1):
                    ans += math.comb(n - 1, k) * freq[x]
                    nxt[m * x] += freq[x]
            freq = nxt
            ans %= MOD
        return ans
