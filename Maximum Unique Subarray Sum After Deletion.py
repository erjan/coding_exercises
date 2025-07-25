'''
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.
'''

---------------------------
#my own solution:
class Solution:
    def maxSum(self, nums: List[int]) -> int:


        negs = [x for x in nums if x <0]

        if len(negs) == len(nums):
            return max(negs)
        if len(nums) == 1:
            return sum(nums)

        n = len(nums)


        nums = list(set(nums))

        res = sum([x for x in nums if x > 0])
        return res

---------------------------------------------------------------  

class Solution:
    def maxSum(self, nums: List[int]) -> int:


        n = len(nums)
        haspos = False

        for n in nums:
            if n>0:
                haspos= True
                break
    
        if not haspos:
            return max(nums)
        
        seen = set()

        res = 0

        for val in nums:
            if val not in seen and val>=0:
                res += val
                seen.add(val)
        
        return res
        
