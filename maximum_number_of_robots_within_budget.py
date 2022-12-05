'''
You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given an integer budget.

The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), where max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running costs among the k robots.

Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.
'''

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        def fn(k): 
            """Return min cost of running k consecutive robots."""
            if k == 0: return 0
            ans = inf 
            sm = 0 
            pq = []
            for i, (ct, rc) in enumerate(zip(chargeTimes, runningCosts)): 
                sm += rc
                heappush(pq, (-ct, i))
                if i >= k: 
                    sm -= runningCosts[i-k]
                    while pq[0][1] <= i-k: heappop(pq)
                if i >= k-1: ans = min(ans, -pq[0][0] + k*sm)
            return ans 
        
        lo, hi = 0, len(chargeTimes)
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if fn(mid) <= budget: lo = mid 
            else: hi = mid - 1
        return lo 
      
-----------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n, max_robots = len(chargeTimes), 0
        max_charge = [] # max heap with tuples: (charge, index)
        running = runsum = 0
        p1 = p2 = cost = 0
        
        while p2 <= n:
            k = p2 - p1
            if cost <= budget:
                max_robots = max(max_robots, k)
            if p2 == n:
                break
                
			# pop any charge times that are not in the current window
            while max_charge and max_charge[0][1] < p1:
                heapq.heappop(max_charge)
                
            if cost <= budget: # add the next robot if we are within budget
                heapq.heappush(max_charge, (-chargeTimes[p2], p2))
                running += runsum + (k + 1) * runningCosts[p2]
                runsum += runningCosts[p2]
                cost = running - max_charge[0][0] # max heap stores negs
                p2 += 1
            
            elif k == 1:
                p1 = p2
                cost = running = runsum = 0
            
            else: # shrink window if budget is exceeded
                while max_charge and max_charge[0][1] <= p1:
                    heapq.heappop(max_charge)
                running -= runsum + (k - 1) * runningCosts[p1]
                runsum -= runningCosts[p1]
                cost = running - max_charge[0][0]
                p1 += 1
                
        return max_robots
      
--------------------------------------------------------------------------------------------------------------------------------------------      


class Solution:
    def maximumRobots(self, time: List[int], cost: List[int], budget: int) -> int:
        prefix_sum = [0]
        S = 0 
        for v in cost:
            S += v
            prefix_sum.append(S)
        
        # print(prefix_sum)
        maxQ = deque()
        
        # slide window
        n = len(time)
        l = 0
        ret = 0
        # the window considered here is [l,r], boundary included
        for r in range(n):
            while len(maxQ) and time[r] > maxQ[-1]:
                maxQ.pop()
            maxQ.append(time[r])
            
            k = r-l+1
            tc = prefix_sum[r+1] - prefix_sum[l] # total cost
            mt = maxQ[0] # max time
            
            while l<=r and (mt + k*tc) > budget:
                if time[l] == maxQ[0]:
                    maxQ.popleft()
                l += 1
                
                if l > r:
                    break
        
                k = r-l+1
                tc = prefix_sum[r+1] - prefix_sum[l]
                mt = maxQ[0]
            
            ret = max(ret, r-l+1)
        return ret
