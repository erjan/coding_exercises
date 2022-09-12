'''
Given an integer array nums, return the maximum difference 
between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.
'''

from functools import reduce
class Solution(object):
        def maximumGap(self, nums):
            if len(nums) == 1:
                return 0
            
            sorted_array = self.radix_sort(nums)
            max_gap = self.maximum_Gap(sorted_array)
            return max_gap
            
                
        def radix_sort(self, nums):
            num_digits = len(str(max(nums)))
            A = nums 
            for i in range(num_digits):
                B = [[] for _ in range(10)]
                for num in A:
                    bucket = (num // (10 ** i)) % 10
                    B[bucket].append(num)
                A = reduce(lambda x, y: x+y, B)
                
            return A
            
                
        def maximum_Gap(self, sorted_array):
            max_gap = -float('inf')
            for i in range(1, len(sorted_array)):
                if sorted_array[i] - sorted_array[i-1] >= max_gap:
                    max_gap = sorted_array[i] - sorted_array[i-1]
            
            return max_gap
---------------------------------------------------------------------------
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        hi, lo, ans = max(nums), min(nums), 0
        bsize = (hi - lo) // (len(nums) - 1) or 1
        buckets = [[] for _ in range(((hi - lo) // bsize) + 1)]
        for n in nums:
            buckets[(n - lo) // bsize].append(n)
        currhi = 0
        for b in buckets:
            if not len(b): continue
            prevhi, currlo = currhi or b[0], b[0]
            for n in b: 
                currhi, currlo = max(currhi, n), min(currlo, n)
            ans = max(ans, currlo - prevhi)
        return ans
