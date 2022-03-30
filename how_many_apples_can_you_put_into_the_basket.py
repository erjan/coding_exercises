'''
You have some apples and a basket that can carry up to 5000 units of weight.

Given an integer array weight where weight[i] is the weight of the ith apple, return the maximum number of apples you can put in the basket.
'''


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        
        total = 0
        c = 0
        for i in range(len(weight)):
            
            w = weight[i]
            
            total +=w
            c+=1
            
            if total > 5000:
                c -=1
                break
        return c
        
        
