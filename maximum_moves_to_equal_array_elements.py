'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

'''

class Solution:
	def minMoves(self, nums: List[int]) -> int:
		_sum, _min = 0, float('inf')
		for num in nums:
			_sum += num
			_min = _min if _min < num else num
		return _sum-_min*len(nums)
  
--------------------------------------------------------
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        num_count = len(nums)
        min_num = min(nums)
        sum_nums = sum(nums)
        move_count = sum_nums - min_num*num_count
        
        return move_count
