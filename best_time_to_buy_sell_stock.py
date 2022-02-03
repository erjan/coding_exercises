'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one 
stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

#my own TLE solution
def f(nums):
    cur_profit = 0
    m = 1e9
    for i in range(len(nums)-1):

        local_min = nums[i]
        if local_min < m:
            m = local_min

            for j in range( i+1, len(nums)):
                if nums[j] - nums[i] > cur_profit:
                    cur_profit = nums[j]-nums[i]
    print(cur_profit)
        
r = [7,1,5,3,6,4]
f(r)
