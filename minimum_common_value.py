'''
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
'''



class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        c1 = dict(Counter(nums1))
        c2 = dict(Counter(nums2))

        temp = set()
        for el in list(c1.keys()):
            if el in c2.keys():
                temp.add(el)
        if temp: 
            return min(temp)
        return -1
