'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
'''


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            cur = nums[left] + nums[right]
            if cur == k:
                ans += 1
                left += 1
                right -= 1
            elif cur < k:
                left += 1
            else:
                right -= 1
        
        return ans
      
-------------------------------------------------------------------------------------------------
The idea is that there is only one int k - n that can be paired with n. That said we can remember which and how many k - n do we need when n is encountered. If we find k - n, we can delete one n from dict because we can't use that int more than once.

We can use default dictionary from python lib so not to get ValueError in the absence of some key.

from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pair = defaultdict(int) # integer 0 is the default value of all the keys
        res = 0
        
        for n in nums:
            if pair[n]: # if we encountered k - n already
                res += 1
                pair[n] -= 1
            else: # if we did'n find a pair yet
                pair[k - n] += 1
                
        return res
      
------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        res = 0
        for n in c.keys():
            res += min(c[k-n], c[n])
                
        return res//2
