'''
You are an ant tasked with adding n new rooms numbered 0 to n-1 to your colony. You are given the expansion plan as a 0-indexed integer array of length n, prevRoom, where prevRoom[i] indicates that you must build room prevRoom[i] before building room i, and these two rooms must be connected directly. Room 0 is already built, so prevRoom[0] = -1. The expansion plan is given such that once all the rooms are built, every room will be reachable from room 0.

You can only build one room at a time, and you can travel freely between rooms you have already built only if they are connected. You can choose to build any room as long as its previous room is already built.

Return the number of different orders you can build all the rooms in. Since the answer may be large, return it modulo 109 + 7.
'''

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        tree = defaultdict(list)
        for i, x in enumerate(prevRoom): tree[x].append(i)
        
        def fn(n): 
            """Return number of nodes and ways to build sub-tree."""
            if not tree[n]: return 1, 1 # leaf 
            c, m = 0, 1
            for nn in tree[n]: 
                cc, mm = fn(nn)
                c += cc
                m = (m * comb(c, cc) * mm) % 1_000_000_007
            return c+1, m
        
        return fn(0)[1] 
