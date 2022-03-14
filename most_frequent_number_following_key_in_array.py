'''
You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.

For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. In other words, count the number of indices i such that:

0 <= i <= nums.length - 2,
nums[i] == key and,
nums[i + 1] == target.
Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.
'''

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        
        d = dict()
        for i in range(len(nums)-1):

            if nums[i] == key:
                if nums[i+1] not in d:
                    d[nums[i+1]] = 1
                else:
                    d[nums[i+1]] += 1

        maxi = max(d.values())
        for k, v in d.items():
            if v == maxi:
                print(k)
                return k
