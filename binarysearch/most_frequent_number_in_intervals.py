'''

You are given a list of list of integers intervals where each element contains the inclusive interval [start, end].

Return the most frequently occurring number in the intervals. If there are ties, return the smallest number.

solution:
Let's do a line sweep. Running a vertical line from left to right, we encounter OPEN and CLOSE events of the intervals.

First, we find max_active, the largest number of intervals that can be stabbed by a vertical line.

After, the first time that an interval can be stabbed max_active number of times, we return the left-most point of that interval.

*******************************************************
explanation

we need to count the max num of active intervals ever - thru all the intervals, so if [1,4] and [3,5] intersect - the "3" will be repeating itself twice!
so we need to get that max occuring. 
'''


class Solution:
    def solve(self, intervals):
        OPEN, CLOSE = 0, 1

        events = []
        for s, e in intervals:
            events.append([s, OPEN])
            events.append([e, CLOSE])
        events.sort()

        active = max_active = 0
        for x, cmd in events:
            active += 1 if cmd == OPEN else -1
            max_active = max(max_active, active)

        for x, cmd in events:
            active += 1 if cmd == OPEN else -1
            if active == max_active:
                return x

        return 0
