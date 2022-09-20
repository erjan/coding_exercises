'''
You are given two positive integer arrays nums1 and nums2, both of length n.

The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.
'''

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = zip(*sorted(zip(nums1, nums2)))
        mad = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        M = sum(mad)
        MOD = 10**9 + 7
        best = 0
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                j = bisect.bisect_left(nums1, nums2[i])
                if j == len(nums1):
                    best = max(best, mad[i] - abs(nums1[-1] - nums2[i]))
                elif j == 0:
                    best = max(best, mad[i] - abs(nums1[0] - nums2[i]))
                else:
                    new = min(abs(nums1[j] - nums2[i]), abs(nums1[j-1] - nums2[i]))
                    best = max(best, mad[i] - new)
        return (M - best) % MOD
