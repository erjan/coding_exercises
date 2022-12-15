'''
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.
'''



'''
The code below takes a very simple approach to this problem, yet it manages to achieve a Top 92% Speed rating.

The algorithm is the following:

We first create explicit watering ranges for each Tap, and sort them. This solves 99% of the problem :)

By looking at the given Diagram, we note that the problem actually consists in watering all the middle points [0.5 , 1.5, ... , n-0.5 ].

Starting from x=0.5 we query all the Tap ranges starting before "x", and find the further reaching Tap. We pick this Tap as our anwer.

If our chosen Tap is unable to water "x", we exit with an error (-1). Otherwise, we move to the point "+0.5" to the right from it.

We repeat the previous steps until we reach "n-0.5".

That's the code, I hope you guys find it helpful. I think I achieved a 
High Speed Rating because, after the sorting step, the code does very few O(n) operations. For n = 10000, the difference between O(n) and O(n log n) is very small. If the operations after the sorting step are simple, the difference can be easily compensated.
'''

class Solution:
    def minTaps(self, n, ranges):
        # Shameless Range conversion
		for i,x in enumerate(ranges):
            ranges[i] = [i-x,i+x]
        # Sorting Step
        ranges.sort(reverse=True) # Reverse, so pop() behaves like popleft()
        # Main Loop
        x, res = 0.5, 0 # Try to water points in the middle
        while x<n:
            b = -1
            while ranges and ranges[-1][0]<=x: 
                # Idea: 1) Query/Pop all points Starting before "x"
                #       2) Pick the one reaching furthest
                #       3) After one fail, points start at x<a (leave for later)
                b = max(b,ranges.pop()[1])
            if b<0 or b<x: # We didn't find anything, or b<x (we never watered "x" at all)
                return -1
            x = b + 0.5
            res += 1
        return res
