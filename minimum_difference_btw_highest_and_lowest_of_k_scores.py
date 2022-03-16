
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

    


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        nums.sort()
        res = math.inf
        
        for i in range(len(nums)-k+1): #this is important!!! -k+1 , +1 is needed! otherwise wrong answer!

            sliding_window = nums[i: (i+k)]
            cur = max(sliding_window) - min(sliding_window)
            if cur < res:
                #print('found new low: ', cur)

                res = cur
        print(res)
        return res    
