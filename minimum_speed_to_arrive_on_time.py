'''
You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.
'''

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
		# the speed upper is either the longest train ride: max(dist),
		# or the last train ride divide by 0.01: ceil(dist[-1] / 0.01).
		# notice: "hour will have at most two digits after the decimal point"
        upper = max(max(dist), ceil(dist[-1] / 0.01))
        # 
		# the function to calcute total time consumed
        total = lambda speed: sum(map(lambda x: ceil(x / speed), dist[:-1])) + (dist[-1] / speed)
		# the case of impossible to arrive office on time
        if total(upper) > hour:
            return -1
        # 
		# binary search: find the mimimal among "all" feasible answers
        left, right = 1, upper
        while left < right:            
            mid = left + (right - left) // 2
            if total(mid) > hour:
                left = mid + 1 # should be larger
            else:
                right = mid # should explore a smaller one
        return right
