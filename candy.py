'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies_dist = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candies_dist[i] = candies_dist[i-1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies_dist[i] = max(candies_dist[i], candies_dist[i+1] + 1)
            
        return sum(candies_dist)

--------------------------------------------------------------------------------------
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [0] + [1] * len(ratings) + [0]
        ratings = [float('inf')] + ratings + [float('inf')]

        for i in range(1, len(ratings) - 1):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        for i in range(len(ratings) - 2, 0, -1):
            if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
                res[i] = res[i + 1] + 1
        
        return sum(res)
