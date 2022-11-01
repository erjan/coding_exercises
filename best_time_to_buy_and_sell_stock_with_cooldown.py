'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

def maxProfit(self, prices):
    free = 0
    have = cool = float('-inf')
    for p in prices:
        free, have, cool = max(free, cool), max(have, free - p), have + p
    return max(free, cool)
  
-------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
		# initialization
        cool_down, sell, hold = 0, 0, -float('inf')
        
        for stock_price_of_Day_i in prices:
            
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
            
            # Max profit of cooldown on Day i comes from either cool down of Day_i-1, or sell out of Day_i-1 and today Day_i is cooling day
            cool_down = max(prev_cool_down, prev_sell)
            
            # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
            sell = prev_hold + stock_price_of_Day_i
            
            # Max profit of hold on Day_i comes from either hold of Day_i-1, or cool down on Day_i-1 and buy on Day_i
            hold = max(prev_hold, prev_cool_down - stock_price_of_Day_i)
        
        
        # The action of final trading day must be either sell or cool down
        return max(sell, cool_down)
      
--------------------------------------------------------------------------------------------------------
The key is 3 states and 5 edges for state transition. 3 states are notHold (stock), hold (stock), and notHold_cooldown. The initial values of the latter two are negative infinity since they are meaningless, i.e. you won't hold stocks at first and there's no cooldown at first. The 5 edges:

hold -----do nothing----->hold

hold -----sell----->notHold_cooldown

notHold -----do nothing -----> notHold

notHold -----buy-----> hold

notHold_cooldown -----do nothing----->notHold

def maxProfit(self, prices):
    notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
    for p in prices:
        hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
    return max(notHold, notHold_cooldown)
