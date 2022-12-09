'''
You are given an integer n. You roll a fair 6-sided dice n times. Determine the total number of distinct sequences of rolls possible such that the following conditions are satisfied:

The greatest common divisor of any adjacent values in the sequence is equal to 1.
There is at least a gap of 2 rolls between equal valued rolls. More formally, if the value of the ith roll is equal to the value of the jth roll, then abs(i - j) > 2.
Return the total number of distinct sequences possible. Since the answer may be very large, return it modulo 109 + 7.

Two sequences are considered distinct if at least one element is different.
'''


class Solution:
    def distinctSequences(self, n: int) -> int:
        # generate base case, e.g., if you roll 1 and 2 (1,2) then you can roll 3,5 as the next one
        d = defaultdict(list)
        for i in range(1,7):
            for j in range(1,7):
                if (i!=j) & (gcd(i,j)==1):
                    for k in range(1,7):
                        if (i!=k) & (k!=j) & (gcd(k,j)==1):
                            d[(i,j)].append(k)
                    
        if n==1:
            return 6
        elif n==2:
            return len(d.keys())
        else:
            cur = {}
            nex = defaultdict(int)
            for k in d.keys():
                cur[k] = 1
            x = 2
            m = (10**9+7)
            while x<n:
                for k in d.keys():
                    for j in d[k]:
                        nex[(k[1], j)] += (cur[k])%(10**9+7)
                cur = nex
                nex = defaultdict(int)
                x += 1
            return sum(cur.values())%(10**9+7)
            
                    
    def gcd(a, b):
        if(b == 0):
            return abs(a)
        else:
            return gcd(b, a % b)
          
-----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i, prev, prev_prev):
            if i >= n:
                return 1
            result = 0
            for dice in range(1, 7):
                if dice == prev or dice == prev_prev:
                    continue
                if dice % 2 == 0 and prev % 2 == 0:
                    continue
                if dice % 3 == 0 and prev % 3 == 0:
                    continue
                result += dfs(i + 1, dice, prev)
            return result % MOD
        return dfs(0, -1, -1)
      
---------------------------------------------------------------------------------
