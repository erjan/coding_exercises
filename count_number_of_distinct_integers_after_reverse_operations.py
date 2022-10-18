'''
You are given an array nums consisting of positive integers.

You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.

Return the number of distinct integers in the final array.
'''

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        
        res = set(nums)
        
        for n in nums:
            
            n = int(str(n)[::-1])
            res.add(n)
            
        
        return len(res)
            
