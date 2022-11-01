'''
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 109 + 7.
'''

class Solution:
    def kadane(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(max(nums), 0)
    
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        sums = sum(arr)
        mod = 10**9 + 7
        if k == 1:
            return self.kadane(arr) % (mod)
        if sums > 0:
            return (self.kadane(arr+arr) + (k-2)*sums) % (mod)
        else:
            return self.kadane(arr+arr) % (mod)
          
-------------------------------------------------------------------------------------------
class Solution(object):
    def maxSubarray(self, A):
        if not A:
            return 0
        curSum = maxSum = A[0]
        for i in range(1,len(A)):
            curSum = max(A[i], curSum + A[i])
            maxSum = max(curSum, maxSum)
        
        return max(maxSum,0)
        
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arrSum = sum(arr)
        MOD = (10**9 + 7)
        if k == 1:
            return self.maxSubarray(arr)%MOD
        if k == 2:
            return self.maxSubarray(2*arr)%MOD
        if k > 2 and arrSum > 0:
            return (self.maxSubarray(arr+arr) + (k-2)*arrSum)%MOD
        else:
            return self.maxSubarray(2*arr)%MOD
