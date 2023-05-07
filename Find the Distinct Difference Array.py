'''
You are given a 0-indexed array nums of length n.

The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of distinct elements in the suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements in the prefix nums[0, ..., i].

Return the distinct difference array of nums.

Note that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j inclusive. Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.
'''


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        # One liner
        # return [len(Counter(nums[:i + 1])) - len(Counter(nums[i + 1:])) for i in range(len(nums))]
        prefix = defaultdict(int)
        suffix = Counter(nums)
        result = []
        for x in nums:
            prefix[x] += 1
            suffix[x] -= 1
            if suffix[x] == 0:
                suffix.pop(x)
            result.append(len(prefix) - len(suffix))
        return result
