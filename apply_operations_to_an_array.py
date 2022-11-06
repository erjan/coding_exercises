'''
You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.

For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
Return the resulting array.

Note that the operations are applied sequentially, not all at once.
'''

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        i = 0
        n = len(nums)
        while i < n-1:
            if nums[i] == nums[i+1]:
                nums[i]= nums[i]*2
                nums[i+1] = 0
            
            i+=1
        res = []

        if nums.count(0) == 0:
            return nums
        z = nums.count(0)

        for i in range(n):
            if nums[i] != 0:
                res.append(nums[i])
        res.extend(z*[0])
        return res
      
-------------------------------------------------------------------------------------------------------
class Solution:
    def applyOperations(self, n):

        # apply the first part of operations
        for i in range(1,len(n)):
            if n[i] == n[i-1]:
                n[i-1], n[i] = n[i-1]*2, 0    
        
        # 'not' of any non-zero number is equal to 0, i.e.,
        # less than 'not 0' which is 1 (here, sorting is stable)
        return sorted(n, key=lambda x: not x)
            
