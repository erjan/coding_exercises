'''
You are given a 0-indexed integer array books of length n where books[i] denotes the number of books on the ith shelf of a bookshelf.

You are going to take books from a contiguous section of the bookshelf spanning from l to r where 0 <= l <= r < n. For each index i in the range l <= i < r, you must take strictly fewer books from shelf i than shelf i + 1.

Return the maximum number of books you can take from the bookshelf.
'''

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        dp, stack = [0] * n, []
        for i in range(n):
            if books[i] == 0:
                stack.append(i)
                continue
            while stack:
                j = stack[-1]
                if books[j] >= books[i] - (i - j):
                    stack.pop()
                else:
                    break
            if not stack:
                j = -1
            if books[i] - i + j + 1 < 0:
                dp[i] = books[i] * (books[i] + 1) // 2
            else:
                dp[i] = (books[i] + books[i] - i + j + 1) * (i - j) // 2
            if j >= 0:
                dp[i] += dp[j]
            stack.append(i)
        return max(dp)
------------------------------------------------------------------------------------------------------
class Solution:
	def maximumBooks(self, books: List[int]) -> int:
		n = len(books)
		dp = [0] * n
		diff = [0] * n
		prev = [-1] * n
		res = 0
		stack = []

		for i in range(n):
			diff[i] = books[i] - i

		# increasing stack to find prev smaller
		for i in range(n):
			while stack and stack[-1][1] >= diff[i]:
				stack.pop()

			if stack:
				prev[i] = stack[-1][0]

			stack.append([i, diff[i]])

		dp[0] = books[0]

		for i in range(n):
			if  prev[i] != -1:
				length, startIndex = i - prev[i], i - prev[i]
				startValue = books[i] - startIndex + 1
				endValue = books[i]
				total = ((startValue + endValue) * length) // 2
				dp[i] = max(total, total + dp[prev[i]])
			else:
				length, startIndex = min(i + 1, books[i]), min(i + 1, books[i])
				startValue = books[i] - startIndex + 1
				endValue = books[i]
				total = ((startValue + endValue) * length) // 2
				dp[i] = total

		return max(dp)
