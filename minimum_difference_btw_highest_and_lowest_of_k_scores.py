
'''
You are given a 0-indexed integer array nums, where nums[i] represents 
the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference 
between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.
'''


#MLE solution bad



class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        total = math.inf
        res = list(itertools.combinations(nums, k))
        for l in res:
            cur = max(l) - min(l)

            if cur < total:
                total = cur
        print(total)
        return total
