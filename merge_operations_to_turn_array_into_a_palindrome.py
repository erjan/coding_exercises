'''
You are given an array nums consisting of positive integers.

You can perform the following operation on the array any number of times:

Choose any two adjacent elements and replace them with their sum.
For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].
Return the minimum number of operations needed to turn the array into a palindrome.
'''


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ls, rs = nums[l], nums[r]
        cnt = 0
        while l < r:
            if ls == rs:
                l += 1
                r -= 1
                ls, rs = nums[l], nums[r]
            elif ls < rs:
                l += 1
                ls += nums[l]
                cnt += 1
            else:
                r -= 1
                rs += nums[r]
                cnt += 1
        return cnt
            
