'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                s = nums[l]+nums[r]
                if s == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return list(result)
----------------------------------------------------------------------------------------    
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l < r:
                sum3 = a + nums[l] + nums[r]
                if sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
        # delete duplicates
        res = [tuple(sorted(val)) for val in res]
        res = list(set(res))
        res = [list(t) for t in res]
        print(res)
        return res
