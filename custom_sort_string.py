'''
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
'''

from collections import defaultdict

class Solution:
    def customSortString(self, S, T) :
        ordering = defaultdict(lambda: -1, ((v, k) for (k, v) in enumerate(S)))
        return ''.join(sorted(T, key=ordering.__getitem__))
      
--------------------------------------------------------------------------------------
from collections import Counter

class Solution:
    def customSortString(self, s: str, t: str) -> str:
        s = list(s)
        h = Counter(t)
        res = ''
        for i in range(len(s)):
            c = s[i]
            if c in h:
                for j in range(h[c]):
                    res += c
                del h[c]
        for key, value in h.items():
            for i in range(value):
                res += key
        return res
