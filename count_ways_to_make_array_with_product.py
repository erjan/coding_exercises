'''
You are given a 2D integer array, queries. For each queries[i], where queries[i] = [ni, ki], find the number of different ways you can place positive integers into an array of size ni such that the product of the integers is ki. As the number of ways may be too large, the answer to the ith query is the number of ways modulo 109 + 7.

Return an integer array answer where answer.length == queries.length, and answer[i] is the answer to the ith query.
'''

Algo
For any given query, compute prime factorization. For each factor with multiplicity, distribute them into n buckets via multiset.

Implementation

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        spf = list(range(10001)) # spf = smallest prime factor 
        for i in range(4, 10001, 2): spf[i] = 2
        for i in range(3, int(sqrt(10001))+1): 
            if spf[i] == i: 
                for ii in range(i*i, 10001, i): 
                    spf[ii] = min(spf[ii], i)
        
        ans = []
        for n, k in queries: 
            freq = {} # prime factorization via sieve
            while k != 1: 
                freq[spf[k]] = 1 + freq.get(spf[k], 0)
                k //= spf[k]
            val = 1
            for x in freq.values(): 
                val *= comb(n+x-1, x)
            ans.append(val % 1_000_000_007)
        return ans 
      
--------------------------------------------------------------------------------------------------
