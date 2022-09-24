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
        self.res = float('inf')
        
        for baseCost in baseCosts:
            self.dfs(toppingCosts, target, baseCost)
		
        return self.res
    
    def dfs(self, toppingCosts, target, total):
        if abs(target-total) < abs(self.res-target):
            self.res = total
        if total > target: return
        
        for i in range(len(toppingCosts)):
            self.dfs(toppingCosts[i+1:], target, total+0*toppingCosts[i])
            self.dfs(toppingCosts[i+1:], target, total+1*toppingCosts[i])
            self.dfs(toppingCosts[i+1:], target, total+2*toppingCosts[i])
