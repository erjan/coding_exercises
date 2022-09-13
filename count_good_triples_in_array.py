'''
You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

Return the total number of good triplets.
'''

from sortedcontainers import SortedList

class BIT:
    def __init__(self, size):
        self.bit = [0] * (size + 1)

    def getSum(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & (-idx)
        return s

    def addValue(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] += val
            idx += idx & (-idx)

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        idx = {}
        for i, x in enumerate(nums2):
            idx[x] = i
        
        for i in range(n):
            nums1[i] = idx[nums1[i]]

        ans = 0
        seen = SortedList()
        bit = BIT(n)
        for x in nums1:
            cnt = seen.bisect_right(x)
            ans += bit.getSum(x+1)
            bit.addValue(x+1, cnt)
            seen.add(x)
        return ans
