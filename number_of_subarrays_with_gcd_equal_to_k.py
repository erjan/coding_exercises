'''
Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The greatest common divisor of an array is the largest integer that evenly divides all the array elements.
'''


class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b , a % b)
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            present_gcd = 0
            for j in range(i , len(nums)):
                present_gcd = gcd(present_gcd, nums[j])
                if present_gcd == k:
                    count += 1
                    
        return count
      
--------------------------------------------------------------------------------------
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
                                        
        ans = 0                             #   Ex: nums = [9,3,1,3]
                                            #
        for i, num in enumerate(nums):      #   num  next   G   ans
            G = num                         #   –––  ––––  –––  ––– 
                                            #    9     9    9    0
            for next in nums[i:]:           #    9     3    3    1
                                            #    9     1    1    1
                G = gcd(G,next)             #    3     3    3    2
                ans+= (G == k)              #    3     1    1    2
                if G < k: break             #    1     1    1    2
                                            #    3     3    3    3  <-- answer
        return ans
