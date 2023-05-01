'''
You are given two 0-indexed integer arrays player1 and player2, that represent the number of pins that player 1 and player 2 hit in a bowling game, respectively.

The bowling game consists of n turns, and the number of pins in each turn is exactly 10.

Assume a player hit xi pins in the ith turn. The value of the ith turn for the player is:

2xi if the player hit 10 pins in any of the previous two turns.
Otherwise, It is xi.
The score of the player is the sum of the values of their n turns.

Return

1 if the score of player 1 is more than the score of player 2,
2 if the score of player 2 is more than the score of player 1, and
0 in case of a draw.
'''


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        

        score1 = 0
        score2 = 0

        n = len(player1)

        for i in range(n):
            score1 += player1[i]
            score2 += player2[i]

        if n>1:

            for i in range(1,n):

                if player1[i-1] == 10 or (i>=2  and player1[i-2] ==10):
                    score1 += player1[i]
                if player2[i-1] == 10 or (i>=2 and player2[i-2] == 10):
                    score2+= player2[i]


            
        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        elif score1 == score2:
            return 0






