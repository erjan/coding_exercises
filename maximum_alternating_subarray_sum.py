'''
A subarray of a 0-indexed integer array is a contiguous non-empty sequence of elements within an array.

The alternating subarray sum of a subarray that ranges from index i to j (inclusive, 0 <= i <= j < nums.length) is nums[i] - nums[i+1] + nums[i+2] - ... +/- nums[j].

Given a 0-indexed integer array nums, return the maximum alternating subarray sum of any subarray of nums.
'''


Kadane's Algorithm Variance
This problem is a variance of the maximum sum of subarrays problem, which is resolved using Kadane's Algorithm (DP). If you are not familiar with this solution/problem, you should search for it and take a look since it's calssic and quite common seen problem during interviews. Probably you won't be able to see it on interviews because of the popluarity.

We just need tweak the Kadane approach to calcuate the alternative sum instead.
In Kadane alrogithm, we compare the current maximum sum with the current num num.

curr = max(curr + num, num)
max_sum = max(max_sum, curr)
However, in this case, we can't simply increase the curr with current num, but need to separate it to pos and nes respectively. pos means the maximum sum of subarrays ending up at num with + as the last operation. Similar with it, nes means the maximum sum of subarrays ending up at num with - as the last operation.

This is because each num can be added to previous nes to constrcut pos, or subtracted from previous pos to construct nes.
Then similar with kadane algorihtm, each num can also be the start of new subarrays for pos, not nes. Why is it not possible to be start of subarrays for nes?
Then there is only one chance for us to update nes which is to subtract from pos.

As such, the transition formula can be changed to

pos, nes = max(nes + num, num), pos - num
max_sum = max(max_sum, pos, nes)
Finally, we can simply write up the solution as

def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
	max_sum = pos = nes = float('-inf')
    for i, num in enumerate(nums):
		pos, nes = max(nes + num, num), pos - num
        max_sum = max(max_sum, pos, nes)
	return max_sum
Time Complexity= O(N)
Space Complexity= O(1)

------------------------------------------------------------------------------------------


class Solution(object):
    def maximumAlternatingSubarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        arr1 = [nums[i] if i%2 else -nums[i] for i in range(len(nums))]
        globalMax1 = float('-inf')
        localMax = 0
        for i in range(1, len(arr1)):
            if localMax < 0 and i%2 != 0:
                localMax = 0
            localMax += arr1[i]
            if localMax > globalMax1:
                globalMax1 = localMax
                
        arr2 = [nums[i] if i%2==0 else -nums[i] for i in range(len(nums))]
        globalMax2 = float('-inf')
        localMax = 0
        for i in range(len(arr2)):
            if localMax < 0 and i%2 == 0:
                localMax = 0
            localMax += arr2[i]
            if localMax > globalMax2:
                globalMax2 = localMax
  
        return max(globalMax1, globalMax2)
  ----------------------------------------------------------------------------------------
  
  class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        cur = nums[0]
        cur2 = 0
        for i in range(1, n):
            cur += -nums[i] if i % 2 else nums[i]
            cur2 -= -nums[i] if i % 2 else nums[i]
            res = max(res, cur, cur2)
            if cur < 0:
                cur = 0 if i % 2 else nums[i]
            if cur2 < 0:
                cur2 = nums[i] if i % 2 else 0
        return res
---------------------------------------------------------------

class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        last_neg = 0; last_pos = nums[0]; res = nums[0]
        
        for num in nums[1:]:
            curr_neg = last_pos - num
            curr_pos = max(last_neg + num, num)
            res = max(res, curr_neg, curr_pos)
            last_neg, last_pos = curr_neg, curr_pos
        
        return res
      
----------------------------------------

dp0: max sum before current nums[i] and previous operation is plus nums[i - 1]
dp1: max sum before current nums[i] and previous operation is minus nums[i - 1]

dp0 could be updated by nums[i] or dp1 + nums[i]
dp1 can only be updated by dp0 - nums[i]

class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        dp0, dp1, res = nums[0], 0, nums[0]
        for n in nums[1:]:
            dp0, dp1 = max(n, dp1 + n), dp0 - n
            res = max(res, dp0, dp1)
        return res
``
-----------------------------------------------------------------------

      
  
