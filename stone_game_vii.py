'''
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.
'''

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        
        prefix = [0]
        for i in stones:
            prefix.append(prefix[-1]+i)
        
        def solve(left, right):
            if left == right:
                return 0
            
            leftScore = prefix[right+1] - prefix[left+1] - solve(left+1,right)
            rightScore = prefix[right] - prefix[left] - solve(left,right-1)
            return max(leftScore,rightScore)
        
        return solve(0,n-1)
      
---------------------------------------------------

class Solution:
    def stoneGameVII(self, S: List[int]) -> int:
        N, dp = len(S), [0] * len(S)
        for i in range(N - 2, -1, -1):
            total = S[i]
            for j in range(i + 1, N):
                total += S[j]
                dp[j] = max(total - S[i] - dp[j], total - S[j] - dp[j-1])
        return dp[-1]
