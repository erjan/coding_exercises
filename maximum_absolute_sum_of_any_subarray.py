'''
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
'''


Our target is to find the maximum/minimum subarray sum and choose maximum absolute value between them.
This situation is suited for adopting Kadane's algorithm.


class Solution:
	def maxAbsoluteSum(self, A):

		ma,mi,res = 0,0,0
		for a in A:
			ma = max(0,ma+a)
			mi = min(0,mi+a)
			res = max(res,ma,-mi)
		return res
  
  
  
----------------------------------------------------------------------------------------------------------------------
Use of one kadane's algorithm to compute max absolute sum and anothe kadane's to compute min absolute sum, return max comparing both

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum = nums[0]
        curr_min = nums[0]
        
        max_sum = nums[0]
        curr_max = max_sum
        
        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(curr_max, max_sum)
        
        for i in range(1, len(nums)):
            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(curr_min, min_sum)
        
        return max(abs(max_sum), abs(min_sum))
