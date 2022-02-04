'''
Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

nums[a] + nums[b] + nums[c] == nums[d], and
a < b < c < d
'''

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for x in range(k+1, len(nums)):
                        if nums[i]+nums[j] + nums[k] == nums[x]:
                            count+=1
        return count
    
    
# using combinations - something new!

  def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        
        for i,j,k,x  in itertools.combinations( range(len(nums)),4):
            if nums[i] + nums[j] + nums[k] == nums[x]:
                count+=1
        return count
            
