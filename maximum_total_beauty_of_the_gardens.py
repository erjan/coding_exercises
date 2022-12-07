'''
Alice is a caretaker of n gardens and she wants to plant flowers to maximize the total beauty of all her gardens.

You are given a 0-indexed integer array flowers of size n, where flowers[i] is the number of flowers already planted in the ith garden. Flowers that are already planted cannot be removed. You are then given another integer newFlowers, which is the maximum number of flowers that Alice can additionally plant. You are also given the integers target, full, and partial.

A garden is considered complete if it has at least target flowers. The total beauty of the gardens is then determined as the sum of the following:

The number of complete gardens multiplied by full.
The minimum number of flowers in any of the incomplete gardens multiplied by partial. If there are no incomplete gardens, then this value will be 0.
Return the maximum total beauty that Alice can obtain after planting at most newFlowers flowers.
'''

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers = sorted(min(target, x) for x in flowers)
        prefix = [0]
        ii = -1 
        for i in range(len(flowers)): 
            if flowers[i] < target: ii = i 
            if i: prefix.append(prefix[-1] + (flowers[i]-flowers[i-1])*i)
        ans = 0 
        for k in range(len(flowers)+1): 
            if k: newFlowers -= target - flowers[-k]
            if newFlowers >= 0: 
                while 0 <= ii and (ii+k >= len(flowers) or prefix[ii] > newFlowers): ii -= 1
                if 0 <= ii: kk = min(target-1, flowers[ii] + (newFlowers - prefix[ii])//(ii+1))
                else: kk = 0 
                ans = max(ans, k*full + kk*partial)
        return ans 
