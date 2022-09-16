'''
Given the strings s1 and s2 of size n and the string evil, return the number of good strings.

A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 109 + 7.
'''

from functools import lru_cache

def srange(a, b):
    yield from (chr(i) for i in range(ord(a), ord(b)+1))
        
def failure(pat): 
    res = [0]
    i, target = 1, 0
    while i < len(pat): 
        if pat[i] == pat[target]: 
            target += 1
            res += target,
            i += 1
        elif target: 
            target = res[target-1] 
        else: 
            res += 0,
            i += 1
    return res                        

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        f = failure(evil)
        @lru_cache(None)
        def dfs(idx, max_matched=0, lb=True, rb=True):
            '''
			idx: current_idx_on_s1_&_s2, 
			max_matched: nxt_idx_to_match_on_evil, 
			lb, rb: is_left_bound, is_right_bound
			'''
            if max_matched == len(evil): return 0 # evil found, break
            if idx == n: return 1 # base case
            
            l = s1[idx] if lb else 'a' # valid left bound
            r = s2[idx] if rb else 'z' # valid right bound
            candidates = [*srange(l, r)]
            
            res = 0
            for i, c in enumerate(candidates):
                nxt_matched = max_matched
                while evil[nxt_matched] != c and nxt_matched:
                    nxt_matched = f[nxt_matched - 1]
                res += dfs(idx+1, nxt_matched + (c == evil[nxt_matched]), 
                           lb=(lb and i == 0), rb=(rb and i == len(candidates)-1))
            return res                
        
        return dfs(0) % (10**9 + 7)
