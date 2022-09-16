'''
Given an integer n represented as a string, return the smallest good base of n.

We call k >= 2 a good base of n, if all digits of n base k are 1's.
'''


def smallestGoodBase(self, n: str) -> str:

	def is_valid(base):
		"""returns 0 if total == n, pos if n > total and neg if n < total"""
		total = sum(base**i for i in range(length))
		return n - total

	n = int(n)
	N = len(bin(n)[2:])
	for length in range(N, 0, -1):
		low = 2
		high = n - 1
		while low <= high:
			guess = (low + high) // 2
			v = is_valid(guess)
			if v < 0:
				high = guess - 1
			elif v > 0:
				low = guess + 1
			else:
				return str(guess)
