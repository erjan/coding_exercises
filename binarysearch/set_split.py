'''

Given a list of positive integers nums, return whether you can divide the list into two groups a and b such that:

The sum of a and the sum of b are equal.
Every number in a is strictly less than every number in b.

'''

class Solution:
    def solve(self, nums):
        nums.sort()
        prefixsum = list(accumulate(nums))
        nums.reverse()
        suffixsum = list(accumulate(nums))

        suffixsum.reverse()
        nums.reverse()
        

        for i in range(1, len(nums)):
                if suffixsum[i] == prefixsum[i-1] and nums[i] > nums[i-1]:                                                
                        return True
        return False       
