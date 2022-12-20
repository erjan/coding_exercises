'''
There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.

Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.
'''




'''
A state consists of three factors: the left bound and the right bound of current window of stones, and the target number of piles to be merged into.
For the case where only one pile is desired, we prepare 
the stones in the window into best k piles and merge them into one pile. For the case
where more than one pile is desired, we explore the best ways to split the stones into two parts in sizes of i and piles - i, respectively.
'''


class Solution:
    @cache
    def dp(self, l, r, piles) -> int:
        if r - l < piles:
            return inf
        if r - l == piles:
            return 0
        if piles == 1:
            return self.dp(l, r, self.k) + self.prefix_sum[r] - self.prefix_sum[l]
        return min(self.dp(l, m, i) + self.dp(m, r, piles - i) for i in range(1, piles) for m in range(l+i, r-i+1))
            
    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones) - k) % (k - 1) != 0:
            return -1
        self.k = k
        self.prefix_sum = [0]
        for i in range(0, len(stones)):
            self.prefix_sum.append(self.prefix_sum[-1] + stones[i])
        return self.dp(0, len(stones), 1)
      
-----------------------------------------------------------------------------------------------------------------------------


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones)-1) % (k-1): return -1 # impossible
        
        prefix = [0]
        for x in stones: prefix.append(prefix[-1] + x)
        
        @cache
        def fn(lo, hi): 
            """Return min cost of merging stones[lo:hi]."""
            if hi - lo < k: return 0 # not enough stones
            ans = inf 
            for mid in range(lo+1, hi, k-1): 
                ans = min(ans, fn(lo, mid) + fn(mid, hi))
            if (hi-lo-1) % (k-1) == 0: ans += prefix[hi] - prefix[lo]
            return ans 
        
        return fn(0, len(stones))
