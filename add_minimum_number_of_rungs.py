'''
You are given a strictly increasing integer array rungs that represents the height of rungs on a ladder. You are currently on the floor at height 0, and you want to reach the last rung.

You are also given an integer dist. You can only climb to the next highest rung if the distance between where you are currently at (the floor or on a rung) and the next rung is at most dist. You are able to insert rungs at any positive integer height if a rung is not already there.

Return the minimum number of rungs that must be added to the ladder in order for you to climb to the last rung.
'''

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        return sum((a - b - 1) // dist for a, b in zip(rungs, [0] + rungs))
      
-----------------------------------------------------------------------------------

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        n = len(rungs)
        res = 0 
        for i in range(n-1):
            a, b = rungs[i], rungs[i+1]
            s = b - a
            if s > dist:
                res += (s-1)//dist
        if rungs[0] > dist:
            res += (rungs[0]-1)//dist
        return res
