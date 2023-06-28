'''
You are given a 0-indexed integer array nums representing the score of students 
in an exam. The teacher would like to form one non-empty group of students with maximal 
strength, where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].

Return the maximum strength of a group the teacher can create.
'''


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
          
        pos = []
        neg = []
      
        for n in nums:
            if n < 0:
                neg.append(n)
            elif n > 0:
                pos.append(n)        
        res = 1

        neg.sort(reverse=True)
        if len(neg)%2 == 1:
            neg.remove(neg[0])
        
        if not neg and not pos:
            return 0
        
        for p in pos:
            res = res* p
        for n in neg:
            res = res * n
        return res
---------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        return max(prod(combo) for size in range(1, len(nums) + 1) for combo in combinations(nums, size))
        
