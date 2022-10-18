'''
You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.
'''

**
For every position we try to get a point or advantage
To get a point lets say for 2 we have choices [3,10] the we should use 3 not 10 as we can get advantage from both of them but using less valuable item can be good in the long run .
To do so we sort num1 and find the index with value just greater than item in nums2 : if no such index exists add the smallest we have
**

class Solution:
    def binarySearch(self , arr , x):
        low = 0 
        high = len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] <= x:low = mid + 1
            else: high = mid - 1
        return low
    
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        n = len(nums1)
        ans = []
        for i in nums2:
            idx = self.binarySearch(nums1 , i)
            if idx == n: idx = 0
            ans.append(nums1[idx])
            nums1.pop(idx)
            n-=1
        return ans
