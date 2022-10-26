'''
You are given an integer array coins of length n which represents the n coins that you own. The value of the ith coin is coins[i]. You can make some value x if you can choose some of your n coins such that their values sum up to x.

Return the maximum number of consecutive integer values that you can make with your coins starting from and including 0.

Note that you may have multiple coins of the same value.


The idea behind it is simple:
sort the coins, and every time we take the smallest available (greedy and dp like)
cur_max tracks the max consecutive we can make.

if we have a "1", then we know for sure we can make the next number (so: cur_max +=1) (Actually this case is already covered in the next if condition "coin <= cur_max+1", but I hope by separating this case out there, things are clearer)
if we have a coin "k+1" but cur_max is "k", that means we can make any number from 0 to k, so by just adding k to them, we can also make any number from k to k+(k+1). The same applies if we have any coin "j" where j < k. (we can make numbers from 0 to k+j)
if we have a coin that's bigger than the cur_max+1, we know we cannot make cur_max + 1. As the coins are sorted, we don't need to look further.
we return cur_max + 1 because we don't return the max number we can make, but the amount of numbers. From 0 to cur_max, there are exactly (cur_max + 1) numbers.
'''


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        cur_max = 0
        coins.sort()
      
        for coin in coins:
            if coin == 1:
                cur_max += 1
            elif coin <= cur_max+1:
                cur_max += coin
            else: #coin > cur_max + 1
                break
        
        return cur_max+1
      
----------------------------------------------------------------------------------------------------------------
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        
        res = 1
        
        for coin in coins:
            if (res >= coin):
                res += coin
        
        return res
