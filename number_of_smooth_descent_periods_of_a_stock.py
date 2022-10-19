'''
You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.
'''



The approach of this question is to find contigous substring of decreasing order (i.e. 5,4,3,2,1).
Step1 :- every element of array is a contigous substring, so this is why we initialized a dp with values 1
Step 2 :- Check if the difference between previous and current value is 1 dp[current_value] will become whatever the dp[curr_value]+dp[prev_value]
Step 3 :- Return the sum of values in dp (I have calculated it while updating dp values, I have initialized the s with one to include first valu)

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
                
        n = len(prices)
        res = 1
        dp = [1]*n
        
        for i in range(1,n):
            
            if prices[i-1] - prices[i] == 1:
                
                dp[i] = dp[i-1]+1
                
            res+=dp[i]            
        return res

    

