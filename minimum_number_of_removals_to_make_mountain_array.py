'''
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.
'''

# Time: O(n^2)
# Space: O(n)
class Solution:
	def minimumMountainRemovals(self, nums: List[int]) -> int:
		n = len(nums)

		if n <= 3:  # 3 <= nums.length <= 1000, it's given!
			return 0

		inc = [0]*n
		dec = [0]*n

		# Longest Increasing Subsequence
		for i in range(n):
			maX = 0
			for j in range(i+1):
				if nums[j] < nums[i]:
					if inc[j] > maX:
						maX = inc[j]
			inc[i] = maX+1

		# Longest Decreasing Subsequence
		for i in range(n)[::-1]:
			maX = 0
			for j in range(n-1, i, -1):
				if nums[j] < nums[i]:
					if dec[j] > maX:
						maX = dec[j]
			dec[i] = maX+1

		# Result
		res = 0
		for i in range(0, n):
			if inc[i] > 1 and dec[i] > 1:
				res = max(res, (inc[i] + dec[i])-2)
		return n - res - 1
  
------------------------------------------------------------------------
class Solution:
	def minimumMountainRemovals(self, lst: List[int]) -> int:
		l = len(lst)
		dp = [0] * l
		dp1 = [0] * l

		for i in range(l):   # for increasing subsequence
			maxi = 0
			for j in range(i):
				if lst[i] > lst[j]:
					if dp[j] > maxi:
						maxi = dp[j]

			dp[i] = maxi + 1

		for i in range(l - 1, -1, -1):  # for decreasing subsequence
			maxi1 = 0
			for j in range(l - 1, i, -1):
				if lst[i] > lst[j]:
					if dp1[j] > maxi1:
						maxi1 = dp1[j]

			dp1[i] = maxi1 + 1

		ans = 0
		for i in range(l):
			if dp[i] > 1 and dp1[i] > 1:
				temp = dp[i] + dp1[i] - 1
				if temp > ans:
					ans = temp

		return l - ans
