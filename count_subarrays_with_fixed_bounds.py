'''
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.
'''

def countSubarrays(self, A: List[int], minK: int, maxK: int) -> int:
        res = 0
        jmin = jmax = jbad = -1
        for i,a in enumerate(A):
            if not minK <= a <= maxK: jbad = i
            if a == minK: jmin = i
            if a == maxK: jmax = i
            res += max(0, min(jmin, jmax) - jbad)
        return res
        
---------------------------------------------------------------------------------------

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def split(seq):
            start = 0
            for idx, num in enumerate(seq):
                if num < minK or num > maxK:
                    if idx != start:
                        yield seq[start:idx]
                    start = idx + 1
            idx += 1
            if idx != start:
                yield seq[start:idx]

        def count(seq):
            nmi = -1  # index of nearest/rightest minK so far
            nma = -1  # index of nearest/rightest maxK so far
            ans = 0
            for idx, num in enumerate(seq):
                if num == minK:
                    nmi = idx
                if num == maxK:
                    nma = idx
                if nmi != -1 and nma != -1:
                    ans += min(nmi, nma) + 1
            return ans
                    
        ans = 0
        for seq in split(nums):
            ans += count(seq)
        return ans        
