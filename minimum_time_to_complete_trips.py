'''
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.
'''

#heap solution

import heapq

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # Return the smallest multiple of b strictly greater than a.
        def ceiling(a, b):
            return a // b * b + b
        
		# Step 1: Find est, an initial lower bound
        speed = sum(1/t for t in time)
        est = int(totalTrips/speed)
        
		# Step 2: Construct the heap
        trips = 0
        hp = []
        for t in time:
		    # ceiling(est, t) is the next returning time for the truck t
            heappush(hp, (ceiling(est, t), t))
			# Compute trips, the number of trips actually finished at time est
            trips += est // t
            
	    # Step 3: Heap update
        answer = est
        while trips < totalTrips:
		    # Update the returning time as answer for every incoming trip
            answer, t = heappop(hp)
			# Push back the next returning time for the same truck which just returned.
            heappush(hp, (ceiling(answer, t), t))
            trips += 1
            
        return answer
      
---------------------------------------------------------------------------------
def minimumTime(self, time: List[int], totalTrips: int) -> int:
	if len(time) == 1:
		return totalTrips * time[0]

	l, r = 0, 10**15
	while l < r:
		mid = (l + r) // 2

		res = 0
		for t in time:
			res += mid // t

		if res >= totalTrips:
			r = mid
		else:

			l = mid + 1

	return l

-----------------------------------------------------------------------------------------------------
class Solution(object):
    def minimumTime(self, time, totalTrips):
        anstillnow=-1;
        left=1;
        right= 100000000000001;
        
        while(left<=right):
            mid= left+ (right-left)/2      #find mid point like this to avoid overflow
            
            curr_trips=0;
            
            for t in time:
                curr_trips+= mid/t
            
            if(curr_trips>=totalTrips):
                anstillnow=mid
                right=mid-1
            
            else:
                left=mid+1

        return anstillnow
-------------------------------------------------------------------------------
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low=0
        high=max(time)*totalTrips
        
        ans=0
        while low<=high:
            mid=(low+high)//2
            count=0
            for t in time:
                count=count+(mid//t)
            if count>=totalTrips:
                ans=mid
                high=mid-1
            else:
                low=mid+1
            
        return ans
