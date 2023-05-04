'''
You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.
'''



class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ct, n = 0, len(nums)
        for d in nums:
            if d == 1:
                ct += 1
        if ct > 0:
            return n - ct
        for steps in range(n):
            for i in range(n - steps - 1):
                nums[i] = gcd(nums[i], nums[i+1])
                if nums[i] == 1:
                    return steps + n
        return -1
