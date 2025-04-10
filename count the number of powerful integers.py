'''
You are given three integers start, finish, and limit. You are also given a 0-indexed string s representing a positive integer.

A positive integer x is called powerful if it ends with s (in other words, s is a suffix of x) and each digit in x is at most limit.

Return the total number of powerful integers in the range [start..finish].

A string x is a suffix of a string y if and only if x is a substring of y that starts from some index (including 0) in y and extends to the index y.length - 1. For example, 25 is a suffix of 5125 whereas 512 is not.
'''

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(val: int) -> int:
            chakra = str(val)  # Chakra flow string
            n = len(chakra) - len(s)  # How much room left for chakra prefix

            if n < 0:
                return 0  # Not enough space to include suffix

            # dp[i][tight] = number of valid chakra flows from index i
            dp = [[0] * 2 for _ in range(n + 1)]

            # Base case: formed entire prefix, check suffix compatibility
            dp[n][0] = 1
            dp[n][1] = int(chakra[n:] >= s)

            # Fill DP table from back to front
            for i in range(n - 1, -1, -1):
                digit = int(chakra[i])

                # Not tight → any digit from 0 to limit
                dp[i][0] = (limit + 1) * dp[i + 1][0]

                # Tight case → we must respect current digit
                if digit <= limit:
                    dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]
                else:
                    dp[i][1] = (limit + 1) * dp[i + 1][0]

            return dp[0][1]

        return count(finish) - count(start - 1)
