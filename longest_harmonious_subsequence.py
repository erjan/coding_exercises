'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

'''

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        l = sorted(list(d.keys()))
        print(l)
        maxi = 0
        for i in range(len(l)-1):

            if l[i+1] - l[i] <= 1:
                maxi = max(maxi, d[l[i+1]] + d[l[i]])
        print(maxi)
        return maxi
