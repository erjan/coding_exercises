'''
Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.


 '''

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:        
        heapq.heapify(nums)

        for _ in range(k):
            heapq.heappush(nums, -heapq.heappop(nums))
        return sum(nums)
