'''
You are playing a variation of the game Zuma.

In this variation of Zuma, there is a single row of colored balls on a board, where each ball can be colored red 'R', yellow 'Y', blue 'B', green 'G', or white 'W'. You also have several colored balls in your hand.

Your goal is to clear all of the balls from the board. On each turn:

Pick any ball from your hand and insert it in between two balls in the row or on either end of the row.
If there is a group of three or more consecutive balls of the same color, remove the group of balls from the board.
If this removal causes more groups of three or more of the same color to form, then continue removing each group until there are none left.
If there are no more balls on the board, then you win the game.
Repeat this process until you either win or do not have any more balls in your hand.
Given a string board, representing the row of balls on the board, and a string hand, representing the balls in your hand, return the minimum number of balls you have to insert to clear all the balls from the board. If you cannot clear all the balls from the board using the balls in your hand, return -1.
'''

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = ''.join(sorted(hand))
        
        @cache
        def fn(board, hand):
            """Return min number of balls to insert."""
            if not board: return 0
            if not hand: return inf 
            ans = inf 
            for i, ch in enumerate(hand): 
                if i == 0 or hand[i-1] != ch: # pruning 1
                    hh = hand[:i] + hand[i+1:]
                    for j in range(0, len(board)): 
                        if ch == board[j] or j and board[j-1] == board[j]: # pruning 2
                            bb, nn = "", board[:j] + ch + board[j:]
                            while bb != nn:
                                bb, nn = nn, ""
                                for k, grp in groupby(bb): 
                                    x = len(list(grp))
                                    if x < 3: nn += k*x
                            ans = min(ans, 1 + fn(bb, hh))
            return ans 
        
        return (lambda x: x if x < inf else -1)(fn(board, hand))
