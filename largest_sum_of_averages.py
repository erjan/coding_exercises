'''
You are given an integer array nums and an integer k. You can partition the array into at most k non-empty adjacent subarrays. The score of a partition is the sum of the averages of each subarray.

Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

Return the maximum score you can achieve of all the possible partitions. Answers within 10-6 of the actual answer will be accepted.
'''

def largestSumOfAverages(self, nums: List[int], k: int) -> float:
	n = len(nums)
	pre = [0]
	for i in nums:
		pre.append(pre[-1] + i)
	def solve(i, k):
		if(k == 1): return sum(nums[i:])/(n-i)

		if(n-i < k): return -1

		if((i, k) in d): return d[(i, k)]

		temp = 0
		for j in range(i+1, n):
			temp = max(temp, solve(j, k-1)+(pre[j]-pre[i])/(j-i))
		d[(i, k)] = temp
		return temp
	d = dict()            
	return solve(0, k)

--------------------------------------------------------------------------------------------------------------------------
The idea of this question is very straightforward.
There are 2 things to consider: state and option.

State is the variable, what might change in the question, in this case, the length of the array & the number of partition
Option is what we can decide. In this case, we can decide whether cut the array or not at a certain position, and we want to optimize the option, aka we need to find the best result from cut or not cut.
DP array is defined as follow:
dp[i][j] states what is the maximal result given that the first i+1 character in the array and j cuts.

Here is the process:
Base case: when i = 0, j =0, means given the first char, maximum of 0 cut is allowed, dp[i][j] = A[0], piece of cake.
Base nonpermissible case: when i = 0, j = n , n in [1,2,3...], means given the first char, maximum of n cut is allowed, dp[i][j] = 0
State Transition: for any dp[i][j] that are not classified as base cases, we want to find the maximum partition, which is the maximum of dp[k][j-1]+avg(A[k+1:i+1])) such that k in the range of 0 to i-1. (Intuitively, we don't care what the partition from 0 to k is, we leave that as to our subproblems)

Here is the code written in Python:

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        def avg(array):
            return sum(array) / len(array)
        dp = [[0 for _ in range(K)] for _ in range(len(A))]
        dp[0][0] = A[0]
        for i in range(len(A)):
            for j in range(K):
 #               if i == 0 and j != 0:
 #                  continue
                if j == 0:
                    dp[i][j] = avg(A[:i+1])
                else:
                    for k in range(i):
                        dp[i][j] = max(dp[i][j],dp[k][j-1]+avg(A[k+1:i+1]))
        return dp[len(A)-1][K-1]
        
----------------------------------------------------------------------------------------------------------
def dp(A, K):
	dp = [[0] * len(A) for _ in range(K)]
	for j in range(len(A)):
		dp[0][j] = mean(A[:j + 1])
	for k in range(1, K):
		for j in range(k, len(A)):
			for i in range(j):
				dp[k][j] = max(dp[k][j], dp[k - 1][i] + mean(A[i + 1:j + 1]))
	return dp[-1][-1]
return dp(A, K)
