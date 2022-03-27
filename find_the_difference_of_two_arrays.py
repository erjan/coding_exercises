'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
'''


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        f1 = set()
        f2 = set()
        
        for i in range(len(nums1)):
            
            if nums1[i] not in nums2:
                f1.add(nums1[i])
                
        
        for i in range(len(nums2)):
            
            if nums2[i] not in nums1:
                f2.add(nums2[i])
                
        
        answer = list()
        
        f1 = list(f1)
        f2 = list(f2)
        
        answer.append(f1)
        answer.append(f2)
        return answer
                
