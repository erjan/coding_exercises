'''
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.
'''


def validPartition(self, nums: List[int]) -> bool:
    dp = [False]*(len(nums)+1)
    dp[len(nums)] = True
    for i in range(len(nums)-1, -1, -1):
        if (i+1 < len(nums) and nums[i] == nums[i+1]):
            dp[i] = dp[i] or dp[i+2]
        if i+2 < len(nums):
            if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                dp[i] = dp[i] or dp[i+3]
            elif (nums[i+1]-nums[i] == 1 and nums[i+2]-nums[i+1] == 1):
                dp[i] = dp[i] or dp[i+3]
    return dp[0]
  
---------------------------------------------------------------------------------------------------------------
def validPartition(self, nums: List[int]) -> bool:
    dp = [-1]*(len(nums)+1)
    def trav(i=0):
        if i == len(nums):
            return True
        
        if dp[i] != -1:
            return (False if dp[i] == 0 else True)
        
        ans = False
        if (i+1 < len(nums) and nums[i] == nums[i+1]):
            ans = ans or trav(i+2)
        if i+2 < len(nums):
            if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                ans = ans or trav(i+3)
            elif(nums[i+1]-nums[i] == 1 and nums[i+2]-nums[i+1] == 1):
                ans = ans or trav(i+3)
        dp[i] = (0 if ans == False else 1)
        return ans
	return trav()

-------------------------------------------------------------------------------------------------------------------------------

'''
If we carefully observe, we are just using dp[i+2] and dp[i+3] states while calculating the answer for current state. so we can just the answer for next 3 states and still calculate the answer for current setp

Space Optimisation
'''

def validPartition(self, nums: List[int]) -> bool:
    #We are setting all of them to be true because if we take any number of steps from last index, the answer is true
    dp_1 = True #represents (i+1) state
    dp_2 = True #represents (i+2) state
    dp_3 = True #represents (i+3) state
    
    for i in range(len(nums)-1, -1, -1):
        cur = False #current dp state
        if (i+1 < len(nums) and nums[i] == nums[i+1]):
            cur = cur or dp_2
        if i+2 < len(nums):
            if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                cur = cur or dp_3
            elif (nums[i+1]-nums[i] == 1 and nums[i+2]-nums[i+1] == 1):
                cur = cur or dp_3
        dp_1, dp_2, dp_3 = cur, dp_1, dp_2
    return dp_1

------------------------------------------------------------------------------------------------------
n=len(nums)
        @cache
        def valid(i):
            if i==n:
                return True
            if i+1<n and nums[i]==nums[i+1] and valid(i+2):
                return True
            if i+2<n and nums[i]==nums[i+1]==nums[i+2] and valid(i+3):
                return True
            if i+2<n and nums[i]==nums[i+1]-1 and nums[i+1]==nums[i+2]-1 and valid(i+3):
                return True
        return valid(0)
      
---------------------------------------------------------------------------------------------------------------------
class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [False for _ in range(len(nums)+1)]
        dp[0] = True
        if nums[0] == nums[1]:
            dp[2] = True
        for i in range(3, len(nums)+1):
            if nums[i-1] == nums[i-2]:
                dp[i] = dp[i] or dp[i-2]
            if nums[i-1] == nums[i-2] == nums[i-3]:
                dp[i] = dp[i] or dp[i-3]
            if nums[i-1]-2 == nums[i-2]-1 == nums[i-3]:
                dp[i] = dp[i] or dp[i-3]
        return dp[-1]
