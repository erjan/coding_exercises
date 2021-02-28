'''
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr
'''

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_final = 0
        n = arr
        sum_final += sum(n)
        for i in range(3,107,2):

            t = i
            for j in range(len(n)-(i-1)):
                sub_array = n[j:j+t]
                print(sub_array)
                sum_final+= sum(sub_array)
        print(sum_final)
        return sum_final
