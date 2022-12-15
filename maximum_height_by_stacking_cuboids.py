'''
Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

Return the maximum height of the stacked cuboids.
'''


def maxHeight(self, cuboids: List[List[int]]) -> int:
	
	# Build a list of all possible (3) orientations for each block
	index = collections.defaultdict(list)
	for i,dim in enumerate(cuboids):
		a, b, c = sorted(dim)
		index[i] = [[a, b, c], [a, c, b], [b, c, a]]
	
	# Compute the bit-mask for each index i.e. binary '1000' is block #3 and '10' is block #1
	mask = [1 << i for i in range(len(cuboids))]
	
	@functools.lru_cache(None)
	def helper(L, W, H, used):
		
		best = 0
		
		# filter out unusable blocks
		available = []
		for i in range(len(cuboids)):
			if not (used&mask[i]):
				found_match = False
				for l, w, h in index[i]:
					if l <= L and w <= W and h <= H:
						available.append(i)
						break
				else:
					used |= mask[i]
		
		# Try adding each usable block to the tower
		for i in available:
			for l, w, h in index[i]:
				if l <= L and w <= W and h <= H:
					best = max(best, h + helper(l, w, h, used | mask[i]))
		
		return best
	
	return helper(math.inf, math.inf, math.inf, 0)          

-----------------------------------------------------------------------------------------------------------------
Sort each cub's length, width, height from small to large
Sort cub by length, width, height from large to small
Initialize a 1-D dp array, dp[i] = largest height if put cuboids[i] at the top
Iterate over cuboids, from large to small; try get the largest height by putting itself on previous cube cub[j] (j < i)
Record height while iterating and return the maximum height
Time: O(N*N)
Space: O(N)
Implementation
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = sorted([sorted(cub) for cub in cuboids], reverse=True)   # sort LxWxH in cube, then sort cube reversely
        ok = lambda x, y: (x[0] >= y[0] and x[1] >= y[1] and x[2] >= y[2]) # make a lambda function to verify whether y can be put on top of x
        n = len(cuboids)
        dp = [cu[2] for cu in cuboids]                                     # create dp array
        ans = max(dp)
        for i in range(1, n):                                              # iterate over each cube
            for j in range(i):                                             # compare with previous calculated cube
                if ok(cuboids[j], cuboids[i]):                             # update dp[i] if cube[i] can be put on top of cube[j]
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])              # always get the maximum
            ans = max(ans, dp[i])                                          # record the largest value
        return ans
