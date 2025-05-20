You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:

Select a subset of indices within the range [li, ri] in nums.
Decrement the values at the selected indices by 1.
A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        pref = [0]*len(nums)
        for q in queries:
            a,b = q
            for i in range(a,b+1):
                pref[i] +=1
        
        print(pref)

        if any( p<n   for n,p in zip(nums,pref)):
            return False
        
        return True



-------------------------------------------------------------------------------------
