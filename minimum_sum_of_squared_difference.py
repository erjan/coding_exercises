'''
You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

Note: You are allowed to modify the array elements to become negative integers.
'''


from sortedcontainers import SortedDict
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = []
        for num1, num2 in zip(nums1, nums2):
            diff.append(abs(num1-num2))
        
        k = k1 + k2
        
        count = SortedDict(Counter(diff))
        print(diff, count)
        
        if k - sum(diff) >= 0:
            return 0
        
        while k > 0:
            key, value = count.popitem()
            if k >= value:
                k -= value
                count[key - 1] = count.get(key - 1, 0) + value
            elif k < value:
                count[key] = value - k
                count[key - 1] = count.get(key - 1, 0) + k
                k = 0
                
        res = 0
        for key, val in count.items():
            res += key ** 2 * val
            
        return res
