'''
Implement a data structure with the following methods:

RangeSum(int[] nums) constructs a new instance with the given nums.
total(int i, int j) returns the sum of integers from nums between [i, j). That is, nums[i] + nums[i + 1] + ... + nums[j - 1].
Constraints

n ≤ 100,000 where n is the length of nums
k ≤ 100,000 where k is the number of calls to total
'''


class RangeSum:
    def __init__(self, nums):
        self.prefix = [0] + list(itertools.accumulate(nums))

    def total(self, i, j):
        return self.prefix[j] - self.prefix[i]

      
class RangeSum:
    def calculateprefixsum(self, vals):
        vals.insert(0, 0)
        for i in range(1, len(vals)):
            vals[i] += vals[i - 1]
        return vals

    def __init__(self, nums):
        self.nums = nums
        self.prefixsum = self.calculateprefixsum(nums)

    def total(self, i, j):
        return self.prefixsum[j] - self.prefixsum[i]
