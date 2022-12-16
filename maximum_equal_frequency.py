'''
Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).
'''

class Solution:
    def maxEqualFreq(self, N: List[int]) -> int:
        L, C = len(N), collections.Counter(N)
        for i in range(L-1,-1,-1):
            S = set(C.values())
            if len(C.values()) == 1 or S == {1}: return i + 1
            elif len(S) == 2:
                if 1 in S and list(C.values()).count(1) == 1: return i + 1
                if list(C.values()).count(max(S)) == 1 and max(S) - min(S) == 1: return i + 1
            if C[N[i]] == 1: del C[N[i]]
            else: C[N[i]] -= 1
        return 0
		


