'''
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.
'''


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        heap = [-i for i in nums]
        heapq.heapify(heap)
        
        for i in range(1, len(nums),2):
            nums[i] = -heapq.heappop(heap)
        
        for i in range(0, len(nums),2):
            nums[i] = -heapq.heappop(heap)
        
