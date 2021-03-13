'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in
nums1 and nums2 are m and n respectively. You may 
assume that nums1 has a size equal to m + n such that 
it has enough space to hold additional elements from nums2.
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
        здесь я тупо не понял задачу и сидел решал не то - тут даны m, n - а они нужны чтоб вести отсчет!
        '''
        
        p1 = m - 1
        p2 = n - 1
        i = m+n-1
        while p2 >= 0:

        
            if p1 >= 0 and nums1[p1] > nums2[p2]:
               
                nums1[i] = nums1[p1]
                i = i-1
                p1 = p1-1

            else:                
                nums1[i] = nums2[p2]
                i = i-1
                p2 = p2-1

        return nums1

