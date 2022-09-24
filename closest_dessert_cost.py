'''
You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors and m types of toppings to choose from. You must follow these rules when making your dessert:

There must be exactly one ice cream base.
You can add one or more types of topping or have no toppings at all.
There are at most two of each type of topping.
You are given three inputs:

baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
target, an integer representing your target price for dessert.
You want to make a dessert with a total cost as close to target as possible.

Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.
'''


class Solution:
	def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

		minDiff = float('inf')
		closestCost = 0

		def combinations(tCosts, idx, curCost, target):
			nonlocal minDiff
			nonlocal closestCost

			if abs(target - curCost) <= minDiff:
				if minDiff == abs(target - curCost):
					closestCost = min(closestCost, curCost)
				else:
					closestCost = curCost
					minDiff = abs(target- curCost)

			if idx >= len(tCosts):
				return 

			for num in range(3):
				combinations(tCosts, idx+1, curCost+(tCosts[idx] * num), target)

		for bCost in baseCosts:
			 combinations(toppingCosts, 0, bCost, target)

		return closestCost
