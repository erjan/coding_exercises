'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
'''


#messy solution
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        c1 = dict(c1)
        c2 = dict(c2)

        res = []
        for k in c1.keys():
            temp = []
            if k in c2.keys():
                how_many = min(c1[k],c2[k])
                temp.extend( [k] * how_many)
            if len(temp)!= 0:
                res.extend( temp )
        return res


