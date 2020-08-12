'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n = nums
        counts = dict()
        left_indices = dict()
        min_length = 0
        degree = 0

        for i in range(len(n)):
            if n[i] not in left_indices:
                left_indices[n[i]] = i

            if n[i] not in counts:
                counts[n[i]] = 1
            else:
                counts[n[i]]+=1
            if counts[n[i]] > degree:
                degree = counts[n[i]]
                min_length = i - left_indices[n[i]] + 1
            elif counts[n[i]] == degree:
                min_length = min(min_length, i - left_indices[n[i]]+1)
        return min_length
