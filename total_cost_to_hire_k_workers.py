'''
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.
'''

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        cand_heap = [] # Heap of candidates; hp elem (cost, inx)
        
        # remaining elems bounds
        left_bound, right_bound = candidates, n-candidates-1
        
        # add left candidates
        for i in range(candidates):
            heapq.heappush(cand_heap, (costs[i], i))
        
        # add right candidates, (exclude already taken from left)
        for i in reversed(range(n-candidates, n)):
            if i < left_bound:
                break
            heapq.heappush(cand_heap, (costs[i], i))
        
        total_cost = 0
        for _ in range(k):
            cost, inx = heapq.heappop(cand_heap)
            total_cost += cost
            if left_bound <= right_bound: # if there are remaining elements
                if inx < left_bound: # if cur elem was from left, replenish from left
                    heapq.heappush(cand_heap, (costs[left_bound], left_bound))
                    left_bound += 1
                elif inx > right_bound: # if cur elem was from right, replenish from right
                    heapq.heappush(cand_heap, (costs[right_bound], right_bound))
                    right_bound -= 1
        return total_cost 
