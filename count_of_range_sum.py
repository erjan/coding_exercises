'''
Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.
'''


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix,thisSum,ans = [0],0,0
        for n in nums:
            thisSum += n
            ans += bisect.bisect_right(prefix, thisSum-lower) - bisect.bisect_left(prefix, thisSum-upper)
            bisect.insort(prefix, thisSum)
        return ans
----------------------------------------------------------
def countRangeSum(self, nums, lower, upper):
    n = len(nums)
    Sum, BITree = [0] * (n + 1), [0] * (n + 2)
    
    def count(x):
        s = 0
        while x:
            s += BITree[x]
            x -= (x & -x)
        return s
    
    def update(x):
        while x <= n + 1:
            BITree[x] += 1
            x += (x & -x)
            
    for i in range(n):
        Sum[i + 1] = Sum[i] + nums[i]
    sortSum, res = sorted(Sum), 0
    for sum_j in Sum:
        sum_i_count = count(bisect.bisect_right(sortSum, sum_j - lower)) - count(bisect.bisect_left(sortSum, sum_j - upper))
        res += sum_i_count
        update(bisect.bisect_left(sortSum, sum_j) + 1)
    return res
------------------------------------------------------------------------------------------
import bisect

class FenwickTree:
    def __init__(self, n: int) -> None:
        self.BIT = [0] * (n+1)
    
    def sum(self, n: int) -> int:
        rv = 0
        while n > 0:
            rv += self.BIT[n]
            n -= n & -n
        return rv
    
    def increment(self, n: int) -> None:
        while n < len(self.BIT):
            self.BIT[n] += 1
            n += n & -n
            
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sums = [0] * (len(nums)+1)
        for i, n in enumerate(nums):
            sums[i+1] = sums[i] + n
        sortedSums = sorted(sums)
        ranks = {s: i+1 for i, s in enumerate(sortedSums)}
        ft = FenwickTree(len(sums))
        rv = 0
        for s in sums:
            rv += (ft.sum(bisect.bisect_right(sortedSums, s-lower)) -
                   ft.sum(bisect.bisect_left(sortedSums, s-upper)))
            ft.increment(ranks[s])
        return rv
      
----------------------------------------------------------------------------
What this does is using prefix sums, and then for each presum, search in the ordered previously inserted list of presums both the smallest and largest sum to subtract from it. As long as the index of the smallest acceptable presum is within the range of bisect search, we add to our count of acceptable answers up until the largest acceptable one or to the end of the presum list.

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sums = list(accumulate(nums))
        inserts = [0]
        ans = 0
        
        for sum in sums:
            idxLow = bisect_left(inserts, sum-upper)
            idxHigh = bisect_right(inserts, sum-lower) - 1

            if idxLow < len(inserts):
                ans += min(idxHigh, len(inserts)-1) - idxLow + 1
            insort(inserts, sum)
  
        return ans
