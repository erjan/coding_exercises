'''
You are given a 0-indexed integer array nums. In one operation, you may do the following:

Choose two integers in nums that are equal.
Remove both integers from nums, forming a pair.
The operation is done on nums as many times as possible.

Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.
'''

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = nums
        d = dict(Counter(pairs))

        left = 0
        npairs = 0
        for k, v in d.items():
            npairs += v//2
            left += v % 2
        print([npairs, left])
        return ([npairs, left])
 
---------------------------------------------------------------

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        notpair = []
        pairs = 0
        
        for i in range(len(nums)):
            if nums[i] not in notpair:
                notpair.append(nums[i])
            elif nums[i] in notpair:
                notpair.remove(nums[i])
                pairs+=1
                
        return [pairs, len(notpair)]
