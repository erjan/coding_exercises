'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
'''


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        
        d = dict()
        res = 0
        
        
        for i in nums1:
            for j in nums2:
                t = -(i+j)
                if t in d:
                    d[t] +=1
                else:
                    d[t] = 1
        
        for k in nums3:
            for q in nums4:
                
                t = k+q
                if t in d:
                    res += d[t]
        return res
