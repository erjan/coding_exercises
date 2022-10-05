'''
You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

Return the maximum number of white tiles that can be covered by the carpet.
'''


import bisect
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], l: int) -> int:
        # Sort based on tile start
        tiles.sort(key=lambda t: t[0])

        # Build prefix sum
        prefix = [0]
        for t in tiles:
            prefix.append(t[1] - t[0] + 1 + prefix[-1])
        
        res = 0
        for i in range(len(tiles)):
            curr = tiles[i]
            end = curr[0] + l - 1 # Where the carpet ends if starts from the left side of curr
            idx = bisect.bisect_right(tiles, end, key=lambda e: e[0]) - 1  # Idx of the last tile the carpet can cover
            if tiles[idx][1] <= end:  # The tile is fully covered
                cover = prefix[idx+1] - prefix[i]
            else:
                cover = (prefix[idx] - prefix[i]) + (end - tiles[idx][0] + 1)  # The tile is partially covered
                
            res = max(cover, res)
            if res == l:
                return l  # No need for further searches if all tiles are white

        return res  
      
--------------------------------------------------------------------------------------------------------------------------------
def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
	tiles.sort()
	maxCover = 0
	starts, ends = zip(*tiles)
	dp = [0]*(len(tiles) + 1) # dp: total covered lengths from 0
	for i in range(len(tiles)):
		dp[i+1] = dp[i] + ends[i] - starts[i] + 1 # length of each tile is end - start + 1
	for l in range(len(tiles)):
		e = starts[l] + carpetLen
		r = bisect_right(starts, e)
		cover = dp[r] - dp[l] - max(0, ends[r-1] - e + 1) # total cover on the right MINUS total cover on the left MINUS offset
		maxCover = max(maxCover, cover)
	return maxCover 
