'''
Given an array of integers nums, sort the array in increasing order based 
on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
'''


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        s= collections.Counter(nums)
        
        nums.sort(key = lambda x: (s[x], -x))
        return nums
