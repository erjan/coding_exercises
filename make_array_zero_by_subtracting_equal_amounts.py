'''
You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.
'''

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        res = 0
        while nums.count(0) != len(nums):

            x = min(i for i in nums if i > 0)

            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= x
            res += 1
        return res


----------------------------------------------------------------

def minimumOperations(self, A):
        return len(set(A) - {0})
  
-------------------------------------------------------------------------
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        count = 0
        while nums != [0]*n:
            count += 1
            small = min([i for i in nums if i > 0])
            for i in range(n):
                if nums[i] != 0:
                    nums[i] -= small
        return count
