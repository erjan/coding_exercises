'''
You are given two 0-indexed integer arrays jobs and workers of equal length, where jobs[i] is the amount of time needed to complete the ith job, and workers[j] is the amount of time the jth worker can work each day.

Each job should be assigned to exactly one worker, such that each worker completes exactly one job.

Return the minimum number of days needed to complete all the jobs after assignment.
'''


class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()

        ans = 0

        for i in range(len(jobs)):
            result = 0

            if jobs[i] > workers[i]:
                result += jobs[i]//workers[i]

                if jobs[i]%workers[i]:
                    result += 1
            else:
                result += 1

            ans = max(ans, result)

        return ans

        
