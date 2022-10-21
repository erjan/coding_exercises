'''
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''


class Solution:
    def maxProfit(self, P: List[int], F: int) -> int:
        buying, selling = 0, -P[0]
        for i in range(1, len(P)):
            buying = max(buying, selling + P[i] - F)
            selling = max(selling, buying - P[i])
        return buying
      
----------------------------------------------------------------------------------------------   

def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        s0 = [0 for i in range(len(prices))]
        s1 = [0 for i in range(len(prices))]
		
		# Set our base case
		s0[0] = 0
		s1[0] = -prices[0]
		
        for i in range(1, len(prices)):
            s0[i] = max(s0[i-1], s1[i-1] + prices[i] - fee)
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
        return s0[-1]
      
-----------------------------------------------------------------------

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp_hold, dp_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            
            prev_hold, prev_not_hold = dp_hold, dp_not_hold
            
            # either keep not hold, or sell out today at stock price
            dp_not_hold = max(prev_not_hold, prev_hold + stock_price)
            
            # either keep hold, or buy in today at stock price and pay transaction fee for this trade
            dp_hold = max(prev_hold, prev_not_hold - stock_price - fee)
        
        # maximum profit must be in not-hold state
        return dp_not_hold
