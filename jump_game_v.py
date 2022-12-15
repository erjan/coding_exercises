'''
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and  0 < x <= d.
i - x where: i - x >= 0 and  0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.
'''


class Solution:
	def maxJumps(self, arr: List[int], d: int) -> int:

		dp = defaultdict(int)
		def dfs(i):
			if i in dp: return dp[i]
			m_path = 0
			for j in range(i+1,i+d+1):
				if j>=len(arr) or arr[j]>=arr[i]: break
				m_path = max(m_path,dfs(j))

			for j in range(i-1,i-d-1,-1):
				if j<0 or arr[j]>=arr[i]: break
				m_path = max(m_path,dfs(j))
			dp[i] = m_path+1
			return m_path+1

		res = 0
		for i in range(len(arr)):
			res = max(res,dfs(i))
		return res
  
  
