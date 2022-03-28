'''
You are given two integer arrays nums1 and nums2 where nums2 is an anagram of nums1. Both arrays may contain duplicates.

Return an index mapping array mapping from nums1 to nums2 where mapping[i] = j means the ith element in nums1 appears in nums2 at index j. If there are multiple answers, return any of them.

An array a is an anagram of an array b means b is made by randomizing the order of the elements in a.

 
 '''
 
 class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
                
        res = list()
        
        
        for n in nums1:
            
            res.append( nums2.index(n))
        
        return res
        
        
