'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.helper(nums, target, 4, [], results)
        return results
    
    def helper(self, nums, target, N, res, results):
        
        if len(nums) < N or N < 2: #1
            return
        if N == 2: #2
            output_2sum = self.twoSum(nums, target)
            if output_2sum != []:
                for idx in output_2sum:
                    results.append(res + idx)
        
        else: 
            for i in range(len(nums) -N +1): #3
                if nums[i]*N > target or nums[-1]*N < target: #4
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]: #5
                    self.helper(nums[i+1:], target-nums[i], N-1, res + [nums[i]], results)
    
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(nums) - 1 
        while left < right: 
            temp_sum = nums[left] + nums[right] 

            if temp_sum == target:
                res.append([nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while right > left and nums[right] == nums[right + 1]:
                    right -= 1
                                
            elif temp_sum < target: 
                left +=1 
            else: 
                right -= 1
                                        
        return res
      
------------------------------------------------------------------------

class Solution:
# @return a list of lists of length 4, [[val1,val2,val3,val4]]
def fourSum(self, num, target):
    two_sum = collections.defaultdict(list)
    res = set()
    for (n1, i1), (n2, i2) in itertools.combinations(enumerate(num), 2):
        two_sum[i1+i2].append({n1, n2})
    for t in list(two_sum.keys()):
        if not two_sum[target-t]:
            continue
        for pair1 in two_sum[t]:
            for pair2 in two_sum[target-t]:
                if pair1.isdisjoint(pair2):
                    res.add(tuple(sorted(num[i] for i in pair1 | pair2)))
        del two_sum[t]
    return [list(r) for r in res]
  
---------------------------------------------------------------------------------------------------  
