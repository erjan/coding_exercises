
'''
Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.
'''

class Solution:
    def minNumber(self, n1: List[int], n2: List[int]) -> int:
        common, m1, m2 = set(n1).intersection(n2), min(n1), min(n2)
        return min(common) if common else min(m1, m2) * 10 + max(m1, m2)
