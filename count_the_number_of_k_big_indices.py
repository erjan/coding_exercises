'''
You are given a 0-indexed integer array nums and a positive integer k.

We call an index i k-big if the following conditions are satisfied:

There exist at least k different indices idx1 such that idx1 < i and nums[idx1] < nums[i].
There exist at least k different indices idx2 such that idx2 > i and nums[idx2] < nums[i].
Return the number of k-big indices.
'''


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        prefix = [False] * len(nums)
        pq = []
        for i, x in enumerate(nums): 
            if len(pq) == k and -pq[0] < x: prefix[i] = True
            heappush(pq, -x)
            if len(pq) > k: heappop(pq)
        ans = 0 
        pq = []
        for i, x in reversed(list(enumerate(nums))): 
            if len(pq) == k and -pq[0] < x and prefix[i]: ans += 1
            heappush(pq, -x)
            if len(pq) > k: heappop(pq)
        return ans
------------------------------------------------------------------------------------------------
from sortedcontainers import SortedList

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        lo = SortedList()
        hi = SortedList(nums)
        ans = 0 
        for x in nums: 
            if lo.bisect_left(x) >= k and hi.bisect_left(x) >= k: ans += 1
            lo.add(x)
            hi.remove(x)
        return ans 
      
