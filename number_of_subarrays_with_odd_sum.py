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

 def numOfSubarrays(self, A):
        # prefix sum means the sum of all numbers up to that index
        # count = [the number of even prefix sums, the number of odd prefix sums]
        # we start with 1 even prefix sum because 0 is even
        count = [1, 0]
        # initialize the current prefix sum (cur) as being even and initialize the result as 0
        cur = res = 0
        # go through each of the numbers in the array
        for a in A:
            # see if the next number is odd (which is what a&1 is doing since it's a bitwise AND operator), and use the exclusion OR operator to see if the current number and the previous number add up to being even (0) or odd (1)
            # this can also be written as cur = (cur + (a % 2))%2
            cur ^= a & 1
            # if the prefix sum is even, then add the number of odd prefix sums to the results. If the prefix sum is odd, then add the number of even prefix sums to the result.
            res += count[1 - cur]
            # increase the counter for the number of even or odd prefix sums seen so far
            count[cur] += 1
        return res % (10**9 + 7)
