'''
There are some prizes on the X-axis. You are given an integer array prizePositions that is sorted in non-decreasing order, where prizePositions[i] is the position of the ith prize. There could be different prizes at the same position on the line. You are also given an integer k.

You are allowed to select two segments with integer endpoints. The length of each segment must be k. You will collect all prizes whose position falls within at least one of the two selected segments (including the endpoints of the segments). The two selected segments may intersect.

For example if k = 2, you can choose segments [1, 3] and [2, 4], and you will win any prize i that satisfies 1 <= prizePositions[i] <= 3 or 2 <= prizePositions[i] <= 4.
Return the maximum number of prizes you can win if you choose the two segments optimally.

 '''


'''
Let's iterate through the array and for each position, calculate the count of prizes in the interval if the interval ends at the current position and store the count and the position in the "intervals" list.

intervals = [(count of prizes, end pos), (count of prizes, end pos)]
Let's also store the interval which covers the maximum count of prizes that ends before some position, the "max stack for the intervals," in the "max_before".

max_before = [(max count of prizes, end pos1), (max count of prizes, end pos2)]
end pos1 <= end pos2 <= end pos3 <= end pos4 ....
count1 <= count2 <= count3 <= count4 ...
The solution is then straightforward and is based on two key ideas:

If we have two intervals, we can make them non-intersecting by moving the first of them, as the second will cover the same prizes. So we need only consider the non-intersecting intervals.

The solution must have the last interval. To find the solution, we pop intervals from the "intervals" list one by one and calculate the solution if the current interval is the last one. Then, find the maximum among these solutions.

To implement this, we pop the next interval from the "intervals" list - the current last interval.
Then, pop all intervals from the "max_before" list that do not end before the current interval.
The top of the "max_before" list will then have the interval with the maximum prize count before the current interval.
The current best candidate solution for the current last interval is the count of prizes for the current last interval plus the top of the "max_before" interval.

candidate = count+(0 if not max_beffore else max_beffore[-1][0])
'''


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        # count of prizes for all intervals
        # (count, end position of interval)        
        intervals = []
        # max stack of intervals
        # (count, end position of interval),
        # There can't be interval with bigger count before the interval
        max_beffore = []
        start_inx = 0 # start index of the current interval
        count = 0 # count of the current interval
        for inx, pos in enumerate(prizePositions):
            count += 1
            # subtract prizes from the current interval if they are not covered by the interval
            while pos-k > prizePositions[start_inx]:
                count -= 1
                start_inx += 1
            intervals.append((count, pos))
            if not max_beffore or max_beffore[-1][0] < count:
                max_beffore.append((count, pos))

        max_solution = 0
        while intervals:
            # the last interval for the current solution
            count, pos = intervals.pop()
            # max_beffore stores only intervals before the last interval,
            # max_beffore is a max stack,
            # so the top of the max possible has the max count among all values in the max_beffore
            while max_beffore and max_beffore[-1][1] >= pos-k:
                max_beffore.pop()
            # The soluthon if the current last interval is the last
            candidate = count+(0 if not max_beffore else max_beffore[-1][0])
            # we need to find maximum among all candidates
            max_solution = max(candidate, max_solution)
        return max_solution
            
