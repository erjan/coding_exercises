'''
You are given two sorted arrays of distinct integers nums1 and nums2.

A valid path is defined as follows:

Choose array nums1 or nums2 to traverse (from index-0).
Traverse the current array from left to right.
If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).
The score is defined as the sum of uniques values in a valid path.

Return the maximum score you can obtain of all possible valid paths. Since the answer may be too large, return it modulo 109 + 7.
'''


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = score1 = score2 = maxScore = 0
        m, n = len(nums1), len(nums2)
        MOD = 10 ** 9 + 7
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                score1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                score2 += nums2[j]
                j += 1
            else:
                maxScore += nums1[i] + max(score1, score2)
                maxScore %= MOD
                score1 = score2 = 0
                i += 1
                j += 1
        
        while i < m:
            score1 += nums1[i]
            i += 1
        while j < n:
            score2 += nums2[j]
            j += 1
        
        maxScore += max(score1, score2)
        return maxScore % MOD
      
----------------------------------------------------------------------------------------------------------
def maxSum(self, arr1, arr2):
        m=len(arr1)
        n=len(arr2)
        sum1=0
        sum2=0
        ans=0
        
        i=0
        j=0
        while i<m and j<n:
            if arr1[i]<arr2[j]:
                sum1+=arr1[i]
                i+=1
                
            elif arr1[i]>arr2[j]:
                sum2+=arr2[j]
                j+=1
                
            else:
                ans += arr1[i] + max(sum1,sum2)
                sum1=0
                sum2=0
                i+=1
                j+=1
                
        while i<m:
            sum1+=arr1[i]
            i+=1
            
        while j<n:
            sum2+=arr2[j]
            j+=1
            
        ans += max(sum1,sum2)
        
        return ans%((10**9)+7)
