'''

You are given an elevation map represents as an integer array heights where heights[i] representing the height of the terrain at index i. The width at each index is 1. You are also given two integers volume and k. volume units of water will fall at index k.

Water first drops at the index k and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

If the droplet would eventually fall by moving left, then move left.
Otherwise, if the droplet would eventually fall by moving right, then move right.
Otherwise, rise to its current position.
Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, level means the height of the terrain plus any water in that column.

We can assume there is infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than one grid block, and each unit of water has to be in exactly one block.
'''

def pourWater(self, heights, V, K):
	for _ in range(V):
		mark = K    # where to fall water

		l = K - 1   #   search left
		while l>=0:
			if heights[l] < heights[mark]:
				mark = l
			elif  heights[l] > heights[mark]:  
				break
			l -= 1
		if mark < K:
			heights[mark] += 1
			continue

		r = K + 1  #   search right
		while r < len(heights):
			if heights[r] < heights[mark]:
				mark = r
			elif heights[r] > heights[mark]:
				break
			r += 1
		heights[mark] += 1
	return heights
