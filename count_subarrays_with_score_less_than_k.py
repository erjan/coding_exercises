'''
The score of an array is defined as the product of its sum and its length.

For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

A subarray is a contiguous sequence of elements within an array.
'''

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # p[i] = nums[:i]
        # num[i] + ...+ num[j] = p[j+1] - p[i]
        p = [0]
        for num in nums :
            p.append(p[-1] + num)

        left = 0 
        res = 0 
        for i in range(1, len(nums)+1):
            val = (p[i] - p[left]) * ( i - left)
            while val >= k and left < i : 
                left += 1 
                val = (p[i] - p[left]) * ( i - left)
            res += i  - left
        return res
     
---------------------------------------------------------------
class Solution:
    def countSubarrays(self, xs: List[int], k: int) -> int:
        n = len(xs)

        i, j, sub_sum = 0, 0, 0
        ans = 0
        while j < n:
            sub_sum += xs[j]
            if sub_sum * (j - i + 1) < k:
                ans += j - i + 1
                j += 1
            elif i == j:
                sub_sum = 0
                j += 1
                i = j
            else:
                sub_sum -= xs[i] + xs[j]
                i += 1
                
        return ans
      
---------------------------------------------------------------------------------
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i, start = 0, 0
        n = len(nums)
        val, ans, sums = 1, 0, 0
        
        while i < n:
            sums += nums[i]
            val = sums * (i-start+1)
            while start <= i and val >= k:
                sums -= nums[start]
                start += 1
                val = sums * (i-start+1)
            ans += (i-start+1)
            i += 1
        
        return ans
