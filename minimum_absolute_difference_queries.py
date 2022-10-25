'''
The minimum absolute difference of an array a is defined as the minimum value of |a[i] - a[j]|, where 0 <= i < j < a.length and a[i] != a[j]. If all elements of a are the same, the minimum absolute difference is -1.

For example, the minimum absolute difference of the array [5,2,3,7,2] is |2 - 3| = 1. Note that it is not 0 because a[i] and a[j] must be different.
You are given an integer array nums and the array queries where queries[i] = [li, ri]. For each query i, compute the minimum absolute difference of the subarray nums[li...ri] containing the elements of nums between the 0-based indices li and ri (inclusive).

Return an array ans where ans[i] is the answer to the ith query.

A subarray is a contiguous sequence of elements in an array.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
'''

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # location of number
        loc = defaultdict(list)
        for i, num in enumerate(nums):
            loc[num].append(i)
        
        # start from sorted key thus keep tracking minimum difference
        k = sorted(loc)
        
        res = []
        for a, b in queries:
            cands = []
            ans = float('inf')
            for c in k:
                # left and right range overlap means no available locations in range
                if bisect.bisect_left(loc[c], a) == bisect.bisect(loc[c], b): continue
                if cands: 
					ans = min(ans, c - cands[-1])
                cands.append(c)
            if ans == float('inf'): ans = -1
            res.append(ans)
        return res
