'''
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
'''
from collections import defaultdict
from functools import cache

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for i, num in enumerate(arr):
            d[num] = i
        @cache
        def dfs(i, j):
            if j == len(arr): return 0
            if arr[i] + arr[j] in d:
                return  1 + dfs(j, d[arr[i] + arr[j]])
            return 0
        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i]+arr[j] in d:
                    res = max(res, dfs(i, j))
        return res + 2 if res > 0 else 0
      
-------------------------------------------------------------------------------------------      

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        d = {arr[i]:i for i in range(n)}
        best=0
        for i in range(n):         
            for j in range(i+1,n):
                tmp = 2
                a = arr[i]
                b = arr[j]
                while True:
                    if a+b in d:
                        c= a+b
                        a = b
                        b = c 
                        tmp+=1
                    else:break
                if tmp>best:best=tmp
                        
        return best  if best>2 else 0 
