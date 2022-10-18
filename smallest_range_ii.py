'''
You are given an integer array nums and an integer k.

For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i] + k or nums[i] - k.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after changing the values at each index.
'''

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        mini = A[0]
        maxi = A[-1]
        res = maxi - mini
        for i in range(len(A)-1):
            res = min(res, max(maxi-K, A[i]+K) - min(mini+K, A[i+1]-K))
        return res
      
---------------------------------------------------------------------------------------------------------------------
