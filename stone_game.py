'''
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.
'''

class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @cache
        def dfs(i, j):
            if i == j:
                return nums[i]

            pick_left = nums[i] - dfs(i+1, j)
            pick_right = nums[j] - dfs(i, j-1)
            
            return max(pick_left, pick_right)
        
        return dfs(0, n-1) >= 0
