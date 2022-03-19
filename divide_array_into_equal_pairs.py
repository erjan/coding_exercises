'''
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
'''

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        n = nums
        n.sort()
        pairs = len(n)//2
        i = 0
        while i < len(n)-1:

            if n[i] != n[i+1]:
                return False 
            i+=2
        return True
