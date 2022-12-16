'''
You are given a 0-indexed binary string floor, which represents the colors of tiles on a floor:

floor[i] = '0' denotes that the ith tile of the floor is colored black.
On the other hand, floor[i] = '1' denotes that the ith tile of the floor is colored white.
You are also given numCarpets and carpetLen. You have numCarpets black carpets, each of length carpetLen tiles. Cover the tiles with the given carpets such that the number of white tiles still visible is minimum. Carpets may overlap one another.

Return the minimum number of white tiles still visible.
'''

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        
        @cache
        def fn(i, n):
            """Return min while tiles at k with n carpets left."""
            if n < 0: return inf 
            if i >= len(floor): return 0 
            if floor[i] == '1': return min(fn(i+carpetLen, n-1), 1 + fn(i+1, n))
            return fn(i+1, n)
        
        return fn(0, numCarpets)
      
--------------------------------------------------------------------------------------------------
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        dp = [[0]*(1 + numCarpets) for _ in range(len(floor)+1)]
        for i in range(len(floor)-1, -1, -1): 
            for j in range(0, numCarpets+1): 
                if floor[i] == '1': 
                    dp[i][j] = 1 + dp[i+1][j] 
                    if j: 
                        if i+carpetLen >= len(floor): dp[i][j] = 0 
                        else: dp[i][j] = min(dp[i+carpetLen][j-1], dp[i][j])
                else: dp[i][j] = dp[i+1][j]
        return dp[0][numCarpets]
