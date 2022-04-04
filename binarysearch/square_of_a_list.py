'''

Given a list of integers sorted in ascending order nums, square the elements and give the output in sorted order.
'''


class Solution:
    def solve(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums
        
        
#another O(n) for time/space

class Solution:
    def solve(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        index = n - 1
        res = [0 for i in range(len(nums))]
        while index >= 0:
            if abs(nums[l]) > abs(nums[r]):
                res[index] = nums[l] * nums[l]
                l += 1
            else:
                res[index] = nums[r] * nums[r]
                r -= 1
            index -= 1

        return res
