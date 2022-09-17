'''
You are given two positive integers startPos and endPos. Initially, you are standing at position startPos on an infinite number line. With one step, you can move either one position to the left, or one position to the right.

Given a positive integer k, return the number of different ways to reach the position endPos starting from startPos, such that you perform exactly k steps. Since the answer may be very large, return it modulo 109 + 7.

Two ways are considered different if the order of the steps made is not exactly the same.

Note that the number line includes negative integers.
'''

Explanation
Two sufficient and necessary conditions from a to b with k steps:

abs(a - b) <= k
(a - b - k) % 2 == 0
Otherwice no ways, directly return 0.

Now two eqations
left + right = k
right - left = b - a

So we can have right = (b - a + k) / 2.
The combinations is to pick right steps from k steps to go right.
return result combination(k, right)

  def numberOfWays(self, a, b, k):
        if (a - b - k) % 2: return 0
        return comb(k, (b - a + k) // 2) % (10 ** 9 + 7)
