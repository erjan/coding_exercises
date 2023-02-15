'''
You are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.
'''

'''
Explanation
When talking about swap, it's very likely to run into Greedy algorithm. In this case, we want to move the minimum to the leftmost side then find how many swaps need to move maximum to the rightmost side.
See below comment for more explanation
'''

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        mi = min(nums)                                     # find minimum
        idx1 = nums.index(mi)                              # locate the first mi from the left side
        
        nums = [nums[idx1]] + nums[:idx1] + nums[idx1+1:]  # make the swaps & update `nums`
        
        mx = max(nums)                                     # find maximum 
        idx2 = nums[::-1].index(mx)                        # locate the first mx from the right side
        return idx1 + idx2                                 # return total swaps needed
      
--------------------------------------------------------------------------------------------------------------
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_value = max_index = nums[0]
        min_index = max_value = 0
        for i, n in enumerate(nums):
            if n < min_value:
                min_value = n
                min_index = i
            
            if n >= max_value:
                max_value = n
                max_index = i
                
        return min_index + len(nums) - 1 - max_index - (min_index > max_index)
