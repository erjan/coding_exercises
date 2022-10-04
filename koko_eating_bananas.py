'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = ceil(sum(piles) / h) # lower bound of Binary Search 
        right = max(piles) # upper bound of Binary Search 
        while left < right:
            mid = (left + right) // 2 # we check for k=mid
            total_time = 0
            for i in piles:
                total_time += ceil(i / mid)
                if total_time > h:
                    break
            if total_time <= h:
                right = mid # answer must lie to the left half (inclusive of current value ie mid)
            else:
                left = mid + 1 # answer must lie to the right half (exclusive of current value ie mid)
        return right
      
----------------------------------------------------------------------------------------------------------------
If the length of the piles is equal to the H, each time koko need to finish a pile in order to eat all of them within the limited time. So k=max(piles)

If the length of the piles is bigger than the H, koko can not finish eat all of them.

If the length of the piles is smaller than the H, we could find a k smaller than the max(piles)

Class Solution:

	def minEatingSpeed(self, piles: List[int], H: int) -> int:
	#If the length of the piles is equal to the H, return max(piles)
		if H == len(piles):
			return max(piles)
	
	#Binary search
	#Koko could each at least 1 banana and at most max(piles) bananas each time
		lo, hi = 1, max(piles)

		while lo < hi:
	#Get the mid number of bananas to eat
			mid = (lo+hi) // 2
	
	#Calculate how many hours that koko need to finish eating all of the piles given the eating speed mid 
			h = 0
			for p in piles:
				if p < mid:
					h += 1
				else:
					h += math.ceil(p/mid)
	#If the time that koko need is less than or equal to H, we need to search for the left part
			if h <= H:
				hi = mid
	#If the time that koko need is bigger than H, we need to search for the right part
			else:
				lo = mid + 1
		return lo
