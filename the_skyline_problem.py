'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.
'''

from heapq import *

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # `position` stores all coordinates where the largest height may change
        # `alive` stores all buildings whose ranges cover the current coordinate
        position = sorted(set([building[0] for building in buildings] + [building[1] for building in buildings]))
        ptr, prevH = 0, 0
        alive, ret = [], []
        
        for curPos in position:
            # pop buildings that end at or before `curPos` out of the priority queue
            # they are no longer "alive"
            while alive and alive[0][1] <= curPos:
                heappop(alive)
            
            # push [negative_height, end_point] of all buildings that start before `curPos` onto the priority queue
            # they are candidates for the current highest building
            while ptr < len(buildings) and buildings[ptr][0] <= curPos:
                heappush(alive, [-buildings[ptr][2], buildings[ptr][1]])
                ptr += 1
            
            # now alive[0] must be the largest height at the current position
            if alive:
                curH = -alive[0][0]
                if curH != prevH:
                    ret.append([curPos, curH])
                    prevH = curH
            else:  # no building -> horizon
                ret.append([curPos, 0])
                
        return ret
