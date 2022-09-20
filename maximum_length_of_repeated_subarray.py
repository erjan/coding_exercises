class Solution:
  def findLength(self, nums1: List[int], nums2: List[int]) -> int:

      m=len(nums1)
      n=len(nums2)
      dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
      res=0
      for i in range(m):
          for j in range(n):
              if nums1[i]==nums2[j]:
                  dp[i+1][j+1]=dp[i][j]+1
              else:
                  dp[i+1][j+1]=0
              res=max(res,dp[i+1][j+1])

      return res
    
-------------------------------------
def dp(A, B):
	longest = 0
	DP = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

	for i in range(1, len(A) + 1):
		for j in range(1, len(B) + 1):
			if A[i - 1] == B[j - 1]:
				DP[i][j] = 1 + DP[i - 1][j - 1]
				longest = max(longest, DP[i][j])
	return longest
return dp(A, B)

--------------------------------------------------------
#difflib

from difflib import SequenceMatcher

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if set(A).isdisjoint(B): return 0
        a, b, size = SequenceMatcher(None, A, B, autojunk=False).find_longest_match(0, len(A), 0, len(B))
        return size
      
-------------------------------------------------------------------
class Solution:
	"""
	Time:   O(n*m)
	Memory: O(n*m)
	"""

	def findLength(self, a: List[int], b: List[int]) -> int:
		n, m = len(a), len(b)
		dp = [[0] * (m + 1) for _ in range(n + 1)]

		for i in range(n):
			for j in range(m):
				if a[i] == b[j]:
					dp[i + 1][j + 1] = dp[i][j] + 1

		return max(map(max, dp))
