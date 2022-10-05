'''
You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.
'''


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            if sum([(n - 1) // mid for n in nums]) > maxOperations: 
                l = mid + 1
            else:
                r = mid
        return l
      
---------------------------------------------------------------------------------------
Given a threshold t (max number of balls per final bag), we need at least ceil(n / t) of bags to split n balls. The required operations is then ceil(n / t) - 1. For example a bag of n = 10 balls and threshold t = 4, we need to split them into (4, 4, 2) 3 bags, which requires 2 split operations.
Binary search on the threshold which takes O(logM) time, where M is the maximum number of balls in each bags. Checking if a certain threshold is feasible take O(N) for N bags. Together, the time complexity is O(N log M).

from math import ceil
def minimumSize(self, nums: List[int], maxOperations: int) -> int:
	def required(n, t):
	    """ Required N of operations to split a bag with n balls into bags 
			each with fewer than or equals to t balls
		"""
		return int(ceil(n / t)) - 1
	def possible(t):
	    """ Is it possible to have less than t balls per bag with maxOperations? """
		if t <= 0:
			return False
		sum_req = 0
		for x in nums:
			sum_req += required(x, t)
			if sum_req > maxOperations:
				return False
		return True

	nums = sorted(nums, reverse=True)
	r = nums[0]  # known minimum possible threshold
	l = 0        # known maximum impossible threshold
	while r - l > 1:
		mid = (r + l) // 2
		if possible(mid):
			r = mid
		else:
			l = mid
	return r
