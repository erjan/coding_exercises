'''

Given a two-dimensional integer list intervals of the form [start, end] representing intervals (inclusive), return their intersection, that is, the interval that lies within all of the given intervals.

You can assume that the intersection will be non-empty.

'''


class Solution:
    def solve(self, intervals):


        first = max([item[0] for item in intervals])

        second = min([item[1] for item in intervals])

        return [first,second]
