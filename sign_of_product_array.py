'''
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
'''

#my own solution

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if nums.count(0) != 0:
            return 0
        else:
            neg_counter = 0
            for i in range(len(nums)):
                if nums[i] < 0:
                    neg_counter +=1

            if neg_counter % 2 == 0:
                return 1
            else:
                return -1
