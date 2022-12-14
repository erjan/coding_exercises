'''
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.
'''


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0 
        prev = 1_000_000_001
        for x in reversed(nums): 
            d = ceil(x/prev)
            ans += d-1
            prev = x//d
        return ans 
      
-----------------------------------------------------------------------------------
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        prev = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
                continue
            q, r = divmod(nums[i], prev)
            ops = q if r else q - 1
            res += ops
            prev = nums[i] // (ops + 1)
            
        return res
------------------------------------------------------------------      
