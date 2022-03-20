'''
You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.
'''

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        newnum = list()
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                newnum.append(nums[i])
        print('after')
        print(newnum)

        nums = newnum
        count = 0
        i = 1
        while i < len(nums)-1:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                count += 1

            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                count += 1
            i += 1

        print('total hill valey count', count)
        return count
