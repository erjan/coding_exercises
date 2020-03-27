#Given an integer array, find three numbers whose product is maximum and output the maximum product.

import math
import functools
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        f1 = nums[-1] * nums[-2] * nums[-3]
        
        f2 = nums[-1] * nums[0] * nums[1]
        
        return max(f1,f2)
