'''
You are given a list of integers nums. Return the number of pairs i < j such that nums[i] = nums[j].
'''

from  collections import Counter

class Solution:
    def solve(self, nums):                
        res = 0
        d = dict(Counter(nums))

        d = d.values()

        for x in d:

            res += x*(x-1)//2
        return res

