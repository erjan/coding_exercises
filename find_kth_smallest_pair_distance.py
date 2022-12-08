'''
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
'''

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)

        def less(v):
            """number of distances < v"""
            cnt, left = 0, 0
            for right in range(1, N):
                while left < right and nums[right] - nums[left] >= v:
                    left += 1
                cnt += right - left
            return cnt

        lo, hi = 0, max(nums) - min(nums)
        while lo <= hi:
            v = (lo+hi) // 2
            cnt = less(v)
            if cnt < k:
                lo = v + 1
            else:
                hi = v - 1
        return hi
      
---------------------------------------------------------------------------------------
class Solution:
	def smallestDistancePair(self, nums: List[int], k: int) -> int:

		def getPairs(diff):
			l = 0
			count = 0

			for r in range(len(nums)):
				while nums[r] - nums[l] > diff:
					l += 1
				count += r - l

			return count


		nums.sort()
		l, r = 0, nums[-1] - nums[0]

		while l < r:
			mid = (l + r) // 2
			res = getPairs(mid)

			if res >= k:
				r = mid
			else:
				l = mid + 1

		return l
