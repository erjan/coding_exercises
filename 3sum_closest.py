'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        diff=float('inf')
        for i in range(len(nums)-1):
            start=i+1
            end=len(nums)-1
            while(start<end):
                sum=nums[i]+nums[start]+nums[end]
                if sum==target:
                    return target
                elif abs(target-sum)<diff:
                    diff=abs(target-sum)
                    ans=sum
                if sum>target:
                    end-=1
                else:
                    start+=1
        return ans
      
----------------------------------------------------------------------------------------------
def threeSumClosest(self, nums, target):
    nums.sort()
    res = sum(nums[:3])
    for i in xrange(len(nums)):
        l, r = i+1, len(nums)-1
        while l < r:
            s = sum((nums[i], nums[l], nums[r]))
            if abs(s-target) < abs(res-target):
                res = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else: # break early 
                return res
    return res
