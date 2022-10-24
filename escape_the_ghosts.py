'''
You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point [0, 0], and you are given a destination point target = [xtarget, ytarget] that you are trying to get to. There are several ghosts on the map with their starting positions given as a 2D array ghosts, where ghosts[i] = [xi, yi] represents the starting position of the ith ghost. All inputs are integral coordinates.

Each turn, you and all the ghosts may independently choose to either move 1 unit in any of the four cardinal directions: north, east, south, or west, or stay still. All actions happen simultaneously.

You escape if and only if you can reach the target before any ghost reaches you. If you reach any square (including the target) at the same time as a ghost, it does not count as an escape.

Return true if it is possible to escape regardless of how the ghosts move, otherwise return false.
'''


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_distance = abs (target[0]) + abs (target[1])
        for ghost in ghosts:
            ghost_distance = abs (target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if my_distance >= ghost_distance:
                return False
        return True
      
------------------------------------------
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = sum(map(abs, target))
        x, y = target
        for gx, gy in ghosts:
            if abs(x-gx) + abs(y-gy) <= dist:
                return False
        return True
