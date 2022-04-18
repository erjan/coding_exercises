'''
Given an integer array nums sorted in non-decreasing order 
and an integer k, return true if this array can be divided into one or more 
disjoint increasing subsequences of length at least k, or false otherwise.
'''



import collections


class Solution:
    def canDivideIntoSubsequences(self, nums, K: int) -> bool:
        return max(collections.Counter(nums).values()) * K <= len(nums)
      
      
class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        return collections.Counter(nums).most_common(1)[0][1] <= (len(nums) // K)
      
      
class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        return len(nums)//max(Counter(nums).values())>=K
      
      
--------------------------------------------------------------
The problem is equivalent to seperating the list into several sets such that in each set there is no duplicated elements.

class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        count = collections.Counter(nums)
        c = max(count.values())
        return K*c <= len(nums)
