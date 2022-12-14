'''
Given a sorted integer array nums and an integer n, add/patch elements to the array 
such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.
'''

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res, N, reach, i = 0, len(nums), 0, 0
        while reach < n: # if didn't reach n
            if i < N and nums[i] <= reach + 1: # no need to add
                reach += nums[i]
                i += 1
            else: # need to add, the nums are sorted, means others numbers after this one is not possible
                res += 1
                reach += reach + 1
        return res
      
---------------------------------------------------------------------
class Solution:
	def minPatches(self, nums: List[int], n: int) -> int:
		ans, total = 0, 0
		num_idx = 0
		while total < n:
			if num_idx < len(nums):
				if total < nums[num_idx] - 1:
					total = total * 2 + 1
					ans += 1
				else:
					total += nums[num_idx]
					num_idx += 1
			else:
				total = total * 2 + 1
				ans += 1
		return ans
  
----------------------------------------------------------------------------------
