'''
You are given a 0-indexed integer array nums and two integers key and k. 
A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.
'''

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        l = list()
        for i in range(len(nums)):

            if nums[i] == key:
                l.append(i)

        total = list()
        for j in range(len(l)):

            for i in range(len(nums)):

                if abs(i - l[j]) <= k:
                    total.append(i)
        total = list(set(total))
        total.sort()
        print(total)
        return total
