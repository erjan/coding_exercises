'''
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        val = max(nums)
        count = ans = 1
        j = 1
        
        while j < len(nums):
            if nums[j] == val and nums[j - 1] == val:
                count += 1
                ans = max(ans, count)
            elif nums[j] == val:
                count = 1
            else:
                count = 0
            j += 1
        
        return ans
      
-------------------------------------------------------------------------------------------
class Solution:     # The problem reduces to finding the longest subarray with only 
                    # elements = max(nums). So here's the plan:
                    #  1) Determine max(nums).
                    #  2) Iterate through nums and keep track of the lengths of such 
                    #     max subarrays. 
                    #  3) When a max subarray ends, update the max length. 
                    #  4) Return the max length of those subarrays. (Note the
                    #     last update in the return)
    def longestSubarray(self, nums: List[int]) -> int:

        ans, tally, mx = 0, 0, max(nums)            # <-- 1)

        for n in nums:
            if n == mx: tally += 1                  # <-- 2)
            else: ans, tally = max(ans, tally), 0   # <-- 3)

        return max(ans, tally)                      # <-- 4)
