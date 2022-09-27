'''
You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
Remove x from nums.
Return the maximum score after performing m operations.
'''

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        s=0
        n=len(nums)
        m=len(multipliers)
        dp=[[0]*(m+1) for i in range(m+1)]
        for j in range(m-1, -1, -1):
            for low in range(j, -1, -1):
                first=nums[low]*multipliers[j]+dp[j+1][low+1]
                last=nums[n-1-(j-low)]*multipliers[j]+dp[j+1][low]
                dp[j][low]=max(first, last)
        return dp[0][0]
