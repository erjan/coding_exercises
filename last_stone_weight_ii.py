'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.
'''


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.cache = {}
        
        return self.recursive(stones, 0, 0, 0)
    
    def recursive(self, stones: List[int], index:int, sum_1, sum_2):
        if index == len(stones):
            return abs(sum_1 - sum_2)
        key = str(index) + '#' + str(sum_1)+'#'+ str(sum_2)
        if  key not in self.cache:
            diff_1 = self.recursive(stones, index+1, sum_1 + stones[index], sum_2)
            diff_2 = self.recursive(stones, index+1, sum_1, sum_2 + stones[index])
            self.cache[key] = min(diff_1, diff_2)
        
        return self.cache[key] 
      
---------------------------------------------------------------------------------------------
