'''
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose 
elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
'''

class Solution:
	def checkSubarraySum(self, nums: List[int], k: int) -> bool:
		# Optimal Approach - Time and Space: O(n), O(n)
		res = {0: -1}
		prefSum = 0
		for i in range(len(nums)):
			prefSum += nums[i]
			rem = prefSum % k
			if rem in res:
				if i-res[rem] > 1:
					return True
			else:
				res[rem] = i
		return False
