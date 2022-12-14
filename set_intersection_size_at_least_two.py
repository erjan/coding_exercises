'''
You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.
'''

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        size = 0
        prev_start = -1
        prev_end = -1

        for curr_start, curr_end in intervals:
            if prev_start == -1 or prev_end < curr_start: #if intervals do not overlap
                size += 2
                prev_start = curr_end-1
                prev_end = curr_end

            elif prev_start < curr_start: #if intervals overlap
                if prev_end != curr_end:
                    prev_start = prev_end
                    prev_end = curr_end
                    
                else:
                    prev_start = curr_end-1
                    prev_end = curr_end

                size += 1

        return size
---------------------------------------------------------------------------------------------------------------------------
class Solution:
    def intersectionSizeTwo(self, intervals):
        # make a equivalent simpliest intervals
        itvls = []
        for itvl in sorted(intervals, key=lambda e: (e[0], -e[1])):
            while itvls and itvls[-1][1] >= itvl[1]:
                itvls.pop()
            itvls.append(itvl)

        # greedily choose right most number from each interval to form nums
        # according to two most possible number to fulfill current interval in nums
        # we can determine how much shortage current interval needs
        nums = []
        for l, r in itvls:
            lack = 2
            if nums: lack -= (l <= nums[-2] <= r) + (l <= nums[-1] <= r)

            for i in range(lack): nums.append(r - i)

        return len(nums)
        
