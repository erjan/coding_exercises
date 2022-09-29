'''
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_types = Counter()
        distinct = 0
        max_fruits = 0
        
        left = right = 0
        while right < len(fruits):
            # check if it is a new fruit, and update the counter
            if fruit_types[fruits[right]] == 0:
                distinct += 1
            fruit_types[fruits[right]] += 1
            
            # too many different fruits, so start shrinking window
            while distinct > 2:
                fruit_types[fruits[left]] -= 1
                if fruit_types[fruits[left]] == 0:
                    distinct -= 1
                left += 1
            
            # set max_fruits to the max window size
            max_fruits = max(max_fruits, right-left+1)
            right += 1
        
        return max_fruits
