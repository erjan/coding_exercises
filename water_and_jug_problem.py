'''
You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
 
 '''

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return False if x + y < z else True if x + y == 0 else not z % math.gcd(x,y)
      
-----------------------------------------------------
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        total = jug1Capacity+jug2Capacity
        visit = set()
        visit.add(0)
        q = [0]
        while q:
            curr = q.pop(0)
            if curr == targetCapacity:
                return True
            for step in [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]:
                new = curr+step
                if new > 0 and new <= jug1Capacity+jug2Capacity and new not in visit:
                    visit.add(new)
                    q.append(new)
        return False
