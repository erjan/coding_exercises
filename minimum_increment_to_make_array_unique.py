'''
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.
'''

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                # this is the case for making item unique
                diff = nums[i-1] + 1 - nums[i]
                ans += diff
                nums[i] = nums[i-1] + 1
        return ans
      
------------------------------------------------------------
def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            pre = nums[i-1]
            cur = nums[i]
            if pre >= cur:
                res += pre-cur+1 # recording the no of changes
                nums[i] = pre + 1 # increasing the (i-1)th value by 1 and assigning it to ith value
        return res
