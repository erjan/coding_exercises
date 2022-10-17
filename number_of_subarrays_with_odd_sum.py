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
    
----------------------------------------------------------------------------------------------------------------------
Explanation
cur = 0 if current prefix sum is even
cur = 1 if current prefix sum is odd
count[0] is the number of even prefix sum
count[1] is the number of odd prefix sum

For each element in A:
if current prefix sum is even, res += the number of odd prefix sum
if current prefix sum is odd, res += the number of even prefix sum


More Explanation
All by @Anonymouso:

Basically the way it works is -
If you add an odd number to an even number - you get an odd number (4+1 = 5, 1+2 = 3, 7+12 = 19 etc.)
If you add an even number to an odd number - same result as above obviously.
if you add an even number to an even number - you get an even number (4 + 2 =6, 8+6 = 14 etc.)
If you add an odd number to an odd number - you get an even number ( 1+1 = 2, 5 +7 = 12 etc.)

Based on the above table of options, you need to pick only 2 options > add odd number to even number & add even number to odd number.
What lee is doing is basically counting the amount of "odd" prefix sums he sees and "even prefix sums he sees.
As he does that:
if the current subarray sum is odd - that means that we need to add all the number of even sub arrays we saw so far to the result.
if the current subarray sum is even - that means that we need to add all the number of odd sub arrays we saw so far to the result.

