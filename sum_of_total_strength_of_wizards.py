'''
As the ruler of a kingdom, you have an army of wizards at your command.

You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:

The strength of the weakest wizard in the group.
The total of all the individual strengths of the wizards in the group.
Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.
'''

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        ans = 0 
        stack = []
        prefix = list(accumulate(accumulate(strength), initial=0))
        for i, x in enumerate(strength + [0]): 
            while stack and stack[-1][1] >= x: 
                mid = stack.pop()[0]
                lo = stack[-1][0] if stack else -1 
                left = prefix[mid] - prefix[max(lo, 0)]
                right = prefix[i] - prefix[mid]
                ans = (ans + strength[mid]*(right*(mid-lo) - left*(i-mid))) % 1_000_000_007
            stack.append((i, x))
        return ans 
