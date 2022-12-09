'''
You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.
'''

class Solution:
    def minimumTimeRequired(self, jobs, k):
        if k == len(jobs):
            return max(jobs)
    
        self.min_val = float("inf")

        def backtrack(idx,ans):
            if idx == len(jobs):
                self.min_val = min(self.min_val,max(ans))
                return

            seen = set()

            for i in range(k):
                if ans[i] in seen: continue
                if ans[i] + jobs[idx] >= self.min_val: continue
                seen.add(ans[i])

                ans[i] += jobs[idx]
                backtrack(idx+1,ans)
                ans[i] -= jobs[idx]

        backtrack(0,[0]*k)

        return self.min_val
---------------------------------------------------------------------------------------------------------
class Solution:
    
    def dfs(self, pos: int, jobs: List[int], workers: List[int]) -> int:
        if pos >= len(jobs):
            return max(workers)
        
        mn = float("inf")
        # we keep track of visited here to skip workers
        # with the same current value of assigned work
		# this is an important step in pruning the number
		# of workers to explore
        visited = set()
        for widx in range(len(workers)):
            
            if workers[widx] in visited:
                continue
            visited.add(workers[widx])
            
            # try this worker
            workers[widx] += jobs[pos]
            
            if max(workers) < mn:
                # if it's better than our previous proceed
                res = self.dfs(pos+1, jobs, workers)
                mn = min(mn, res)
            
            # backtrack
            workers[widx] -= jobs[pos]
        
        return mn
        
    
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
	    # sorting the jobs means that highest value jobs are assigned first
		# and more computations can be skipped by pruning
        jobs.sort(reverse=True)
        return self.dfs(0, jobs, [0] * k)

        
        
