'''
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.
'''

class Solution:
    @functools.lru_cache(None)
    def helper(self, idx, hold):
        if idx == len(self.nums):
            return 0, 1
        elif hold is None or hold < self.nums[idx]:
            # take
            length1, times1 = self.helper(idx+1, self.nums[idx])
            length1 += 1
            
            # not take
            length2, times2 = self.helper(idx+1, hold)
            
            # if both take and not take are same length, pick both
            # otherwise, pick the longer LIS one
            if length1 == length2:
                return length2, times1 + times2
            elif length1 > length2:
                return length1, times1
            else:
                return length2, times2
        else:
            return self.helper(idx+1, hold)
    
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0  # special case, no LIS
        self.nums = nums
        return self.helper(0, None)[1]
      
------------------------------------------------------------------------------
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        m, dp, cnt = 0, [1] * n, [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j]+1: dp[i], cnt[i] = dp[j]+1, cnt[j]
                    elif dp[i] == dp[j]+1: cnt[i] += cnt[j]
            m = max(m, dp[i])                        
        return sum(c for l, c in zip(dp, cnt) if l == m)
