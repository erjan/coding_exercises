'''
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
      
        pq = []

        heapq.heapify(pq)

        for i in range(len(nums)):

            heapq.heappush(pq, [nums[i],i] )
            if len(pq) > k:
                heapq.heappop(pq)

        pq.sort(key = lambda x: x[1])
        ans = []

        for i in range(len(pq)):
            ans.append(pq[i][0])
        return ans
