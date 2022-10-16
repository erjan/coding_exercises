'''
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
'''

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
    
        @cache
        # dp(i, k): min difficulty when you start working on i-th job at day `k`
        def dp(i, k):
            # reach the last day
            # we put all the remaining jobs on this day
            # so we return the one with max difficulty
            if k == d: return max(jobDifficulty[i:])
            # init min difficulty with inf 
            res = float('inf')
            # cur is the max difficulty we've seen so far on day `k`
            # init current max with 0
            cur = 0
            # for jobDifficulty like 6 5 4 3 2 1, 
            # we can have following ways to distribute them into two days
            # 6 | 5 4 3 2 1
            # 6 5 | 4 3 2 1 
            # 6 5 4 | 3 2 1
            # 6 5 4 3 | 2 1
            # 6 5 4 3 2 | 1
            # notice that each day we must have at least one task
            # given the starting index `i`, 
            # we can only at most choose the jobs till the position `n - d + k - 1`
            for j in range(i, n - d + k):
                cur = max(cur, jobDifficulty[j])
                # if j-th job is the last job on day `k`, 
                # the max difficulty for day `k` is `cur`
                # and we need to start (j + 1)-th job on the next day
                # the result would be `cur + dp(j + 1, k + 1)`
                # then we take the min
                res = min(res, cur + dp(j + 1, k + 1))
            return res
        # n < d : you will have free days. hence you cannot find a schedule for the given jobs
        # e.g. Example 2
        # otherwise, we start working on 0-th job at day 1
        return -1 if n < d else dp(0, 1)
      
--------------------------------------------------------------------------------------------------------------
Recursion with Memoization, Top-down

Starting from the last day, we simply try out all the possible schdules for each day.
We track the intended finished day (intended) and the first i-th jobs (end).

from functools import lru_cache
class Solution:
    def minDifficulty(self, J, d):
        @lru_cache(maxsize=None) # memoization
        def helper(intended, end):
		    # the base case, if we only have 1 day left, we need to handle all the tasks on that day
            if intended == 1: return max(J[:end])
			
            res, mx = math.inf, 0
            for done in range(1,end-intended+2):
                mx = max(mx, J[end-done])
                res = min(helper(intended-1, end-done) + mx, res)
            return res                
        
        return helper(d, len(J)) if len(J) >= d else -1
DP, Bottom-up

class Solution:
    def minDifficulty(self, J, d):
        if len(J) < d: return -1
        
        dp = {} # (index of day, index of the last finished job)
        for i,job in enumerate(J):
            # the base case, all jobs need to be finish in one day
            dp[0, i] = max(dp.get((0, i-1), 0), job)
            
        for i in range(1, d):
            for j in range(i, len(J)):
                mx = J[j]
                for k in range(j, i-1, -1):
                    mx = max(mx, J[k])
                    dp[i, j] = min(dp.get((i, j), math.inf), mx + dp[i-1, k-1])
                
        return dp[d-1, len(J)-1]
--------------------------------------------------------------------------------------------------------
def dp(jobs, d):
	A = [[float("inf")] * d for i in range(len(jobs))]
	A[0][0] = jobs[0]
	for i in range(1, len(jobs)):
		A[i][0] = max(A[i - 1][0], jobs[i])

	for i in range(1, len(jobs)):
		for j in range(1, min(i + 1, d)):
			for k in range(i):
				A[i][j] = min(A[i][j], A[k][j - 1] + max(jobs[k + 1:i + 1]))

	return A[-1][-1]
return dp(jobDifficulty, d)
