'''
You are given an integer array stations that represents the positions of the gas stations on the x-axis. You are also given an integer k.

You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

Return the smallest possible value of penalty(). Answers within 10-6 of the actual answer will be accepted.
'''

Bottom Line: When you are facing an optimization problem, take a second to think about the range of possble answers to the problem first. Getting some first ideas about this before approaching the problem may save you a lot of efforts.

My first reaction to this problem is to maintain a priority queue (max heap) to keep the segment that currently has the longest distance between adjacent stations on top. At each iteration, build another station into this top segment and push it back into the max heap, until you have exhausted all K new stations. The result to be returned is the distance between adjacent stations in the top segment.

I implemented this, and it throws TLE onto my face.

import heapq

class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        # maintain a max heap and alway cut the maximum length segment
        max_heap = []
        for i in range(1, len(stations)):
            # ((negative) max distance inside the segment, index of the end station, number of cuts so far)
            heapq.heappush(max_heap, (-float(stations[i] - stations[i-1]), i, 1))
        
        added = 0  # keeps track of the number of new stations built
        while added < K:
            cur_dist, i, cur_added = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-float(stations[i] - stations[i-1])/(cur_added+1), i, cur_added+1))
            added += 1
        
        return -max_heap[0][0]
The reason for TLE is due to cases where we have very large number of K. The above solution is O(KlgN), and in some test cases, notably the one that it failed, has very large K. The remedy, however, is to 

realize that we don't have to consider adding new stations from 1 to K. There is a lower bound of the answer to this problem, that is the distance between two adjacent stations when we evenly place K new stations between the orignal first and last stations, ignoring all other original stations in the middle. The result of that scheme is lower_bound = (stations[-1] - stations[0]) / (K+1). Therefore, instead of initializing the max heap by pushing the original segments with 0 new stations into it, we initialize by installing needed number of new stations in each segment such that the distance between two adjacent stations within that segment is no larger than lower_bound. Take a minute to think about it and you should be able to convince yourself that now we only have approximately N new stations left to place, which brings down the time complexity to O(NlgN).

import heapq
import math

class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        # priority queue
        # the lower bound of the solution is the entire length divided by (K+1)
        bound = (stations[-1] - stations[0]) / (K + 1)
        added = 0  # keeps track of the stations already built
        max_heap = []
        for i in range(1, len(stations)):
            needed = math.ceil((stations[i] - stations[i-1]) / bound) - 1
            heapq.heappush(max_heap, (-(stations[i] - stations[i-1])/(needed+1), i, needed))
            added += needed
        
        while added < K:
            cur, i, needed = heapq.heappop(max_heap)
            needed += 1
            heapq.heappush(max_heap, (-(stations[i] - stations[i-1])/(needed+1), i, needed))
            added += 1
        
        return -max_heap[0][0]
And now things work out nicely. The key is really to realize that there is a natural lower bound for the answer to this problem. And we probably should all think a little bit about what values the answer could possbly take before we even determine what approach to take to solve the problem algorithmically.


-----------------------------------------------------------------------------------
Classic binary search solution similar to the problems
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
https://leetcode.com/problems/split-array-largest-sum/submissions/
https://leetcode.com/problems/koko-eating-bananas/

Basically the idea is we are searching for the optimal K* in the interval [0, S] that answers the problem statement. We know the upper bound S, because the existing stations already tells us what's the maximum distance we get even without putting new stations.

 min_distance = 0
        for i, station in enumerate(stations):
            if i==len(stations)-1:
                pass
            else:
                min_distance = max(min_distance, abs(stations[i] - stations[i+1]))
However what we can see is that it is possible to verify in O(n) for a given K whether or not it's a feasible solution (not the best, a feasible one) to the problem statement.
Then we can simply search for smallest K that is still feasible ...
Hardest thing was to make sure that the possible() function, that checks whether or not K is feasible, is done in O(n) and not O(k). So implementing it correctly by putting several stations at the same time (instead of one station by one) is important !

count += int((next_station - current_station)/max_distance)
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        min_distance = 0
        for i, station in enumerate(stations):
            if i==len(stations)-1:
                pass
            else:
                min_distance = max(min_distance, abs(stations[i] - stations[i+1]))
        
        S = min_distance
        i = 0
        j = S
        iteration = 40
        while iteration!=0:
            middle = (i+j)/2
            max_distance = middle
            if self.possible(max_distance, stations, k):
                j = middle -0.00000001
            else:
                i = middle  + 0.00000001
            iteration -= 1
        return i
    
    
    def possible(self, max_distance, stations, k):
        count = 0
        current_station = stations[0]
        for i, next_station in enumerate(stations):
            if i==0:
                continue
            count += int((next_station - current_station)/max_distance)
            current_station = next_station
            if count > k:
                return False
        return count <= k
      
---------------------------------------------------------
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
	
		# as we are looking for the intervals between different stations, the very first ituition 
		# is we convert the given array into an array of station disances, and then, this problem 
		# becomes almost exactly same as problem  # 1760 (Minimum Limit of Balls in a Bag). 
		# We need to separate the distances (balls in the bag) within k times and try to find the 
		# min of the max distance (panalty). The only difference is that we need to deal with float numbers

		# convert the array into distance array
        for i in range(1, len(stations)):
            stations[i-1] = stations[i] - stations[i-1]
        stations.pop()
        
		# do the binary search
        left = 0
        right = max(stations)
        
        while left <= right:
            mid = (left + right) / 2
            nums = 0
            for i in stations:
                if i > mid:
                    nums += int(i / mid)
            if nums <= k:
                right = mid - 0.000001
            else:
                left = mid + 0.000001
        
        return left
------------------------------------------------------------------------------
Here I post the top-down DP similar to Editorial approach 1's bottom-up DP, just for completeness cuz I didn't find this impl in discuss.
And the time complexity is easier to analyze compare w/ backtracking DFS due to overlapping subproblems. Using the formula stated in post: https://medium.com/@timpark0807/dp-is-easy-part-2-74422931dd98, DP Time Complexity = Number of Function Calls * Work Done per Function Call: O(NK^2)
* #states: O(NK)
* Work done per func call: O(K) to find minmax

def minmaxGasDist():
    deltas = []
    for l, r in zip(stations, stations[1:]):
        deltas.append(r - l)
    D = len(deltas)
    # print(deltas, D)

    @cache
    def dp(n, g):
        """
        TLE: 31 / 61 test cases passed.

        opt solution for adding g more stations in first n intervals.
        T: O(NK^2)
        """
        if n == 1:
            return deltas[0] / (g + 1)
        if g == 0:
            return max(deltas[:n])
        res = min(max(deltas[n - 1] / (x + 1), dp(n - 1, g - x)) for x in range(g + 1))
        return res

    return dp(D, k)
      
      
