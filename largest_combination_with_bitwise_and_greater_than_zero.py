'''
The bitwise AND of an array nums is the bitwise AND of all integers in nums.

For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.

Return the size of the largest combination of candidates with a bitwise AND greater than 0.
'''

    def largestCombination(self, A):
        return max(sum(1 << i & a > 0 for a in A) for i in range(30))
    
---------------------------------------------------------------------
class Solution:
    def largestCombination(self, cands: List[int]) -> int:
        grps = [0] * 24
        for c in cands:
            for i, b in enumerate(bin(c)[2:][::-1]):
				grps[i] += (b == '1')
        return max(grps)
