'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1): nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)  
        
        left, right = 0, m-1
        while True:
            pointer1 = left + (right-left) // 2
            pointer2 = (m+n)//2 - pointer1 - 2
            
            left1 = nums1[pointer1] if pointer1 in range(m) else -math.inf
            left2 = nums2[pointer2] if pointer2 in range(n) else -math.inf
            right1 = nums1[pointer1+1] if pointer1+1 in range(m) else math.inf
            right2 = nums2[pointer2+1] if pointer2+1 in range(n) else math.inf
            
            if left1 <= right2 and left2 <= right1:
                if (m+n) % 2 == 0: return (max(left1, left2) + min(right1, right2)) / 2
                else: return min(right1, right2)
                
            elif left1 > right2: right = pointer1 - 1
            else: left = pointer1 + 1
