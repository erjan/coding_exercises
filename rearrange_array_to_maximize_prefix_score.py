'''
You are given a 0-indexed integer array nums. You can rearrange the elements of nums to any order (including the given order).

Let prefix be the array containing the prefix sums of nums after rearranging it. In other words, prefix[i] is the 
sum of the elements from 0 to i in nums after rearranging it. The score of nums is the number of positive integers in the array prefix.

Return the maximum score you can achieve.
'''


class Solution:
    def maxScore(self, nums: List[int]) -> int:

        nums.sort(reverse=True)

        pref = [nums[0]]

        for i in range(1, len(nums)):

            pref.append(pref[-1] + nums[i])

        res = 0
        for i in range(len(pref)):
            if pref[i] > 0:
                res += 1
        return res
      
----------------------------------------------------------------------------------------------
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        return sum(n > 0 for n in accumulate(sorted(nums, reverse=True)))
