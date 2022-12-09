'''
You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.
'''from itertools import permutations 

class Solution:
    def judgePoint24(self, original_nums: List[int]) -> bool:
        def dfs(curr_nums):
            # Case (1,2)(3,4)
            res_1 = self.perform_ops(curr_nums[:1], curr_nums[1:2])
            res_2 = self.perform_ops(curr_nums[2:3], curr_nums[3:])
            res_1 = self.perform_ops(res_1, res_2)
            if self.find_24(res_1): return True

            # Case (1 ((2,3) 4))
            res = self.perform_ops(curr_nums[1:2], curr_nums[2:3])
            res = self.perform_ops(res, curr_nums[3:4])
            res = self.perform_ops(curr_nums[:1], res)
            if self.find_24(res): return True

            # Case (1 (2 (3, 4)))
            res = self.perform_ops(curr_nums[2:3], curr_nums[3:4])
            res = self.perform_ops(curr_nums[1:2], res)
            res = self.perform_ops(curr_nums[:1], res)
            if self.find_24(res): return True

            # Case ((1 (2,3)) 4)
            res = self.perform_ops(curr_nums[1:2], curr_nums[2:3])
            res = self.perform_ops(curr_nums[:1], res)
            res = self.perform_ops(res, curr_nums[3:4])
            if self.find_24(res): return True

            # Case (((1 2) 3) 4)
            res = self.perform_ops(curr_nums[:1], curr_nums[1:2])
            res = self.perform_ops(res, curr_nums[2:3])
            res = self.perform_ops(res, curr_nums[3:4])
            if self.find_24(res): return True

            return False

        for num in list(permutations(original_nums)):
            if dfs(list(num)):
                return True

        return False

    def find_24(self, nums):
        for num in nums:
            if 23.99 < num < 24.01:
                return True

    def perform_ops(self, nums1, nums2):
        result = []
        for num_1 in nums1:
            for num_2 in nums2:
                result.append(num_1 + num_2)
                result.append(num_1 - num_2)
                result.append(num_1 * num_2)
                if num_2 != 0:
                    result.append(num_1 / num_2)
        return result
      
--------------------------------------------------------------------------------------------------------------------
from itertools import combinations
from typing import List


class Solution:

    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6

        for (idx_1, num_1), (idx_2, num_2) in combinations(enumerate(nums), 2):
            new_nums = []
            for (idx_3, num_3) in enumerate(nums):
                if (idx_1 != idx_2) and (idx_2 != idx_3) and (idx_1 != idx_3):
                    new_nums.append(num_3)

            intermediate_numbers = {num_1 + num_2, abs(num_1 - num_2), num_1 * num_2}

            if num_1 != 0: intermediate_numbers.add(num_2 / num_1)
            if num_2 != 0: intermediate_numbers.add(num_1 / num_2)

            for num_4 in intermediate_numbers:
                if self.judgePoint24(new_nums + [num_4]):
                    return True
        return False
--------------------------------------------------------------------------------------------------------------------------------------
from fractions import Fraction

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        @cache
        def fn(*args): 
            """Return True if arguments can be combined into 24."""
            if len(args) == 1: return args[0] == 24
            for x, y, *rem in permutations(args): 
                for op in add, sub, mul, Fraction: 
                    if (op != Fraction or y != 0) and fn(op(x, y), *rem): return True
            return False 
        
        return fn(*cards)
