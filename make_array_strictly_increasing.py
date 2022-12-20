'''
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.
'''

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        
        @cache
        def fn(i, prev): 
            """Return min ops to make arr1[i:] increasing w/ given previous element."""
            if i == len(arr1): return 0 
            ans = inf 
            if (prev < arr1[i]): ans = fn(i+1, arr1[i])
            k = bisect_right(arr2, prev)
            if k < len(arr2): ans = min(ans, 1 + fn(i+1, arr2[k]))
            return ans 
        
        ans = fn(0, -inf)
        return ans if ans < inf else -1 
