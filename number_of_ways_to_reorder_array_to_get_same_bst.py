'''
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7
'''

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        dp = [[1 for r in range(len(nums)+1)] for l in range(len(nums)+1)]
        
        for i in range(1, len(nums)):
            for j in range(1, len(nums)):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j])
        
        return (self.getNum(nums, dp) - 1)%(10**9+7)
    
    def getNum(self, nums, dp):
        if len(nums) <= 2:
            return 1
        left, right = [num for num in nums if num < nums[0]], [num for num in nums if num > nums[0]]
        return (self.getNum(left, dp)*dp[len(left)][len(right)]*self.getNum(right, dp))
      
------------------------------------------
def numOfWays(self, nums: List[int]) -> int:
    def f(nums):
        if len(nums) <= 2: return 1
        left = [v for v in nums if v < nums[0]]
        right = [v for v in nums if v > nums[0]]
        return comb(len(left)+len(right), len(right)) * f(left) * f(right)
    return (f(nums)-1) % (10**9+7)
