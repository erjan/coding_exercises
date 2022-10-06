'''
You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

Return an array answer of the same length as queries where answer[j] is the answer to the jth query.
'''

class Solution(object):
    def maximumBeauty(self, items, queries):
        items.sort()
        ans, beauty = [], [items[0][1]] * len(items)
        for i in range(1, len(items)): beauty[i] = max(beauty[i - 1], items[i][1])

        def bs(t):
            ans, s, e = 0, 0, len(items) - 1
            while s <= e:
                m = (s + e) // 2
                if items[m][0] <= t:
                    ans = beauty[m]
                    s = m + 1
                else: e = m - 1
            return ans

        for i in queries: ans.append(bs(i))
        return ans
      
--------------------------------------------------------------

Sort the items by price, O(nlog)

Step 2. Iterate items, find maximum value up to now, O(n) and store the max value in dictionary(MAP) here dic.

Step 3. For each queries, binary search the maximum beauty, O(log k) in key of the map which we formed and append the max value of the query from dictionary in O(1) .

Step 4. Whole process is doen in O(q+n) though.

Impementation :
'''

class Solution:
	def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

		items.sort()
		dic = dict()
		res = []
		gmax = 0
		for p,b in items:
			gmax = max(b,gmax)
			dic[p] = gmax

		keys = sorted(dic.keys())
		for q in queries:
			ind = bisect.bisect_left(keys,q)
			if ind<len(keys) and keys[ind]==q:
				res.append(dic[q])
			elif ind==0:
				res.append(0)
			else:
				res.append(dic[keys[ind-1]])

		return res
