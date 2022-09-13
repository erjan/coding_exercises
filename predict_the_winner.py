'''
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.
'''


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i, num in enumerate(nums):
            dp[i][i] = num
        
        for start in reversed(range(n)):
            for end in range(start+1, n):
                max_end = nums[end] - dp[start][end-1]      # pick the last number
                max_start = nums[start] - dp[start+1][end]  # pick the first number
                dp[start][end] = max(max_end,max_start)
        return dp[0][-1] >= 0
