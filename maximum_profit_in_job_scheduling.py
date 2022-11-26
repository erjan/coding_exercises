'''
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.
'''



#heap
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))], key=lambda x: x[0])
        heap = []
        currentProfit = 0
        maxProfit = 0
        for start, end, profit in jobs:
            # Calculate the total profit of all the jobs that would have end by this time(start: startTime of current job) 
            while heap and heap[0][0] <= start:
                _, tempProfit = heapq.heappop(heap)
                currentProfit = max(currentProfit, tempProfit)
            
            # Push the job into heap to use it further. It's profit would be definitely currentProfit + profit(of current job)
            heapq.heappush(heap, (end, currentProfit + profit))
            maxProfit = max(maxProfit, currentProfit + profit)

        return maxProfit
      
---------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def getNextEligibleJob(self, jobs, index):
        left = index+1
        right = len(jobs)
        eligibleJobIndex = None
        while left < right:
            mid = left + ((right-left)//2)
            if jobs[mid][0] >= jobs[index][1]:
                eligibleJobIndex = mid
                right = mid
            else:
                left = mid + 1
        return eligibleJobIndex

    def recur(self, jobs, currentJobIndex, lookup):
        if currentJobIndex == len(jobs):
            return 0
        if lookup[currentJobIndex] == -1:
            maxProfit = jobs[currentJobIndex][2]
            nextValidJobIndex = self.getNextEligibleJob(jobs, currentJobIndex)
            if nextValidJobIndex:
                maxProfit += self.recur(jobs, nextValidJobIndex, lookup)
            lookup[currentJobIndex] = max(maxProfit, self.recur(jobs, currentJobIndex+1, lookup))
        return lookup[currentJobIndex]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))], key=lambda x: x[0])
        return self.recur(jobs, 0, [-1 for _ in range(len(jobs))])
      
----------------------------------------------------------------------------------------------------------------------------
#dp another one

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n = len(startTime)
        # sort each list according to the start time
        s = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])
        startTime = [x[0] for x in s]
        endTime   = [x[1] for x in s]
        profit    = [x[2] for x in s]

        # Bottom up dynammic programming 
        # Knapsack problem
        dp = [0] * n
        dp[-1] = profit[-1]
        for i in range(n-2, -1, -1):
            # If we include the current job
            # Add the current job to the maximum profit of the jobs that start when this job ends (if exists)
            j = bisect.bisect_left(startTime, endTime[i])
            # Decision to include job
            dp[i] = max(profit[i] + dp[j] if j < n else profit[i], dp[i+1])

        return dp[0]
