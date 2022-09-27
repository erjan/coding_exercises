'''
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
'''

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # array which keep count of no of occurences of reminders
        dp = [0]*60
        res = 0
        for t in time:
            rem = t % 60
            target = (60 - rem) % 60
            res += dp[target]
            dp[rem] += 1
        return res
