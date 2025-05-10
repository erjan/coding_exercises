'''
You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.
'''
-----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        res = -1

        s1 = sum(nums1)
        s2 = sum(nums2)

        if s1 > s2:
            diff = s1-s2
        else:
            diff = s2-s1

        rem = diff
        if (nums1.count(0) > 0 and nums2.count(0) == 0 and rem!=0) or (nums1.count(0)== 0 and nums2.count(0)>0 and rem!=0):
            return -1

        nums1.sort()
        nums2.sort()

        p1 = 0
        p2 = 0

        return diff



-------------------------------------------
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, zero1=sum(nums1), nums1.count(0)
        sum2, zero2=sum(nums2), nums2.count(0)
        if (zero1==0 and sum1<sum2+zero2)or(zero2==0 and sum2<sum1+zero1):
            return -1
        return max(sum1+zero1, sum2+zero2)
        
        

