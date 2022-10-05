'''
You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can take at most one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.
'''

    def maximumCandies(self, A, k):
        left, right = 0, sum(A) / k
        while left < right:
            mid = (left + right + 1) / 2
            if k > sum(a / mid for a in A):
                right = mid - 1
            else:
                left = mid
        return left
      
-----------------------------------------
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        while l <= r:
            m = (l + r)//2
            if self.countPile(candies, m) >= k:
                if self.countPile(candies, m + 1) < k: return m
                l = m + 1
            else:
                r = m - 1
        return 0
                
    def countPile(self, candies, pileSize):
        return sum(candy//pileSize for candy in candies)
      
-----------------------------------------------------------------------------
class Solution:
    
    def countP(self,m,candies):
        res = 0
        for c in candies:
            res += c//m
        return res
                            
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        
        l = 1
        r = max(candies)
    
        while l <=r:
            
            mid = (l+r)//2
            
            if self.countP(mid,candies) >=k:
                if self.countP(mid+1,candies) < k:
                    return mid
                else:
                    l = mid+1
            else:
                r = mid-1
        return 0
                
