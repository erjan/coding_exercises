'''
You are given an integer array nums​​​ and an integer k. You are asked to distribute this array into k subsets of equal size such that there are no two equal elements in the same subset.

A subset's incompatibility is the difference between the maximum and minimum elements in that array.

Return the minimum possible sum of incompatibilities of the k subsets after distributing the array optimally, or return -1 if it is not possible.

A subset is a group integers that appear in the array with no particular order.
'''

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        d=len(nums)//k # the length of each partition
        
        @lru_cache(None)
        def helper(nums):
            if not nums:
                return 0
            ret=10**15
            for a in combinations(nums,d): # choose a as a partition
                if len(set(a))<d: # check for duplicates
                    continue
                left=list(nums) # numbers left after removing partition a
                for v in a:
                    left.remove(v)
                ret=min(ret,max(a)-min(a)+helper(tuple(left)))
            return ret
        
        ans=helper(tuple(nums)) # turn the input into a tuple so the function can be cached
        return ans if ans!=10**15 else -1
