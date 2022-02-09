'''
Given a list of integers prices representing the stock prices of a company in chronological order, return the 
maximum profit you could have made from buying and selling that stock any number of times.

You must buy before you can sell it. But you are not required to buy or sell the stock.
'''

class Solution:
    def solve(self, prices):
        diffs = list()

        for i in range(len(prices)-1):
            j = i+1
            diffs.append( prices[j] - prices[i])


        total = sum(list(filter(lambda x : x > 0, diffs)))
        return total
