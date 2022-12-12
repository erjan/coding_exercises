'''
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.
'''

from heapq import heappop, heappush

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        L, wealth = len(profits), w
        projs, profits_hp = sorted(range(L), key=capital.__getitem__, reverse=True), []

        for _ in range(min(k, L)):  # rounds untill projects run out or k limit is reached
            while projs and capital[projs[-1]] <= wealth:  # all available projects under current wealth
                heappush(profits_hp, -profits[projs.pop()])  # keep ranking available pure profits
            if not profits_hp: break  # stop when no more project can be performed
            wealth += -heappop(profits_hp)  # greedily perform the most profitable project, udpate wealth

        return wealth
      
---------------------------------------------------------------------------------------------------------------------
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit = []
        min_capital = []
        
        for a, b in zip(capital, profits):
            if a <= w:
                heappush(max_profit, -b)
            else:
                heappush(min_capital, (a, b))

        for i in range(k):
            if max_profit:
                w += -heappop(max_profit)

                while min_capital and min_capital[0][0] <= w:
                    dontcare, value = heappop(min_capital)
                    heappush(max_profit, -value)
            else:
                break
        return w
