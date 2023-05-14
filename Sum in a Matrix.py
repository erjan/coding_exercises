'''
You are given a 0-indexed 2D integer array nums. Initially, your score is 0. Perform the following operations until the matrix becomes empty:

From each row in the matrix, select the largest number and remove it. In the case of a tie, it does not matter which number is chosen.
Identify the highest number amongst all those removed in step 1. Add that number to your score.
Return the final score.
'''


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:

        score = 0
        for i in range(len(nums)):
            row = nums[i]

            nums[i] = sorted(row, reverse=True)

        qq = list(zip(*nums))

        for col in qq:
            score += max(col)

        return score
    
------------------------------------------------------------------------------------
#solution using maxheaps

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        num_rows, num_cols = len(nums), len(nums[0])
        max_heaps = [[] * num_cols for _ in range(num_rows)]
        for r, row in enumerate(nums):
            for e in (row):
                heapq.heappush(max_heaps[r], -e)
        
        score = 0
        for _ in range(num_cols):
            curr_max = 0
            for r, max_heap in enumerate(max_heaps):
                curr_max = max(curr_max, -heapq.heappop(max_heap))
            score += curr_max
        return score
