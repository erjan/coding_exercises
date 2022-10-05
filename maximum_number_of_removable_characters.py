'''
You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

Return the maximum k you can choose such that p is still a subsequence of s after the removals.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
'''

Binary Search k in interval [0, r), where r = len(removable)
For each mid, check if removable[:mid+1] could make p a subsequence of s.
If True, k could be larger, so we search in the right half; else, search in the left half.

Complexity
Time: O((p+s+r) * logr)
Space: O(r)
where r = len(removable); p = len(p); s = len(s).

Python

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def check(m):
            i = j = 0
            remove = set(removable[:m+1])
            while i < len(s) and j < len(p):
                if i in remove:
                    i += 1
                    continue
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            
            return j == len(p)
            
                
        # search interval is [lo, hi)
        lo, hi = 0, len(removable)+1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
                
        return lo if lo < len(removable) else lo-1
---------------------------------------------------------------------
def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        l, r = 0, len(removable)
        ls, lp = len(s), len(p)
        
        while l < r:
            m = (l + r + 1) >> 1
            d = set(removable[:m])
            i, j = 0, 0
            while i < ls and j < lp:
                if i not in d:
                    if s[i] == p[j]:
                        j += 1
                i += 1
            
            if j == lp:
                l = m
            else:
                r = m - 1
        return r
-------------------------------------------------------------------------------------
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def isSubseq(s,subseq,removed):
            i = 0
            j  = 0
            while i<len(s) and j<len(subseq):
                if i in removed or s[i]!= subseq[j]:
                    i+=1
                    continue
                i+=1
                j+=1
            return j == len(subseq)
        
        removed = set()
        l = 0
        r = len(removable)-1
        ans = 0
        while l<=r:
            mid  = l+(r-l)//2
            removed = set(removable[:mid+1])
            if isSubseq(s,p,removed):
                ans = max(ans,len(removed))
                l = mid+1
                
            else:
                r = mid-1
        return ans                             
