'''
You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.

Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
'''



    def partitionArray(self, A, k):
        A.sort()
        res, j = 1, 0
        for i in range(len(A)):
             if A[i] - A[j] > k:
                res += 1
                j = i
        return res
      
------------------------------------------------------------------------------------------

    def partitionArray(self, A, k):
        A.sort()
        res = 1
        mn = mx = A[0]
        for a in A:
            mn = min(mn, a)
            mx = max(mx, a)
            if mx - mn > k:
                res += 1
                mn = mx = a
        return res
      
-----------------------------------------------------------------------------------------------------------------
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
		# To keep track of starting element of each subsequence
        start = nums[0]
        
        for i in range(1, len(nums)):
            diff = nums[i] - start
            if diff > k:
				# If difference of starting and current element of subsequence is greater
				# than K, then only start new subsequence
                ans += 1
                start = nums[i]
        
        return ans
      
      
