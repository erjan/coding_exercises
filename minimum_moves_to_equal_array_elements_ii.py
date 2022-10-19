'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.
'''

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        
        
        nums.sort()
        
        if n %2 == 1:
            median = nums[n//2]
        else:
            median = nums[n//2-1]
        
        
        moves = 0
        
        for n in nums:
            
            if n!= median:
                moves += abs(n-median)
        return moves
        
--------------------------------------------------------------------------------
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans, median = 0, nums[len(nums) // 2]
        for num in nums: ans += abs(median - num)
        return ans
        
        
