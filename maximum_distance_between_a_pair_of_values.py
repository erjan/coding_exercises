'''
You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.
'''

def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i,j = 0,0
        max_distance = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                max_distance = max(max_distance, j-i)
                j += 1
            else:
                j += 1
                i += 1
				
        return max_distance
      
-----------------------------------------------------------------------------------------------
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        distance = 0
        
        for i in range(len(nums1)):
            start = i
            end = len(nums2)-1
            while start<= end:
                mid = (start+end)//2
				
                if nums2[mid] < nums1[i]:
                    end = mid-1
                else:
                    start = mid+1
            distance = max(distance, end -i)
            
        return distance
------------------------------------------------------------------------------------------------------------
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
                 
        maxdist = 0                
        for i in range(len(nums1)):
                        
            l = i
            r = len(nums2)-1
            while l <=r:
                
                mid = (l+r)//2
                
                if nums1[i] > nums2[mid]:
                    r = mid-1
                
                else:
                    l = mid+1                
            maxdist = max(maxdist,r-i)
            
        return maxdist
            
            
                
