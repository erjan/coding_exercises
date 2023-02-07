'''
There is a regular convex polygon with n vertices. The vertices are labeled from 0 to n - 1 in a clockwise
direction, and each vertex has exactly 
one monkey. The following figure shows a convex polygon of 6 vertices.


Each monkey moves simultaneously to a neighboring vertex. A neighboring vertex for a vertex i can be:

the vertex (i + 1) % n in the clockwise direction, or
the vertex (i - 1 + n) % n in the counter-clockwise direction.
A collision happens if at least two monkeys reside on the same vertex after the movement or intersect on an edge.

Return the number of ways the monkeys can move so that at least 
one collision happens. Since the answer may be very large, return it modulo 109 + 7.

Note that each monkey can only move once.
'''

'''
Intuition
Each monkey can move to left or right, So there are 2 possible ways a single monkey can move. For n number of monkeys there are 2 ^ n possibilities. Out of which only 2 possible ways where no monkey can collide when all of them move to either left or right.
Therefore, ans = 2 ^ n - 2

Complexity
Time complexity: O(pow(2,n))O(pow(2, n))O(pow(2,n))
Space complexity: O(1)O(1)O(1)
Code
'''


class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return (pow(2, n, mod) + mod - 2) % mod
