'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        first = 0
        second = 0
        product = 1
        combos = 0
        
        for second in range(len(nums)):
            # add second to product
            product *= nums[second]
            # move first, till product is less than k
            while product >= k and first <= second:
                product /= nums[first]
                first += 1
            # count combos. Note that first is one place beyond the starting range, so add +1
            combos += second - first + 1
                    
        return combos
