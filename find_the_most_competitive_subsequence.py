'''
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive
than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a 
has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because 
the first position they differ is at the final number, and 4 is less than 5.
'''

class Solution:
    def mostCompetitive(self, nums, k):
        stack,n = [],len(nums)
        for idx in range(n):
            while stack and stack[-1] > nums[idx] and n-idx > k-len(stack):
                stack.pop()
            if len(stack)<k:
                stack.append(nums[idx])
        return stack
