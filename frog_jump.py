'''
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
'''

class Solution(object):
    def canCross(self, stones):
        n = len(stones)
        stoneSet = set(stones)
        visited = set()
        def goFurther(value,units):
            if (value+units not in stoneSet) or ((value,units) in visited):
                return False
            if value+units == stones[n-1]:
                return True
            visited.add((value,units))
            return goFurther(value+units,units) or goFurther(value+units,units-1) or goFurther(value+units,units+1)
        return goFurther(stones[0],1)
