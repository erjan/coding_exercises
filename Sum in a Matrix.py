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
