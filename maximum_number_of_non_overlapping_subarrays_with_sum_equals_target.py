'''
Given an array nums and an integer target, return the maximum
number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.
'''



class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        ## RC ##
        ## APPROACH : HASHMAP - 2 SUM VARIANT ##
        lookup = {0 : -1}
        running_sum  = 0
        count = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - target in lookup:
                count += 1
                lookup = {} #reset the map
            lookup[running_sum] = i
        return count
      
---------------------------------------------------------------------------------
class Solution:

  def maxNonOverlapping(self, nums: List[int], target: int) -> int:
      prefix = 0
      cum = 0
      s = set([0])
      for i in range(len(nums)):
          prefix+=nums[i]
          if prefix-target in s:
              cum+=1
              prefix = 0
              s = set([0])
          s.add(prefix) # we must add prefix at the end, in order to deal with target == 0
      return cum
