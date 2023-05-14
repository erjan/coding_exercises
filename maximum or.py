'''
You are given a 0-indexed integer array nums of length n and an integer k. In an operation, you can choose an element and multiply it by 2.

Return the maximum possible value of nums[0] | nums[1] | ... | nums[n - 1] that can be obtained after applying the operation on nums at most k times.

Note that a | b denotes the bitwise or between two integers a and b.
'''


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        cur = 0
        saved = 0
        for num in nums:
            saved |= num & cur
            cur |= num
        
        max_num = 0
        
        for num in nums:
            max_num = max(max_num, saved | (cur & ~num) | num << k)
        return max_num
        
