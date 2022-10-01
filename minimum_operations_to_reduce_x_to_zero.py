
'''
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
'''

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        curr_sum, max_len = 0, 0
        start_idx = 0
        found = False
        for end_idx in range(len(nums)):
            curr_sum += nums[end_idx]
            while start_idx <= end_idx and curr_sum > target:
                curr_sum -= nums[start_idx]
                start_idx += 1
            if curr_sum == target:
                found = True
                max_len = max(max_len, end_idx - start_idx + 1)

        return len(nums) - max_len if found else -1
      
-----------------------------------------------------------------------------------------------
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        maxLen = total = windowStart = 0
        targetSum = sum(nums)
        
        # edge cases
        if targetSum < x: return -1
        if targetSum == x: return len(nums)
        
        # opposite of sliding window but still do sliding window
        # so instead of find continous subarray,
        # we need to find outer points that is not included in continous subarray
        k = targetSum - x # this is for continous subarray
        
        for windowEnd in range(len(nums)):
            total += nums[windowEnd]
            
            while total > k:
                total -= nums[windowStart]
                windowStart += 1
            
            if total == k:
                maxLen = max(maxLen, windowEnd - windowStart + 1)
    
        
        return len(nums) - maxLen if maxLen != 0 else -1
