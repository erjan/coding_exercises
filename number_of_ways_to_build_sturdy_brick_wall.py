'''
You are given integers height and width which specify the dimensions of a brick wall you are building. You are also given a 0-indexed array of unique integers bricks, where the ith brick has a height of 1 and a width of bricks[i]. You have an infinite supply of each type of brick and bricks may not be rotated.

Each row in the wall must be exactly width units long. For the wall to be sturdy, adjacent rows in the wall should not join bricks at the same location, except at the ends of the wall.

Return the number of ways to build a sturdy wall. Since the answer may be very large, return it modulo 109 + 7.
'''


Explanation
Intuition: Try drawing something simple to help you understand the question better
Steps:
Find all possible bottom row combinations
For each combination, find its possible neighbor rows
Starting from the bottom row,
take each combination and build up to the height level
count possible ways using DFS (use @cache to avoid repeat computing, you can also write your own cache using dict)
BFS will TLE, unless a good pruning approach is worked out
Time Complexity:
It's hard to use input parameters to represent the time complexity, so I will make an estimation using worst test case
Given the most complicated input
100
10
[1,2,3,4,5,6,7,8,9,10]
Then len(combos) == 512, there are 100 level at max, so with @cache, the max computation during DFS is about O(51200)
Finding possible neighbor takes 512*512=O(262144)
In total time is at O(10^5) level
Space is capped by the adjacency list d, which is O(10^5)
Implementation
class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        combos = []
        def get_combos(cur, cur_sum):                     # 1. find all possible bottom row combination (combos)
            nonlocal combos, width
            if cur_sum > width: return
            if cur_sum == width:
                combos.append(tuple(cur))                 # if width matches, add to `combos`
                return
            for brick in bricks:
                get_combos(cur + [brick], cur_sum + brick)
        get_combos([], 0)
        
        d = collections.defaultdict(list)                 # make a adjacency list for {combo: [possible_neighbor_row...]}
        
        for i, combo in enumerate(combos):                # 2. for each `combo`, find its possible neighbor row
            s, cur = set(), 0
            for val in combo[:-1]:                        # use set `s` to store all join location, we don't care the right edge (hence combo[:-1]) 
                s.add(cur:=cur+val)
            for j, nei in enumerate(combos):    
                cur = 0                
                for val in nei[:-1]:
                    cur += val
                    if cur in s: break                    # if `combo` and its neighbor row `nei` join bricks at `cur`, then this neighbor can't be used at upper row
                else:                        
                    d[combo].append(nei)
                    
        ans, mod = 0, int(1e9+7)
        
        @cache
        def dfs(combo, h):                                # count number of ways build brick up to `height` \
            nonlocal ans, d, height                       #   with current row as `combo` at the `h`th row
            if height == h: return 1
            return sum(dfs(nei, h+1) for nei in d[combo])
            
        for combo in combos:                              # 3. for each `combo`, starting from bottom row, build up to `height`
            ans += dfs(combo, 1) % mod                    # count all possible ways and take the sum
            
        return ans % mod   
      
---------------------------------------------------------------------------
Suppose we have n row patterns and dp[i][j] stands for the total number of builds for ith row being pattern j, we can have recurrsion as dp[i][j] = sum(dp[i-1][k] for k in compatible(j)). compatible(j) gives us all the compatible row patterns with pattern j.

So what's a valid pattern and how we decide pattern i is compatible with j? First the width of a valid pattern should be width.
Second, "For the wall to be sturdy, adjacent rows in the wall should not join bricks at the same location, except at the ends of the wall." Based on that, we can calculate a prefix sum array for two patterns i and j, except the last element as that will always be the width. If the intersection of two prefix sum array is empty, they are compatible with each other.

To conclude, first we use a dfs to collect a pool of prefix sum arrays of all valid patterns (whose sum is width) . Then we iterate each pair of patterns, and once two are compatible, we build an edge between them so we can have a graph. Any two nodes are connected are two compatible row patterns. Last we use dp to count the number. Since each row count only depends on the previous one row, we can just use 2 one-row dp arrays.

def buildWall(height, width, bricks):
	pool = []
	def dfs(A):
		if A[-1] >= width:
			if A[-1] == width:
				pool.append(A[1:-1])
		else:
			for x in bricks:
				A.append(A[-1]+x)
				dfs(A)
				A.pop()
	dfs([0])
	g = collections.defaultdict(list)
	for i, A in enumerate(pool):
		for j, B in enumerate(pool):
			if not set(A) & set(B):
				g[i].append(j)
	n, M = len(pool), 10**9+7
	dp = [[1]*n,[0]*n]
	for i in range(height):
		for j in range(n):
			dp[i+1&1][j] = sum(dp[i&1][k] for k in g[j]) % M
	return sum(dp[height-1&1]) % M
For time complexity, the majority time cost happens in dp which is O(height * n^2) where n is the length of valid pattern pool.
How large can the pool be? Note the the pattern should be an increasing sequence ends up to width-1, so in the worst case, it could be all subsequence of [1,2,3,...,width-1] and n = 2^(width-1). So time complexity would be O(height*2^(width*2)).

Also note the width <= 10 is pretty small, we can use a bitmask to replace the prefix sum array. We just set all prefix_sum_array[i]th bit for a row pattern bitmask.

def buildWall(height, width, bricks):
	pool, v = [], set()
	def dfs(s,mask):
		if s >= width:
			if s == width:
				pool.append(mask^(1<<width))
		elif mask not in v:
			v.add(mask)
			for x in bricks:
				dfs(s+x,mask|(1<<s+x))
	dfs(0,0)
	g = collections.defaultdict(list)
	for i, r1 in enumerate(pool):
		for j, r2 in enumerate(pool):
			if not (r1 & r2):
				g[i].append(j)
	n, M = len(pool), 10**9+7
	dp = [[1]*n,[0]*n]
	for i in range(height):
		for j in range(n):
			dp[i+1&1][j] = sum(dp[i&1][k] for k in g[j]) % M
	return sum(dp[height-1&1]) % M

------------------------------------------------------------------------------------------
The core of the problem can be solved with dynamic programming to count valid arrangements:

We want to use a dynamic program to fill in the array indexed by height and brick arrangement, dp[height][arrangement].
For each valid brick arrangement, at height zero, there is one way to build the wall.
At each height, the recursion relation is: dp[height][arrangement] = sum(dp[height-1][neighbour] for neighbour in valid_neighbours). The total number of ways to build the wall of any height is sum(dp[height]). Since we only need the previous height, we don't need to store the whole dp array, only the previous layer.
Any two arrangements can be neighbours by looking at their cumulative-sums. For example, with bricks = [1, 2, 3], width = 3 possible arrangements are: [1, 1, 1], [1, 2], [2, 1], [3]. Their cumulative sums are [1, 2, 3], [1, 3], [2, 3], [3]. You can check that two valid neighbouring arrangements will have intersection of exactly one (because they all must get to 3).

All we need to do is compute the valid arrangements, which can be done with DFS + Backtracking, and then pre-compute valid neighbours before doing the DP. The full solution is here:

Python
class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        ways = []
        bricks = sorted(bricks)
        mod = 10**9+7
        backtrack(width, bricks, [0], ways)
        
        allowed_neighbours = collections.defaultdict(list)
        for way in ways:
            setway = set(way)
            for way2 in ways:
                if len(setway.intersection(way2)) == 1:
                    allowed_neighbours[way].append(way2)
        
        prev = {way: 1 for way in ways}
        for i in range(1, height):
            cur = {}
            for way in ways:
                cur[way] = 0
                for way2 in allowed_neighbours[way]:
                    cur[way] += prev[way2]
                cur[way] %= mod
            prev = cur
        
        return sum(prev.values()) % mod
                
        
def backtrack(width, bricks, current, results):
    if current[-1] == width:
        results.append(tuple(current[1:]))
    
    for brick in bricks:
        if current[-1] + brick > width:
            break
        current.append(current[-1]+brick)
        backtrack(width, bricks, current, results)
        current.pop()
----------------------------------------------------------------------------------------
class Solution:
    options = 0
    
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        
        # 1.
        # Create a row split option. Split is a list of coordinates where bricks adjust to each other
        # For instance if we have briks [1,2,3] and width 3 possible splits are [], [1], [2], [1,2]
        one_row_split = []               
        def build_line_options(length: int, adj: List[int]):
            if length == 0:
                one_row_split.append(adj)
            for brick_size in bricks:
                prev = 0 if len(adj) == 0 else adj[len(adj)-1] 
                if brick_size <= length:
                    build_line_options(length-brick_size, (adj + [prev+brick_size]) if prev+brick_size != width else adj)
                    
        build_line_options(width, [])
        
        # 2.
        # Function returns possible next bricks splits based on previous level 
        # For instance for prev_split = [1], return could be ([2], [3])
        @lru_cache(None)    
        def get_next_level_options(prev_split):
            res = []
            for split in one_row_split:                
                found_in_split = False 
                for s in list(prev_split):
                    if s in split:
                        found_in_split = True
                if not found_in_split:
                    res += [split]
            return tuple(res)
         
            
        # 3. 
        # Build map between split bricks and list of possible next levels 
        # 
        level_map = {}        
        def build_level_map():
            for n in one_row_split:
                level_map[tuple(n)] = get_next_level_options(tuple(n))        
        build_level_map()        
        # Add mapping for empty level
        if tuple([]) not in level_map:
            level_map[tuple([])] = tuple(one_row_split)
        
        
        # 4.
        # Recursive function that count possible options of building the wall 
        # It's essential to use chaching 
        @lru_cache(None)
        def count_options(level, prev_layer):                        
            if level == height:            
                return 1
            return sum([count_options(level+1,tuple(child)) for child in level_map[tuple(prev_layer)]])
            
            
        return count_options(0, tuple([])) % int(1e9+7)
-------------------------------------------------------------------------------------------------------------------
class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        
        # step 1: get all combinations of bricks
        ways = set()
        
        def helper(path, t):
            if t == 0:
                ways.add(path)
                return
            for i in range(len(bricks)):
                if t >= bricks[i]:
                    helper(path + (bricks[i],), t - bricks[i])

        helper(tuple(), width)
        if not ways:
            return 0
        
        # step 2: prefix sum and bitmask
        out = set()
        for way in ways:
            mask = 0
            for acc in accumulate(way):
                if acc == width: continue
                mask ^= 1 << acc
            out.add(mask)

        # step 3: build graph for non overlapping prefix sum
        nei = defaultdict(set)
        for x in out:
            nei[x] = set()
            for y in out:
                if x & y == 0: nei[x].add(y)

        # step 4: DP
        @lru_cache(None)
        def dp(i, prev):
            if i == height:
                return 1
            return sum(dp(i+1, x) % (10**9+7) for x in nei[prev]) % (10**9+7)            
        
        return sum(dp(1, x) for x in nei) % (10**9+7)
      
        

      
