'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        
        for i, n in enumerate(nums):
            
            m = target - n
            
            if m in d:
                return [d[m] ,i]
            else:
                d[n] =  i
                
                
#another solution                
def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       for i, value in enumerate(nums): #1
           remaining = target - nums[i] #2
           
           if remaining in seen: #3
               return [i, seen[remaining]]  #4
           else:
               seen[value] = i  #5                
