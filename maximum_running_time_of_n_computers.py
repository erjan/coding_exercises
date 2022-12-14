'''
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.

 
 '''

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, h = min(batteries), sum(batteries)
        
        batteries.sort()
        cands = batteries[-n:]
        rest = sum(batteries[:-n])
        
        def bs(t):
            tmp = rest
            for x in cands:
			    # all rest batteries on computer can run more than t time
                if x >= t: return True
				# need t - x batteries to fill
                tmp -= t - x
				if tmp < 0: return False
            return True
            
        
        while l < h:
            mid = l + (h - l + 1) // 2
            if bs(mid):
                l = mid
            else:
                h = mid  - 1
        
        return l
      
---------------------------------------------------------------------------------------------
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        refills = batteries[n:]
        s = sum(refills)
        res = 0
        for i in range(n-1, 0, -1):
            cur = batteries[i]
            prev = batteries[i-1]
            if prev == cur:
                continue
            smaller_batteries = n-i
            need_for_refill = smaller_batteries * (prev-cur)
            if need_for_refill <= s:
                s -= need_for_refill
            else:
                return cur + s // smaller_batteries
            
        return batteries[0] + s // n
