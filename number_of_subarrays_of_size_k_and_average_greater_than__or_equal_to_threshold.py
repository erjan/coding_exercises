'''
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.
'''

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ptr1, ptr2 = 0, k-1
        subSum = 0
        for idx in range(k):
            subSum += arr[idx]
        count = 1 if (subSum/k) >= threshold else 0 
        while ptr2 < len(arr)-1:
            subSum -= arr[ptr1]
            ptr1 += 1
            ptr2 += 1
            subSum += arr[ptr2]
            count += 1 if (subSum/k) >= threshold else 0 
        return count
        
--------------------------------------------        


class Solution:
    def numOfSubarrays(self, A, k, target):     
        # NOTE:
        #     1) Since avg = sum/k , and "k" is fixed, we can work with the (minimum) "sum" directly .
        #        Therefore, we should multiply "target" by "k"
        target *= k
        #
        # s: temporary "sum" for the latest sub-array of size k
        s = 0
        for i in range(k):
            s += A[i]
        # res: Final result counter
        res     = 1 if s>=target else 0
        #
        for i in range( len(A) - k ):
            s   += - A[i] + A[i+k]
            res += 1 if s>=target else 0
        return res
        
------------------------------------------------------------------------------------------------------------------
class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        windowStart = 0
        max_avg = 0
        avg = 0
        c=0
        result = []
        windowSum = 0
        for windowEnd in range(len(arr)):
            windowSum += arr[windowEnd]
            if((windowEnd)>=k-1):
                avg = windowSum//k
                result.append(avg)
                windowSum -= arr[windowStart]
                windowStart += 1
        for i in range(len(result)):
            if(result[i]>=threshold):
                c=c+1
        return c
        
--------------------------------------------------------------------------------        
