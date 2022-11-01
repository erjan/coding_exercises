'''
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:
'''

def knightDialer(self, N):
    # Neighbors maps K: starting_key -> V: list of possible destination_keys
    neighbors = {
        0:(4,6),
        1:(6,8),
        2:(7,9),
        3:(4,8),
        4:(0,3,9),
        5:(),
        6:(0,1,7),
        7:(2,6),
        8:(1,3),
        9:(2,4)
    }
    current_counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for _ in range(N-1):
        next_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for src_key in range(10):
            for dst_key in neighbors[src_key]:
                next_counts[dst_key] = (next_counts[dst_key] + current_counts[src_key]) % (10**9 + 7)
        current_counts = next_counts
    return sum(current_counts) % (10**9 + 7)
  
---------------------------------------------------------------------------------------------------------------------
class Solution:
    def knightDialer(self, n: int) -> int:
	# paths represents every key we can go to from given key
	# -1 is starting condition, we can start from any key
        paths = {-1: [0,1,2,3,4,5,6,7,8,9], 0: [4,6], 1: [6,8], 2: [7,9], 
		3: [4,8], 4: [0,3,9], 5: [], 6: [0,1,7], 7: [2,6], 8: [1,3], 9: [2,4] }
        
        return self.helper(paths, n, -1, {}) % (10 ** 9 + 7)
        
    def helper(self, paths, idx, curr, cache):
        if (idx,curr) in cache:
            return cache[(idx,curr)]
        if idx == 0:
            return 1
        
        count = 0
        for num in paths[curr]:
            count += self.helper(paths, idx-1, num, cache)
        
        cache[(idx,curr)] = count
        return count
