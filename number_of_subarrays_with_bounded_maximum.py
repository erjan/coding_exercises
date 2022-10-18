'''
Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.
'''

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        end,start=-1,-1
        result=0
        for i in range(len(nums)):  
            if nums[i]>=left and nums[i]<=right:
                end=i
                result+=end-start
            elif nums[i]>right:
                start,end=i,i
            else:
                result+=end-start
                
        return result
      
-------------------------------------------------------------

class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:

        # Initialize the length of nums, the left pointer, the length of valid previous substring, and result
        n, l, valid, res = len(nums), 0, 0, 0

        # Use the right pointer to iterate through all numbers
        for r in range(0, n):

            # If the current number falls between the range, update the length of valid previous substring
            if left <= nums[r] <= right:
                valid = r - l + 1

            # If the current number is greater than the range, reset the left pointer and the length of valid previous substring
            if nums[r] > right:
                l = r + 1
                valid = 0

            # Add the length of valid previous substring to the result
            res += valid

        return res
