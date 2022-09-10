'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        
        longest = 0
        
        for n in nums:
            #check if its the start of sequence
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length+=1
                longest = max(longest, length)
        return longest
