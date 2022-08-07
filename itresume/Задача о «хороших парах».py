'''
Дан массив целых чисел nums. Необходимо посчитать количество «хороших пар». Пара (i, j) называется хорошей, если:

nums[i] == nums[j]
i < j
'''



class Answer:
    def numIdenticalPairs(self, nums):
        
        res = 0
        for i in range(len(nums)):

            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    if i < j:
                        res+=1
        return res
      
--------------------------------------------------
from collections import Counter

class Answer:
    def numIdenticalPairs(self, nums):
        return sum(k * (k - 1) / 2 for k in Counter(nums).values()
