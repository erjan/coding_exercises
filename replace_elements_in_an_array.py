'''
You are given a 0-indexed array nums that consists of n distinct positive integers. Apply m operations to this array, where in the ith operation you replace the number operations[i][0] with operations[i][1].

It is guaranteed that in the ith operation:

operations[i][0] exists in nums.
operations[i][1] does not exist in nums.
Return the array obtained after applying all the operations.
'''



class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        swaps = {}
        for s, e in reversed(operations):
            swaps[s] = swaps[e] if e in swaps else e
        for i, num in enumerate(nums):
            if num in swaps:
                nums[i] = swaps[num]
        return nums
