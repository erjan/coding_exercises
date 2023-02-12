'''
You are given a 0-indexed integer array nums.

The concatenation of two numbers is the number formed by concatenating their numerals.

For example, the concatenation of 15, 49 is 1549.
The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:

If there exists more than one number in nums, pick the first element and last element in nums respectively and add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.
If one element exists, add its value to the concatenation value of nums, then delete it.
Return the concatenation value of the nums.
'''

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0 
        for i in range((n+1)//2): 
            if i == n-1-i: ans += nums[i]
            else: ans += int(str(nums[i]) + str(nums[n-1-i]))
        return ans 
      
------------------------------------------------------------------
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        result=0
        while(i<=j):
            if i!=j :
                result+=int(str(nums[i])+str(nums[j]))
            else:
                result+=nums[i]
            i=i+1
            j=j-1
        return result


