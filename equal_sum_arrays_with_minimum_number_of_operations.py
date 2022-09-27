'''
You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

 
 '''

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2:
            s1, s2 = s2, s1
            nums1, nums2 = nums2, nums1
        # to make s1 < s2            
        heapq.heapify(nums1)            
        nums2 = [-num for num in nums2]
        heapq.heapify(nums2)            
        ans = 0
        diff = s2 - s1
        while diff > 0 and nums1 and nums2:
            a = 6 - nums1[0]
            b = - (1 + nums2[0])
            if a > b:
                heapq.heappop(nums1)                
                diff -= a
            else:
                heapq.heappop(nums2)                
                diff -= b
            ans += 1                
        while diff > 0 and nums1:            
            a = 6 - heapq.heappop(nums1)                
            diff -= a
            ans += 1                
        while diff > 0 and nums2:            
            b = - (1 + heapq.heappop(nums2))
            diff -= b
            ans += 1                
        return ans if diff <= 0 else -1
