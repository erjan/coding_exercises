'''
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.
'''

class Solution:
  def minSubarray(self, nums: List[int], p: int) -> int:
      dp = defaultdict(int)
      dp[0] = -1
      target = sum(nums) % p
      curSum = 0
      result = len(nums)

      if sum(nums) % p == 0: return 0

      for i in range(len(nums)):
          curSum += nums[i]

          curMod = curSum % p

          temp = (curSum - target) % p

          if temp in dp:
              if i - dp[temp] < result:
                  result = i - dp[temp]

          dp[curMod] = i

      return result if result < len(nums) else -1
    
-------------------------------------------------------------------------------------------
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums) 
        remainder = total % p
        if not remainder:
            return 0
        ans = float('inf') 
        presum = [0]
        remainders = {0: -1}
        for i, n in enumerate(nums):
            presum.append(presum[-1] + n)
            r = ((cr := presum[-1] % p) - remainder) % p
            if r in remainders:
                ans = min(ans, i - remainders[r])
            remainders[cr] = i
        return ans if ans < len(nums) else -1
