'''
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
'''

#my own solution

class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        s_nums = sorted(nums)
        if s_nums == nums:
            print('good')
            return True

        new = list()
        for i in range(len(nums)-1):

            if nums[i+1] < nums[i]:

                new.extend(nums[(i+1):])

                new.extend(nums[:(i+1)])


        for i in range(len(nums)-1):
            if new[i] > new[i+1]:
                print('bad')
                return False
        print('good')
        return True
