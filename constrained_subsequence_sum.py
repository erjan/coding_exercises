
'''
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.
'''


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        for i, v in enumerate(nums):
            if len(q): 
                nums[i] += nums[q[0]]
            if q and i - q[0] >= k:
                q.popleft()
            if nums[i] > 0:
                while q and nums[q[-1]] <= nums[i]:
                    q.pop()
                q.append(i)
        return max(nums)
                
---------------------------------------------------------------------------------------------------
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = nums[:1]
        decrease = collections.deque(dp)
        for i, x in enumerate(nums[1:], 1):
            if i > k and decrease[0] == dp[i - k - 1]:
                decrease.popleft()
            tmp = max(x, decrease[0] + x)
            dp += tmp,
            while decrease and decrease[-1] < tmp:
                decrease.pop()
            decrease += tmp,                
        return max(dp)  
