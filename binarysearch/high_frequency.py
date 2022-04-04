
'''

Given a list of integers nums, find the most frequently occurring element and return the number of occurrences of that element.

'''

class Solution:
    def solve(self, nums):
        if len(nums) == 0:
            return 0

        d = dict(collections.Counter(nums))

        return max(d.values())
