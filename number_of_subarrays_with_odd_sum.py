'''
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.


odd + odd = even             //   5 + 5 =  10
odd + even = odd             //   5 + 2 =  7         

even + odd = odd             //   2 + 5 = 7
even + even = even           //   2 + 2 = 4
'''

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        even = 1 #(sum zero before array start)
        odd = 0
        rsum = 0
        for i in range(len(arr)):
            rsum += arr[i]
            if rsum % 2 == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % (10**9 + 7)
      
----------------------------------------------------------------------------------------------      
