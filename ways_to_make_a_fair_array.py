'''
You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.

For example, if nums = [6,1,7,4,1]:

Choosing to remove index 1 results in nums = [6,7,4,1].
Choosing to remove index 2 results in nums = [6,1,4,1].
Choosing to remove index 4 results in nums = [6,1,7,4].
An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

Return the number of indices that you could choose such that after the removal, nums is fair.
'''


class Solution:
	def waysToMakeFair(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return 1

		if len(nums) == 2:
			return 0

		prefixEven = sum(nums[2::2])
		prefixOdd = sum(nums[1::2])
		result = 0

		if prefixEven == prefixOdd and len(set(nums)) == 1:
			result += 1

		for i in range(1,len(nums)):
			if i == 1:
				prefixOdd, prefixEven = prefixEven, prefixOdd 

			if i > 1:
				if i % 2 == 0:
					prefixEven -= nums[i-1]
					prefixEven += nums[i-2]

				else:
					prefixOdd -= nums[i-1]
					prefixOdd += nums[i-2]

			if prefixOdd == prefixEven:
				result += 1

		return result
  ------------------------------------------------------------------------------------------------------------
  def waysToMakeFair(self, nums: List[int]) -> int:
    even, odd = [0], [0]
    for i in range(len(nums)):
      if(i % 2):
        odd.append(odd[-1] + nums[i])
        even.append(even[-1])
      else:
        even.append(even[-1] + nums[i])
        odd.append(odd[-1])
    ans = 0
    for i in range(1, len(nums)+1):
      e_l, o_l = even[i-1], odd[i-1]
      e_r, o_r = even[-1]-even[i], odd[-1]-odd[i]
      if(e_l + o_r == e_r + o_l):
        ans += 1
    return ans
