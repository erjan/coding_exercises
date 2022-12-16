'''
You are given a string s that consists of the digits '1' to '9' and two integers k and minLength.

A partition of s is called beautiful if:

s is partitioned into k non-intersecting substrings.
Each substring has a length of at least minLength.
Each substring starts with a prime digit and ends with a non-prime digit. Prime digits are '2', '3', '5', and '7', and the rest of the digits are non-prime.
Return the number of beautiful partitions of s. Since the answer may be very large, return it modulo 109 + 7.

A substring is a contiguous sequence of characters within a string.
'''



class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        primes = ['2', '3', '5', '7']
        
        # pruning
        if k * minLength > n or s[0] not in primes or s[-1] in primes:
            return 0
        
        # posible starting indexes of a new partition
        ids = [0]
        for i in range(n-1):
            if s[i] not in primes and s[i+1] in primes:
                ids.append(i+1)
        m = len(ids)

        @cache
        # dp(i, kk) means number of ways to partition s[ids[i]:n] into kk partitions
        def dp(i, kk):
            
            # kk==1: last remaining partition, needs to have length >= l
            if kk == 1:
                return 1 if ids[i]+minLength-1 <= n-1 else 0
            res = 0
            
            # iterate possible starting index of next partition
            for j in range(i+1, m-kk+2):
                if ids[j]-ids[i] >= minLength:
                    res += dp(j, kk-1)
            
            return res % (10**9+7)
        
        return dp(0, k)
        
-------------------------------------------------------------------------------------------------
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        s=list(s)
        l0=len(s)
        prime={'2', '3', '5', '7'}
        for i in range(l0):
            s[i]=s[i] in prime
        if not s[0]:
            return 0
        if s[-1]:
            return 0
        p=10**9+7
        stops=[0]
        for i in range(l0-1):
            if (not s[i]) and s[i+1]:
                stops.append(i+1)
        l1=len(stops)

        def bp(i, k):
            if l0-stops[i]<k*minLength:
                return 0
            if k==1:
                return 1                    
            i1=i+1
            while i1<l1 and stops[i1]<stops[i]+minLength:
                i1+=1
            return sm[i1]%p

        for j in range(1, k+1):
            table=[bp(i, j) for i in range(l1)]
            sm=[]
            tmp=0
            for t in table:
                sm.append(tmp)
                tmp+=t
            sm.append(tmp)
            for i in range(l1+1):
                sm[i]=tmp-sm[i]
        
        return table[0]
