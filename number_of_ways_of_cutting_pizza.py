'''
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.
'''

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n, mod = len(pizza), len(pizza[0]), 10**9+7
        matrix = [[0 if c=='.' else 1 for c in l] for l in pizza]
        def A(i, j): return matrix[i][j] if 0<=i<m and 0<=j<n else 0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                matrix[i][j] += (A(i+1, j) + A(i, j+1) - A(i+1, j+1))

        @lru_cache(None)
        def dp(i, j, cut):
            if cut==0: return int(A(i, j) > 0)
            ans = 0
            for h in range(i+1, m): # cut horizontally
                if A(i, j) - A(h, j) > 0: ans += dp(h, j, cut - 1)
            
            for v in range(j+1, n): # cut vertically
                if A(i, j) - A(i, v) > 0: ans += dp(i, v, cut - 1)
            return ans%mod
        return dp(0, 0, k-1)


----------------------------------------------------------------------------------------------------------
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        
        # first, need way to query if a section contains an apple given a top left (r1, c1) and bottom right (r2, c2)
        # we can do this in constant time by keeping track of the number of apples above and to the left of any given cell
        apples = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            apples_left = 0
            for col in range(cols):
                if pizza[row][col] == 'A':
                    apples_left += 1
                apples[row][col] = apples[row-1][col] + apples_left
              
        # query if there is an apple in this rectangle using the prefix sums
        def has_apple(r1, c1, r2 = rows-1, c2 = cols-1) -> bool:
            if r1 > r2 or c1 > c2:
                return False
            tot = apples[r2][c2]
            left_sub = apples[r2][c1-1] if c1 > 0 else 0
            up_sub = apples[r1-1][c2] if r1 > 0 else 0
            upleft_sub = apples[r1-1][c1-1] if r1 > 0 < c1 else 0
            in_rect = tot - left_sub - up_sub + upleft_sub
            return in_rect > 0
        
        # memory optimized dp, keep track of only one matrix of rows x cols
        # bc we only need to access the values at the previous number of cuts
        dp = [[1 if has_apple(r, c) else 0 for c in range(cols + 1)] for r in range(rows + 1)]
        
        for cuts in range(1, k):
            new_dp = [[0] * (cols + 1) for _ in range(rows + 1)]
            for row in range(rows-1, -1, -1):
                for col in range(cols-1, -1, -1):
                    
                    for r2 in range(row, rows):
                        if has_apple(row, col, r2):
                            new_dp[row][col] += dp[r2+1][col]
                            
                    for c2 in range(col, cols):
                        if has_apple(row, col, rows-1, c2):
                            new_dp[row][col] += dp[row][c2+1]
            dp = new_dp
                            
        return dp[0][0] % (10**9 + 7)
      
---------------------------------------------------------------------------------------------------------------------------------
