Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.


  class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2):

            sub3 = nums[i:i+3]

            a,b,c = sub3
            if 2*(a+c) == b:
                res+=1
        return res

--------------------------------------------------------------------------

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(2*(nums[i-1]+nums[i+1])==nums[i] for i in range(1, len(nums)-1))
        
