'''
A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.

The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.

For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.
'''


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        nums = cost
        nums = sorted(nums, reverse=True)
        total_cost = 0
        i = 0

        while i < len(nums):
            if i == len(nums)-1:
                total_cost += nums[i]
                break
            #print(nums[i], nums[i+1])
            total_cost += nums[i] + nums[i+1]
            i += 3
        print(total_cost)

        return total_cost
