'''
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.
'''

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
	
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i):
                nums[j] = (nums[j] + nums[j + 1]) % 10
          
        return nums[0]
      
-------------------------------------------------------------------------
class Solution:
  def triangularSum(self, nums: List[int]) -> int:

      arr=nums.copy()
      lst=[]
      while len(arr)!=1:
        for i in range(0,len(arr)-1):
          s=arr[i]+arr[i+1]
          lst.append(s%10)   #to get the last digit of integer sum
        arr=lst.copy()
        lst=[]
      return arr[0]
