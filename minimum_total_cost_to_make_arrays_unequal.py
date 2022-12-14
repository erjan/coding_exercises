'''
You are given two 0-indexed integer arrays nums1 and nums2, of equal length n.

In one operation, you can swap the values of any two indices of nums1. The cost of this operation is the sum of the indices.

Find the minimum total cost of performing the given operation any number of times such that nums1[i] != nums2[i] for all 0 <= i <= n - 1 after performing all the operations.

Return the minimum total cost such that nums1 and nums2 satisfy the above condition. In case it is not possible, return -1.
'''

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        arr = []
        n = len(nums1)
        hmap = defaultdict(int)
        mx = -1
        for i in range(n):
            if nums1[i] == nums2[i]: #creating arr of indexes which has equal element in both array.
                arr.append(i)
                hmap[nums1[i]] += 1
            if hmap[nums1[i]] > mx: #finding max freq element and its freq.
                mxOcc = nums1[i]
                mx = hmap[nums1[i]]
        sz = len(arr)
        if mx <= sz//2: #condition 2
            return sum(arr)
        else:
            req = (2*mx) - len(arr) #count of extra index to add from nums1 array.
            i = 0
            while i < n and req > 0:
                if nums1[i] != nums2[i] and nums1[i] != mxOcc and nums2[i] != mxOcc: #condition explained in step 4
                    req -= 1
                    arr.append(i)
                i += 1
            return sum(arr) if req == 0 else -1
-------------------------------------------------------------------------------------
from collections import Counter
class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        res = 0
        d = Counter()
        t = 0
        most = 0
        v = None
        for i,(x,y) in enumerate(zip(nums1, nums2)):
            if x == y:
                res += i
                t += 1
                d[x] += 1 
                if d[x] > most:
                    most = d[x]
                    v = x
        if 2*most <= t:
            return res
        k = 2*most - t
        for i, (x,y) in enumerate(zip(nums1, nums2)):
            if x != y and x != v and y != v:
                res += i
                k -= 1
            if k == 0: return res
        return -1

        
            
                
