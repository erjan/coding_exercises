'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 
 '''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices)//2: return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))
        buy, sell = [inf]*k, [0]*k
        for x in prices:
            for i in range(k):
                if i: buy[i] = min(buy[i], x - sell[i-1])
                else: buy[i] = min(buy[i], x)
                sell[i] = max(sell[i], x - buy[i])
        return sell[-1] if k and prices else 0
      
-------------------------------
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices)//2: return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))
        ans = [0]*len(prices)
        for _ in range(k):
            most = 0
            for i in range(1, len(prices)):
                most = max(ans[i], most + prices[i] - prices[i-1])
                ans[i] = max(ans[i-1], most)
        return ans[-1]
----------------------------------------------------------------------------
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        ## RC ##
        ## APPROACH : DP ##
        ## LOGIC ##
        """
        1. Intuition : just like any other DP problem we have to start with basic sub problem. sub problem here is what is the maxProfit for k=1, k=2 ... k=k. So, draw matrix (K x N).
        Example : 
                k = 2
                prices = [6,4,8,6,8,7,8,9]
        2. Formula is below, its better if we understand this with example. as words dont make sense.
                
                dp[i][j] = maximum of   a) dp[i][j-1]
                                        b) dp[i-1][x] + (prices[j] - prices[x]) (for all x in range of 0 to j-1)
                        
                        6   4   8   6   8   7   8   9
                k = 1   0   0   4   4   4   4   5   6
                k = 2   0   0   4   4   6   6  ???      
                
                for the position  k=2, price = 8.
                ??? = max of a) 6
                             b) max of (4 + 8 - 7) or ( 4 + 8 - 8 ) or ( 4 + 8 - 6 ) or ( 4 + 8 - 8 ) or ( 0 + 8 - 4 ) [ i.e for all x in range of 0 to j-1, profit from previous transaction till that position x i.e dp[i-1][x] and plus the profit if you buy at position x and sell at position j.(i.e prices[j] - prices[x]). We get the maximum of all values ]
                    
                ??? = 9
                    
        3. OPTIMIZATION : when you carefully observe the for loop where x = 0 to j-1, we are calculating dp[i-1][x] + prices[j] - prices[x].
        In that equation, prices[j] wont change, so we have to find maximum of ( dp[i-1][x] - prices[x] ) for 0 to j-1.
        instead of looping with x = [0,j-1]. In the j loop itself as we are filling the dp[i][j] we calculate the dp[i-1][x] - prices[x] and store the maximum.
        
        4. Edge case: # ( k = 10000000, n = 1000) k > n//2 indicates all possible transactions must happen. so we do best time to buy and sell stocks II.
        
        5. Further we can reduce the space complexicity using only 2 dp rows.
        """
        
        n = len(prices)
        if not n: return 0
        dp = [ [0 for j in range(n)] for i in range(k+1) ]
        for i in range(1, k+1):
            for j in range(1, n):
                maxpr = 0
                for x in range(j, -1, -1):
                    maxpr = max(maxpr, dp[i-1][x] + ( prices[j] - prices[x] ) )
                dp[i][j] = max( dp[i][j-1], maxpr )
        return dp[-1][-1]
        
        ## OPTIMIZED TO O(KN) ##
        # EDGE CASE
        max_profit = 0
        if k >= n / 2:
            for i in range(1, n):
                max_profit += max(prices[i] - prices[i-1], 0)
            return max_profit
        
        dp = [ [0 for j in range(n)] for i in range(k+1) ]
        for i in range(1, k+1):
            maxpr = -prices[0]
            for j in range(1, n):
                dp[i][j] = max( dp[i][j-1], maxpr + prices[j] )
                maxpr = max( maxpr, -prices[j] + dp[i-1][j] )
        return dp[-1][-1]
