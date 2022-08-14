'''
We call a positive integer special if all of its digits are distinct.

Given a positive integer n, return the number of special integers that belong to the interval [1, n].
'''


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @cache
        def dfs(idx, limit, state):
            if idx == len(s):
                return 1
            up = int(s[idx]) if limit else 9
            res = 0
            for digit in range(up + 1):
				# if we have seen this digit before
                if 1 << digit & state:
                    continue
                # leading zeros
                if digit == 0 and state == 0:
                    res += dfs(idx + 1, False, state)
                else:
                    res += dfs(idx + 1, limit and digit == up, state | (1 << digit))
            return res
		# remove interger "0"
        return dfs(0, True, 0) - 1
