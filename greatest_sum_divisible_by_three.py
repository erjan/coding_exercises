'''
Given an integer array nums, return the maximum
possible sum of elements of the array such that it is divisible by three.
'''


class Solution:
	def maxSumDivThree(self, nums: List[int]) -> int:
		dp = [0]*3

		for num in nums:
			newdp = dp.copy()
			for i in range(3):
				newdp[(num+dp[i])%3] = max(newdp[(num+dp[i])%3], num+dp[i])
			dp = newdp
		return dp[0]
	
------------------------------------------------------------------	
class Solution:
    def maxSumDivThree(self, N: List[int]) -> int:
        A, B, S = heapq.nsmallest(2,[n for n in N if n % 3 == 1]), heapq.nsmallest(2,[n for n in N if n % 3 == 2]), sum(N)
        if S % 3 == 0: return S
        if S % 3 == 1: return S - min(A[0], sum(B) if len(B) > 1 else math.inf)
        if S % 3 == 2: return S - min(B[0], sum(A) if len(A) > 1 else math.inf)
        
-------------------------------------------------------------

class Solution:
	def maxSumDivThree(self, nums: List[int]) -> int:
		dp = [[0 for i in range(len(nums)+1)] for j in range(3)]

		for i in range(1,len(nums)+1):
			for j in range(3):
				dp[j][i] = max(dp[j][i-1], dp[j][i])
				curSum = nums[i-1] + dp[j][i-1]
				idx = curSum % 3
				dp[idx][i] = max(dp[idx][i-1], curSum, dp[idx][i])

		return dp[0][-1]
  
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [0, 0, 0]
        
        for n in nums:
            tmp_dp = dp[:]
            for i in range(len(dp)):
                c_sum = tmp_dp[i] + n
                dp[c_sum % 3] = max(dp[c_sum % 3], c_sum)


        return dp[0]
