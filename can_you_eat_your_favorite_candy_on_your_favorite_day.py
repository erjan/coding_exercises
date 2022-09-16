'''
You are given a (0-indexed) array of positive integers candiesCount where candiesCount[i] represents the number of candies of the ith type you have. You are also given a 2D array queries where queries[i] = [favoriteTypei, favoriteDayi, dailyCapi].

You play a game with the following rules:

You start eating candies on day 0.
You cannot eat any candy of type i unless you have eaten all candies of type i - 1.
You must eat at least one candy per day until you have eaten all the candies.
Construct a boolean array answer such that answer.length == queries.length and answer[i] is true if you can eat a candy of type favoriteTypei on day favoriteDayi without eating more than dailyCapi candies on any day, and false otherwise. Note that you can eat different types of candy on the same day, provided that you follow rule 2.

Return the constructed array answer.
'''

 def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        result = [False] * len(queries)
        presum = [0] + candiesCount[:]
        for i in range(1, len(presum)):
            presum[i] += presum[i - 1]
            
        for idx, val in enumerate(queries):
            candType, favDate, cap = val
            mx = presum[candType + 1] - 1
            mn = presum[candType]//cap
            if mn <= favDate <= mx:
                result[idx] = True
                
        return result
---------------------------------------------

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        A = list(accumulate(candiesCount))
        res = []
        for type, day, cap in queries:
            if type == 0:
                res.append(A[0] > day)
            else:
                to_be_eaten = A[type-1] + 1
                res.append(to_be_eaten <= ((day + 1) * cap) and A[type] > day)
        return res
-----------------------------------------------------------------------------------------------
from itertools import accumulate
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        cumSum = [0] + list(accumulate(candiesCount))
        return [True if cumSum[t] < (day+1)*cap and day < cumSum[t+1] else False for t, day, cap in queries]
