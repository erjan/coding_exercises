'''
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.

Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.

Since the answer may be very large, return it modulo 109 + 7.
'''


class Solution:
    MOD = 10**9 + 7

    def possibleStringCount(self, word: str, k: int) -> int:
        if not word:
            return 0

        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        total = 1
        for num in groups:
            total = (total * num) % self.MOD

        if k <= len(groups):
            return total

        dp = [0] * k
        dp[0] = 1

        for num in groups:
            new_dp = [0] * k
            sum_val = 0
            for s in range(k):
                if s > 0:
                    sum_val = (sum_val + dp[s - 1]) % self.MOD
                if s > num:
                    sum_val = (sum_val - dp[s - num - 1] + self.MOD) % self.MOD
                new_dp[s] = sum_val
            dp = new_dp

        invalid = sum(dp[len(groups):k]) % self.MOD
        return (total - invalid + self.MOD) % self.MOD
