'''
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.
'''


------------------
#this is not my solution - just copied it
from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_window = SortedList()  # To maintain the current window's sorted elements
        start = 0
        total_subarrays = 0
        
        for end in range(n):
            # Add the current element to the sorted window
            sorted_window.add(nums[end])
            
            # Ensure the window is valid
            while sorted_window[-1] - sorted_window[0] > 2:
                # Remove the leftmost element from the window
                sorted_window.remove(nums[start])
                start += 1
            
            # Count valid subarrays ending at 'end'
            total_subarrays += end - start + 1
        
        return total_subarrays
