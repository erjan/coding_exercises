'''
In LeetCode Store, there are n items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given an integer array price where price[i] is the price of the ith item, and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.

You are also given an array special where special[i] is of size n + 1 where special[i][j] is the number of pieces of the jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.

Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.
'''

class Solution(object):
	def shoppingOffers(self, price, special, needs):

		def helper(needs):
			if needs == [0]*m:
				return 0

			if tuple(needs) in d:
				return d[tuple(needs)]

			res = 0

			for i in range(m):
				res += needs[i]*price[i]

			for sp in special:
				for i in range(len(needs)):
					needs[i] -= sp[i]
				if all(needs[i] >= 0 for i in range(len(needs))):
					res = min(res, helper(needs[:])+sp[-1])
				for i in range(len(needs)):
					needs[i] += sp[i]

			d[tuple(needs)] = res

			return res


		n = max(needs)+1
		m = len(needs)

		d = {}

		#call helper function to solve this problem recursively
		return helper(needs)
