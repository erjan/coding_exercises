'''
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.
'''

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        '''
            Solves a given recurrence relation
            @params dp: the nth sum per ith equation
            @params coeff: coefficients for the ith equation
        '''
        def solve_rel(dp, coeff):
            for _ in range(n - 1):
                for i in range(len(dp)):
                    tmp = 0
                    for j, c in enumerate(coeff[i]):
                        # If j >= i we must add the second last
                        #value appended, we already updated that dp.
                        tmp += c*dp[j][-1 if j >= i else -2]
                    dp[i].append(tmp)

            return sum(e[-1] for e in dp) % 1000000007


        if m == 1:
            return solve_rel([[3]], [[2]])
        if m == 2:
            return solve_rel([[6]], [[3]])
        elif m == 3:
            return solve_rel([[6], [6]], [[3,2], [2,2]])
        elif m == 4:
            return solve_rel(
                [[6], [6], [6], [6]], 
                [[3,1,2,2], [1,2,1,1], [2,1,2,2], [2,1,2,2]])
        else:
            return solve_rel(
                [[6], [6], [6], [6], [6], [6], [6], [6]],
                [
                    [2,1,1,1,2,2,1,1], 
                    [1,2,1,1,0,0,1,0], 
                    [1,1,2,1,1,1,1,1], 
                    [1,1,1,2,2,2,1,1], 
                    [2,0,1,2,3,2,1,2], 
                    [2,0,1,2,2,2,1,2], 
                    [1,1,1,1,1,1,2,1], 
                    [1,0,1,1,2,2,1,2]
                ])
          
------------------------------------------------------------------------------------------------------
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        
        @cache
        def fn(i, j, mask): 
            """Return number of ways to color grid."""
            if j == n: return 1 
            if i == m: return fn(0, j+1, mask)
            ans = 0 
            for x in 1<<2*i, 1<<2*i+1, 0b11<<2*i: 
                mask0 = mask ^ x
                if mask0 & 0b11<<2*i and (i == 0 or (mask0 >> 2*i) & 0b11 != (mask0 >> 2*i-2) & 0b11): 
                    ans += fn(i+1, j, mask0)
            return ans % 1_000_000_007
        
        return fn(0, 0, 0)
