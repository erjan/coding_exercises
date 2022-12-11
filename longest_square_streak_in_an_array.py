'''
You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 
 '''

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        # sorting the input list
        nums.sort()

        # Initialize a dict with the nums values as key and 1 as values
        # Since every number is part of its own streak 
        seq_dict = {k:1 for k in nums}

        for num in nums:

            # Calculating the square root of number
            sqrt_num = sqrt(num)

            # If number has a perfect square and that square is present in dict too
            # Increase the count of square streak by 1
            if isqrt(num) and sqrt_num in seq_dict:
                seq_dict[num] = seq_dict[sqrt_num] + 1

        # Getting the max value of dict values aka sqaure streak
        max_val = max(seq_dict.values())

        # Return -1 if the max = 1 else that max values
        return -1 if max_val < 2 else max_val
      
-------------------------------------------------------------------------------------------------
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans, buf = -1, {}
        for n in reversed(sorted(nums)):
            buf[n] = buf.get(n*n, 0) + 1
            if buf[n] > 1:
                ans = max(ans, buf[n])
        return ans
