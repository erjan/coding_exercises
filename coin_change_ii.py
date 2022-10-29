'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
'''

   def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
               if j >= i:
                   dp[j] += dp[j - i]
        return dp[amount]
      
---------------------------------------------------
'''
Abstract model transform.

Fill knapsack of wieght W with N items with each item is unlimited supply.

<=>

Fill knapsack of $amount with C coins with each coin is unlimied supply.

Hint:

Think of dynamic programming strategy with bottom-up update

Make change with small coin to large coin.

Update method count from small amount to large amount.

State transfer function:

DP[ 0 ] = 1 as initialization (i.e., $0 is reached by taking no coins. ).

And update with formula
DP[ current_amount ] = DP[ current_amount ] + DP[ current_amount- coin ]

'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # base case:
        # amount 0's method count = 1 (by taking no coins)
        change_method_count = [1] + [ 0 for _ in range(amount)]
        
        # make change with current coin, from small coin to large coin
        for cur_coin in coins:
            
            # update change method count from small amount to large amount
            for small_amount in range(cur_coin, amount+1):
                
                # current small amount can make changed with current coin
                change_method_count[small_amount] += change_method_count[small_amount - cur_coin]
                
        return change_method_count[amount]
      
----------------------------------------------------------------------------------------------------------

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
            The logic is we find number of ways we can make change for each amount from
            1 to amount. Because, let's say we know how many ways we can make change
            for amount = 2,3,4. Then for a coins array of 1,3 we can say that number
            of ways we can make change for 5 is equal to number of ways we can make
            change for (5-1=4) + (5-3=2).
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        # Why we are looping through coins first and then through amount for each coin is
        # If we loop through amount first and then coins for each amount, we might get
        # duplicate ways because of unorderness. Example: Using 1, 3. we can make 5
        # by 1 + 1 + 3, 1 + 3 + 1, 3 + 1 + 1. But actually all these 3 possibilites
        # are same. This will be avoided if we loop through coins first. Since, we 
        # will only consider each coin once for each amount
        for coin in coins:
            # Why we are starting loop from coin instead of 0 is, if i < coin, i - coin
            # will ge -ve. In normal words, if current amount is 2 and if coin is 5, we
            # anyway can't make an amount of 2 from coin 5.
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]
