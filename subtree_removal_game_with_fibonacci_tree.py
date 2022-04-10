
'''

A Fibonacci tree is a binary tree created using the order function order(n):

order(0) is the empty tree.
order(1) is a binary tree with only one node.
order(n) is a binary tree that consists of a root node with the left subtree as order(n - 2) and the right subtree as order(n - 1).
Alice and Bob are playing a game with a Fibonacci tree with Alice staring first. On each turn, a player selects a node and removes that node and its subtree. The player that is forced to delete root loses.

Given the integer n, return true if Alice wins the game or false if Bob wins, assuming both players play optimally.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

'''

I personally don't like this problem. It should not be in an interview unless its for professional game theory positions.

This game is a special case of Hackenbush game.
According to Colon principle, in this problem:

SG(1) = 1 - 1 = 0
SG(2) = 2 - 1 = 1
SG(n) = (SG(n - 1) + 1) xor (SG(n - 2) + 1)
So we get the solution:

class Solution:
    def findGameWinner(self, n: int) -> bool:
        sg = [None, 0, 1]
        for _ in range(98):
            sg.append((sg[-1] + 1) ^ (sg[-2] + 1))
        return sg[n] != 0
So far, you could already get a full mark, but the solution could be further simplified. If you check the first part of the sg array, you will get [None, 0, 1, 3, 6, 3, 3, 0, 5, 7, 14, 7, 7, 0, 9, 11, 6, 11, 11, 0, 13, ...]. It could be noticed that sg[i] = 0 if and only if i % 6 = 1. This is not a coincidence and we could prove it through mathematical induction.

Suppose sg[t] = 0 and sg[t + 1] is odd. To simply the following writing, let's say sg[t + 1] = x.
We know that sg[t + 2] = (sg[t] + 1) xor (sg[t + 1] + 1) = 1 xor (x + 1). Since x is odd, we could know x + 1 is even. The XOR between an even number and 1 equals to this even number plus 1, so sg[t + 2] = ... = 1 xor (x + 1) = (x + 1) + 1 = x + 2, which is also an odd number.
sg[t + 3] = (sg[t + 1] + 1) xor (sg[t + 2] + 1) = (x + 1) xor (x + 3). Both x + 1 and x + 3 are even (because x is odd), so (x + 1) xor (x + 3) = ((x + 1) / 2 xor (x + 3) / 2) * 2. Let's use y to represent this number. Obviously, y is even and it is not zero.
sg[t + 4] = (sg[t + 2] + 1) xor (sg[t + 3] + 1) = (x + 3) xor (y + 1). Since x + 3 is even and y + 1 is odd, we could know (x + 3) xor (y + 1) = ((x + 3) / 2 xor y / 2) * 2 + 1 = ((x + 3) / 2 xor (((x + 1) / 2 xor (x + 3) / 2)) * 2 + 1 = ((x + 3) / 2 xor (x + 1) / 2 xor (x + 3) / 2) * 2 + 1 = ((x + 1) / 2) * 2 + 1 = x + 1 + 1 = x + 2.
sg[t + 5] = (sg[t + 3] + 1) xor (sg[t + 4] + 1) = (y + 1) xor (x + 3). This is exactly identical to the calculation of sg[t + 4], so it is also x + 2.
sg[t + 6] = (sg[t + 4] + 1) xor (sg[t + 5] + 1) = (x + 2) xor (x + 2) = 0.
sg[t + 7] = (sg[t + 5] + 1) xor (sg[t + 6] + 1) = (x + 3) xor 1. Since x is odd, x + 3 is even, so sg[t + 7] = (x + 3) xor 1 is odd. We can now start a new round starts from t + 6.
Now we have found a loop of length 6. sg[t + i] = 0 if and only if i % 6 = 0. In this problem, we already know that sg[1] = 0 and sg[2] is a odd number, so we could conclude that sg[i] = 0 if and only if i % 6 = 1.

The simplified solution is a one-liner:

class Solution:
    def findGameWinner(self, n: int) -> bool:
        return n % 6 != 1
(The above proving is quite complicated & ugly. I really hope there is a more simple & elegant one :) )
