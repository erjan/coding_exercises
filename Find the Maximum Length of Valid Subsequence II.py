'''
You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.
'''

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        max_len = 0
        for val in range(k):
            dp = [0] * k
            for num in nums:
                rem = num % k
                need = (val - rem + k) % k
                new_len = dp[need] + 1
                dp[rem] = max(dp[rem], new_len)
                max_len = max(max_len, dp[rem])
        return max_len if max_len >= 2 else 0
