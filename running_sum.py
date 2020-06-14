'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = list()

        for i in range(len(nums)):
            res.append(sum(nums[:(i+1)]))
        print(res)
        return res
