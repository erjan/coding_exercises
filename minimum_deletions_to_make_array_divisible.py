'''
You are given two positive integer arrays nums and numsDivide. You can delete any number of elements from nums.

Return the minimum number of deletions such that the smallest element in nums divides all the elements of numsDivide. If this is not possible, return -1.

Note that an integer x divides y if y % x == 0.
'''

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        nums.sort()
        x = reduce(gcd, numsDivide)
        
        count = 0
        for num in nums:
            if x%num == 0:
                return count
            count+=1
        return -1     
