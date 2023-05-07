'''
You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).

The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.

There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road can take you from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.

Return the minimum cost required to go from (startX, startY) to (targetX, targetY).
'''


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        filteredRoads = []
        for road in specialRoads:
            a, b, c, d, cost = road
            if cost < abs(a - c) + abs(b - d):
                filteredRoads.append([a, b, c, d, cost])
                
        dist = {(start[0], start[1]): 0}
        heap = [(0, start[0], start[1])]
        while heap:
            currdist, x, y = heapq.heappop(heap)
            for road in filteredRoads:
                a, b, c, d, cost = road
                if dist.get((c, d), float('inf')) > currdist + abs(x - a) + abs(y - b) + cost:
                    dist[(c, d)] = currdist + abs(x - a) + abs(y - b) + cost
                    heapq.heappush(heap, (dist[(c, d)], c, d))
        res = abs(target[0] - start[0]) + abs(target[1] - start[1])
        for road in filteredRoads:
            a, b, c, d, cost = road
            res = min(res, dist.get((c, d), float('inf')) + abs(target[0] - c) + abs(target[1] - d))
        return res
