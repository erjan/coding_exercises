'''
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones in a pile. On each player's turn, they can remove a stone from the pile and receive points based on the stone's value. Alice and Bob may value the stones differently.

You are given two integer arrays of length n, aliceValues and bobValues. Each aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively, value the ith stone.

The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play optimally. Both players know the other's values.

Determine the result of the game, and:

If Alice wins, return 1.
If Bob wins, return -1.
If the game results in a draw, return 0.
'''



class Solution:
    def stoneGameVI(self, alice: List[int], bob: List[int]) -> int:
        t=list(zip(alice,bob))
        t=sorted(t,key=lambda x: sum(x),reverse=True)
        al=sum([i[0] for i in t[::2]])
        bb=sum([i[1] for i in t[1::2]])
        if al>bb:
            return 1
        elif al<bb:
            return -1
        return 0
      
------------------------------------------------------------------------
 def stoneGameVI(self, A, B):
        return cmp(-sum(B) + sum(sorted(a + b for a,b in zip(A,B))[::-2]), 0)
