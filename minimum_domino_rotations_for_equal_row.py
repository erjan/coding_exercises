'''
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.
'''


from typing import List
from collections import Counter


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Basic idea is to find the most common number in both the top and bottom rows. If all dominoes contain
        that most common number at least once then return the smallest number of spaces out of the top or bottom row which will
        be the fewest number of rotations we need to do.
        """
        value, count = Counter(tops + bottoms).most_common()[0]
        for t, b in zip(tops, bottoms):
            if t != value and b != value:
                # if neither the top or bottom of a single domino contain the most common element
				# then the target condition can never be achieved
                return -1
        if count >= len(tops):
            return min([len(tops) - tops.count(value), len(bottoms) - bottoms.count(value)])
        return -1
