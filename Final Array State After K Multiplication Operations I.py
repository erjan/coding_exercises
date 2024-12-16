'''
You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.
'''

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        heap = []
        for ind,val in enumerate(nums):
            heapq.heappush(heap, [val,ind])
        
        for i in range(k):

            val,ind = heapq.heappop(heap)
            newval = val*multiplier
            heapq.heappush(heap, [newval,ind])
        
        for val,ind in heap:
            nums[ind] = val
        return nums
