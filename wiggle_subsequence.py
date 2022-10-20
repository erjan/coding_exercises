'''
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.
'''

'''
Idea:
The key realization here is that any number that lies in the middle of a stretch of the same direction is extraneous, because the more extreme numbers are the better choices to keep, as they allow for a larger likelihood that a subsequent number will be a directional change.

So the simple answer here is to count the inflection points in our input array (N) where the direction changes. There are several ways to do this, but in this solution, we can keep a directional flag (up) to keep track of the current direction and then increment our answer (ans) and invert up when a change is found.

One tricky thing lies in setting the initial direction. Per the instructions, the first number can represent any direction, so we'll have to wait until the first time we see a different number to set our direction. We can check this with a simple while loop before the main loop.
'''

class Solution:
    def wiggleMaxLength(self, N: List[int]) -> int:
        lenN, i = len(N), 1
        while i < lenN and N[i] == N[i-1]: i += 1
        if i == lenN: return 1
        up, ans = N[i-1] > N[i], 1
        while i < lenN:
            if (up and N[i] < N[i-1]) or (not up and N[i] > N[i-1]):
                up = not up
                ans += 1
            i += 1
        return ans
      
-------------------------------------------------------------------------------------      
