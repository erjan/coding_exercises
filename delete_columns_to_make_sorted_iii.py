'''
You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions, the final array has every string (row) in lexicographic order. (i.e., (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]), and so on). Return the minimum possible value of answer.length.

 
 '''

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0]) # dimensions
        
        @cache 
        def fn(k, prev):
            """Return min deleted columns to make sorted."""
            if k == n: return 0 
            ans = 1 + fn(k+1, prev) # delete kth column
            if prev == -1 or all(strs[i][prev] <= strs[i][k] for i in range(m)): 
                ans = min(ans, fn(k+1, k)) # retain kth column
            return ans 
        
        return fn(0, -1)
