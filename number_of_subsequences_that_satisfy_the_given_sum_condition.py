'''
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.
'''

Let the first pointer be at index 0 and last pointer be at index n-1.

Steps to follow:

Sort the array
Find the start and endindex such that A[start] + A[end] <= target
Let's say we have the required start index i and end index j.
a. For all the index starting from i+1 to j, we can choose either include it our set or ignore it
b. Meaning for every index from i+1 to j we have two options
c. Therefore the total count of subsets would be 2**(j-i)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        nums.sort()
        ans = 0
        while left <= right:
            val = nums[left] + nums[right]
            if val > target:
                right-=1
            else:
                ans += pow(2,right-left,10**9+7)
                left+=1
        return ans % (10**9 + 7)
      
---------------------------------------------------------------------------------------------------------      
