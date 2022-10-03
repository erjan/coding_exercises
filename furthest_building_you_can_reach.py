'''
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
'''

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # prepare: use a min heap to store each difference(climb) between two contiguous buildings
        # strategy: use the ladders for the longest climbs and the bricks for the shortest climbs
        
        min_heap = []
        n = len(heights)
        
        for i in range(n-1):
            climb = heights[i+1] - heights[i]
            
            if climb <= 0:
                continue
            
            # we need to use a ladder or some bricks, always take the ladder at first
            if climb > 0:
                heapq.heappush(min_heap, climb)
            
            # ladders are all in used, find the current shortest climb to use bricks instead!
            if len(min_heap) > ladders:
                # find the current shortest climb to use bricks
                brick_need = heapq.heappop(min_heap)
                bricks -= brick_need
            
            if bricks < 0:
                return i
        
        return n-1
      
------------------------------------------------------------------------------------------------------
class Solution:
    def furthestBuilding(self, H: List[int], B: int, L: int) -> int:
        heap = []
        for i in range(len(H) - 1):
            diff = H[i+1] - H[i]
            if diff > 0:
                if L > 0:
                    heappush(heap, diff)
                    L -= 1
                elif heap and diff > heap[0]:
                    heappush(heap, diff)
                    B -= heappop(heap)
                else: B -= diff
                if B < 0: return i
        return len(H) - 1
      
-------------------------------------------------------------
def furthestBuilding(self, H: List[int], bricks: int, ladders: int) -> int:
    jumps_pq = []
    for i in range(len(H) - 1):
        jump_height = H[i + 1] - H[i]
        if jump_height <= 0: continue
        heappush(jumps_pq, jump_height)
        if len(jumps_pq) > ladders:
            bricks -= heappop(jumps_pq)
        if(bricks < 0) : return i
    return len(H) - 1
