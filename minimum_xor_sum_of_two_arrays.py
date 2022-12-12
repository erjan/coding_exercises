'''
You are given two integer arrays nums1 and nums2 of length n.

The XOR sum of the two integer arrays is (nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) (0-indexed).

For example, the XOR sum of [1,2,3] and [3,2,1] is equal to (1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4.
Rearrange the elements of nums2 such that the resulting XOR sum is minimized.

Return the XOR sum after the rearrangement.
'''


from collections import defaultdict

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [defaultdict(lambda:float('inf')) for _ in range(2)]
        for j in range(n): dp[0][1 << j] = nums1[0] ^ nums2[j]
        for i in range(1, n):
            dp[i & 1] = defaultdict(lambda:float('inf'))
            for mask, v in dp[(i - 1) & 1].items():
                for j in range(n):
                    if mask & (1 << j): continue
                    nxt_mask = mask | (1 << j)
                    dp[i & 1][nxt_mask] = min(dp[i & 1][nxt_mask], v + (nums1[i] ^ nums2[j]))
        return dp[(n - 1) & 1][(1 << n) - 1]
      
---------------------------------------------------------------------------------------------------
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        @cache 
        def fn(mask, k): 
            """Return min xor sum."""
            if not mask: return 0 
            ans = inf 
            for i in range(n): 
                if mask & (1<<i): 
                    ans = min(ans, (nums1[i]^nums2[k]) + fn(mask^(1<<i), k+1))
            return ans 
        
        return fn((1<<n)-1, 0)
