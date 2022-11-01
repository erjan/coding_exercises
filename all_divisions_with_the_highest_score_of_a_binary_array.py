'''
You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:

numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums between index i and n - 1 (inclusive).
If i == 0, numsleft is empty, while numsright has all the elements of nums.
If i == n, numsleft has all the elements of nums, while numsright is empty.
The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.

Return all distinct indices that have the highest possible division score. You may return the answer in any order.
'''


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dev_scores = [0] * (len(nums) + 1)
        dev_scores[0] = max_score = sum(nums)
        
        for i, v in enumerate(nums, 1):
            dev_scores[i] = dev_scores[i - 1] + (1 if v == 0 else -1)
            max_score = max(max_score, dev_scores[i])
        
        return [i for i, score in enumerate(dev_scores) if score == max_score]
      
------------------------------------------------------------------------------------------------------------------------------------
Main Idea
Step 1. Expand from left to right to calculate 0s
Step 2. Expand from right to left to calculate 1s
Step 3. Calculate Sum of zeroFromLeft and oneFromRight and return where maximum value's index

Complexity Analysis
Time: O(n) : Let n be nums's length
Space: O(n): Store zeroFromLeft and oneFromRight take O(n)
Code

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeroFromLeft = [0] * (len(nums) + 1)
        oneFromRight = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroFromLeft[i + 1] = zeroFromLeft[i] + 1
            else:
                zeroFromLeft[i + 1] = zeroFromLeft[i]
                
        for i in range(len(nums))[::-1]:
            if nums[i] == 1:
                oneFromRight[i] = oneFromRight[i + 1] + 1
            else:
                oneFromRight[i] = oneFromRight[i + 1]
        
        allSum = [0] * (len(nums) + 1)
        currentMax = 0
        res = []
        for i in range(len(nums) + 1):
            allSum[i] = oneFromRight[i] + zeroFromLeft[i]
            if allSum[i] > currentMax:
                res = []
                currentMax = allSum[i]
            if allSum[i] == currentMax:
                res.append(i)
        return res
