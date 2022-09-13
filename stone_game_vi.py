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
    
----------------------------------------------------------------------------------------
Intuition
Sort stones by their sum value for Alice and Bob.
If a stone is super valued for Alice, Alice wants to take it.
If a stone is super valued for Bob, Alice also wants to take it.
Because she doesn't want Bob to take it.


Explanation
Here is more convinced explanation.
Assume a stone valued [a,b] for Alice and Bod.
Alice takes it, worth a for Alice,
Bob takes it, worth b for Bob,
we can also consider that it worth -b for Alice.
The difference will be a+b.
That's the reason why we need to sort based on a+b.
And Alice and Bob will take one most valued stone each turn.
----------------------------------------------------------------------
 def stoneGameVI(self, A, B):
        A = sorted(zip(A, B), key=sum)
        return cmp(sum(a for a, b in A[::-2]), sum(b for a, b in A[-2::-2]))
