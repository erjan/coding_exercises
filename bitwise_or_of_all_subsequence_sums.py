'''
Given an integer array nums, return the value of the bitwise OR of the sum of all possible subsequences in the array.

A subsequence is a sequence that can be derived from another sequence by removing zero or more elements without changing the order of the remaining elements.
'''
 
  
'''  
Intuition
The set bit of the final result has two possible sources

set bit in one of an original number;
set bit as a result of a subsequence sum.
For the 2nd source where the set bit is carried over from lower bits, you can always get the 
it from a prefix sum. As a result, the solution is like below.

'''

class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        ans = prefix = 0 
        for x in nums: 
            prefix += x
            ans |= x | prefix 
        return ans
