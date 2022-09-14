'''
A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
Given the base k and the number n, return the sum of the n smallest k-mirror numbers.
'''

class Solution:
	def kMirror(self, k: int, n: int) -> int:

		def deci_checker(num):
			new_num = str(int(num, k))
			return int(new_num) * all([new_num[i] == new_num[~i] for i in range(len(new_num)//2)])


		res = sum(range(1, (min(k, n+1))))

		n -= k - 1
		if n <= 0:
			return res

		base = ['']
		nxt = [str(i) for i in range(k)]

		while n:
			new = []
			for s in range(k):
				s = str(s)
				for b in base:
					tmp = s + b + s
					new.append(tmp)
					if s != '0':
						tmp = deci_checker(tmp)
						if tmp:
							n -= 1
							res += tmp
							if not n:
								return res
			nxt, base = new, nxt

		return res
