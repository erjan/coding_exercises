'''
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
'''

my code:
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        st = True
        for i in range(n-1):
            cur = nums[i]
            next= nums[i+1]
            if (cur%2 == 0 and next%2 == 1) or (cur%2 == 1 and next%2 == 0):
                continue
            else:
                st = False
        return st
            

---------------------------------------------------------------------------------------
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i-1] % 2 == nums[i] % 2:
                return False # adjacent nums are both odd or even
        return True # passed check
