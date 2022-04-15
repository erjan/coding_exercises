'''
On a campus represented as a 2D grid, there are n workers and m bikes, with n <= m. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.



At first I implemented the solution with backtracking, but with this approach you need to generate all possible assignments which has factorial complexity. I was passing over the bikes that were not assigned yet (left_bikes) and the current worker I was assigning a bike to, and effectively in this situation we have repeated calls:

I assign the first bike to the first worker, and then I assign the second bike to the second worker, my current worker will be 3 and my left bikes will be all but first and second. On a different branch I assign the first bike to the second worker, and then the second bike to the first worker, and I have the same as before, current worker 3 and left bikes all but first and second.

The thing is, I cannot memoize with this approach, because the assignments are different, so I cannot use the information from the past branch to get the distance on this different branch, then I will get time limit.

Clearly, the way to go is dynamic programming, if I build a bottom up solution then I can use the information from the past seen calls into my current assignment:

left_bikes is an array the size of bikes, which has a 0 if bike[i] has been assigned or not. You can generate a new array on every call or pass it by reference and update it in a backatracking fashion, which I did to save space.
cur_worker is the index of the current worker I need to assign a bike to
In order to memoize, left_bikes need to be transformed into a tuple, since lists are not hashable.


'''

class Solution(object):

    def assignBikes(self, workers, bikes):
	
        def _assign(left_bikes, cur_worker):
            info = (cur_worker, tuple(left_bikes)) # unique identifier of the call parameters 
            if info in self.seen: # if I have computed the min distance for this paramenters before
                return self.seen[info]
            if cur_worker == len(workers): # if I already assigned all workers
                return 0
            temp = float('inf') # start calculating the minimum from this assignment onwards
            for j in range(len(left_bikes)): 
                if left_bikes[j] == 0: # assign all left bikes to the current worker
                    left_bikes[j] = 1
                    wx, wy = workers[cur_worker]
                    bx, by = bikes[j]
                    temp = min(temp, abs(wx - bx) + abs(wy - by) + _assign(left_bikes, cur_worker + 1)) # update my minimum considering the minimum between what I had and the distance of this assignment + the minimum distance for the future assignments 
                    left_bikes[j] = 0 # unassign bike (instead of creating new left_bike array for every call)
            self.seen[info] = temp # memoize
            return temp 
			
        self.seen = dict() # initialize my memoization structure
        return _assign([0 for _ in range(len(bikes))], 0) # start with all bikes unassigned and with worker 0
      
-------------------------------------------------------------------------
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dist(w, b):
            xw, yw = workers[w]
            xb, yb = bikes[b]
            return abs(xw - xb) + abs(yw - yb)
        @lru_cache(None)
        def dfs(used_bikes, wi):
            if wi == len(workers):
                return 0
            ans = float('inf')
            for bi in range(len(bikes)):
                if used_bikes & (bitmask := 1 << bi) == 0:
                    ans = min(ans, dist(wi, bi) + dfs(used_bikes | bitmask, wi+1))
            return ans         
        return dfs(0, 0) 
      
      ------------------------------------------------------------------------------
      
class Solution(object):
    def assignBikes(self, workers, bikes):

        cache = dict()

        def manh_dist(w, b):
            return abs(w[0] - b[0]) + abs(w[1] - b[1])

        def helper(curr_bikes, w_idx):
            hash = (
                w_idx,
                curr_bikes,
            )

            seen = cache.get(hash, False)
            if seen:
                return seen

            if w_idx == len(workers):
                return 0
            res = float("inf")

            for b_idx in range(len(bikes)):
                if (curr_bikes >> b_idx) & 1:

                    curr_bikes ^= 1 << b_idx  # flip bit

                    mhd = manh_dist(workers[w_idx], bikes[b_idx])
                    res = min(
                        res,
                        mhd + helper(curr_bikes, w_idx + 1),
                    )

                    curr_bikes ^= 1 << b_idx # flip bit back

            cache[hash] = res
            return res

        bits = 0
        for _ in range(len(bikes)):
            bits = (bits << 1) + 1   # 1 = bike available

        return helper(bits, 0)
      
------------------------------------------------------------------
from functools import lru_cache
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        # precompute distances
        dists = [[] for _ in range(len(workers))]
        for i,worker in enumerate(workers):
            for j,bike in enumerate(bikes):
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                dists[i].append(dist)                  
                        
        
        @lru_cache(None)
        def rec(i, visited):
            if i == len(workers):
                return 0
            
            sum_ = float('inf')
            for bike in range(len(bikes)):                               
                if not (visited & (1 << bike)):
                    visited |= (1 << bike)
                    dist = dists[i][bike] 
                    sum_ = min(sum_ , dist + rec(i+1, visited))
                    visited &= ~(1 << bike)
            return sum_
        
        visited = 0        
        
        return rec(0,visited)
