'''
You are given two integers m and n that represent the height and width of a rectangular piece of wood. You are also given a 2D integer array prices, where prices[i] = [hi, wi, pricei] indicates you can sell a rectangular piece of wood of height hi and width wi for pricei dollars.

To cut a piece of wood, you must make a vertical or horizontal cut across the entire height or width of the piece to split it into two smaller pieces. After cutting a piece of wood into some number of smaller pieces, you can sell pieces according to prices. You may sell multiple pieces of the same shape, and you do not have to sell all the shapes. The grain of the wood makes a difference, so you cannot rotate a piece to swap its height and width.

Return the maximum money you can earn after cutting an m x n piece of wood.

Note that you can cut the piece of wood as many times as you want.
'''

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for h, w, p in prices:
            dp[h][w] = p
        for i in range(1, m+1):
            for j in range(1, n+1):
                v = max(dp[k][j] + dp[i - k][j] for k in range(1, i // 2 + 1)) if i > 1 else 0
                h = max(dp[i][k] + dp[i][j - k] for k in range(1, j // 2 + 1)) if j > 1 else 0
                dp[i][j] = max(dp[i][j], v, h)
        return dp[m][n]
      
------------------------------------------------------------------------------------------------------------------
#bottom up

def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # use a dictionary to save size and prices
        price_dict = {}
        for pi, pj, price in prices:
            price_dict[(pi, pj)] = price
        
        # use dp to calculate the max sale price
		# dp[1][1] represents [1,1,price] in prices
		# therefore, we need (m+1)*(n+1) to represent the shapes since dp[i][0] and dp[0][j] are not valid shapes
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (i,j) in price_dict:
                    dp[i][j] = price_dict[(i, j)]
				
				# dp[i][j] is the max of all sub shapes
                for ii in range(1,i//2+1):
                    x = dp[ii][j]+dp[i-ii][j]
                    if x>dp[i][j]:
                        dp[i][j] = x 
                for jj in range(1,j//2+1):
                    x = dp[i][jj]+dp[i][j-jj]
                    if x>dp[i][j]:
                        dp[i][j] = x
        
        
        return dp[m][n]
