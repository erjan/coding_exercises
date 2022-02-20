'''
You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.
Return the final value of original.
'''

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        def helper(nums, original):
            c = nums.count(original)
            if c!= 0:
                i = nums.index(original)
                return helper(nums,original*2)
            return original

        return helper(nums, original)
       
    
