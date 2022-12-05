    
'''
You are given two 0-indexed integer arrays nums and removeQueries, both of length n. For the ith query, the element in nums at the index removeQueries[i] is removed, splitting nums into different segments.

A segment is a contiguous sequence of positive integers in nums. A segment sum is the sum of every element in a segment.

Return an integer array answer, of length n, where answer[i] is the maximum segment sum after applying the ith removal.

Note: The same index will not be removed more than once.



Here, I use

a ordered set to store the points where nums are divided;
a hash table mapping from left boundary to right boundary to validate if a triplet is still effective;
a priority queue to the triplet of <range sum, left boundary, right boundary>.
At each query, I add the point to the set of dividers, adjust the mapping of its left 
and right boundary points, and add the new two pieces to the priority queue. While finding current maximum 
from the priority queue, I first validate if the triplet is still in effect by checking if the left
boundary matches the right boundary
in the hash table. If not, I discard the top element until a valid triplet.
'''

from sortedcontainers import SortedList

class Solution: 
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        sl = SortedList([-1, n])
        prefix = list(accumulate(nums, initial=0))
        mp = {-1 : n}
        pq = [(-prefix[-1], -1, n)]
        
        ans = []
        for q in removeQueries: 
            sl.add(q)
            i = sl.bisect_left(q)
            lo = sl[i-1]
            hi = sl[i+1]
            mp[lo] = q
            mp[q] = hi 
            heappush(pq, (-(prefix[q]-prefix[lo+1]), lo, q))
            heappush(pq, (-(prefix[hi]-prefix[q+1]), q, hi))
            
            while mp[pq[0][1]] != pq[0][2]: heappop(pq)
            ans.append(-pq[0][0])
        return ans 
      
---------------------------------------------------------------------------------------------------------------      


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        acc = [0]
        # prefix sum
        for num in nums:
            acc.append(acc[-1] + num)
        
        # current max sum with boundries
        q = [(-sum(nums), 0, n - 1)]
        # removed index
        rm_idx = []
        
        
        ans = []
        for idx in removeQueries:
            bisect.insort(rm_idx, idx)
            while q:
                _, s, e = q[0]
                loc = bisect.bisect_left(rm_idx, s)
                idx = rm_idx[min(loc, len(rm_idx) - 1)]
                # if removed index fall between the boundry of largest sum
                if idx > e or idx < s: break
                heappop(q)
                if s < idx:
                    heappush(q, (-(acc[idx] - acc[s]), s, idx - 1))
                if e > idx:
                    heappush(q, (-(acc[e + 1] - acc[idx + 1]), idx + 1, e))
            if q:
                ans.append(-q[0][0])
            else:
                ans.append(0)
            
        
        return ans
