'''
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.
'''

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            while dp and dp[0][1] + k < i:
                dp.popleft()
            cost = nums[i] + dp[0][0]
            while dp and cost >= dp[-1][0]:
                dp.pop()
            dp.append((cost, i))
        return dp[-1][0]
