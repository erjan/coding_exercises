'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:

        return min(nums)
      
-----------------------------------------------------------------------
def findMin(self, nums: List[int]) -> int:
    n = len(nums)

    minimum = nums[0]

    # We can search for the minimum element using Binary Search
    start = 0
    end = n - 1

    while start <= end:
        # If the "start" element is smaller than "end"
        if nums[start] < nums[end]: return min(minimum, nums[start])

        mid = start + (end - start) // 2

        # IF this mid value is smaller than previous minimum we found
        # Then update the minimum
        minimum = min(minimum, nums[mid])

        # If start, end and mid are all same e.g. if [3,3,0,3] is the test case
        # Then, we will simply decrement end pointer
        if nums[start] == nums[mid] == nums[end]: end -= 1
        # Otherwise, we check
        # Is this "mid" value part of left sorted subarray or right sorted subarray?
        # If this is part of the left sorted subarray, we will find minimum on right side
        elif nums[mid] >= nums[start]: start = mid + 1
        # Otherwise, we will find the minimum on the left side
        else: end = mid - 1

    return minimum
