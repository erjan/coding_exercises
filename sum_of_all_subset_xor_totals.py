'''
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
'''

#bad but my own solution

from itertools import chain, combinations, accumulate

from operator import xor
from functools import reduce



class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def powerset(iterable):
            s = list(iterable)

            return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
        
        nums = [str(i) for i in nums]
        nums = ''.join(nums)
        res = powerset(nums)

        for i in range(len(res)):
            res[i] = list(res[i])
            if len(res[i]) > 0:
                for j in range(len(res[i])):
                    res[i][j] = int(res[i][j])

        ac_sum = 0
        for i in range(len(res)):
            subset = res[i]
            if len(subset) != 0:
                temp = reduce(lambda i, j: int(i) ^ int(j), subset)
                ac_sum += temp

        print(ac_sum)
        return ac_sum
        
        
