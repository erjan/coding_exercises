'''
We are playing the Guessing Game. The game will work as follows:

I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.
'''


def getMoneyAmount(self, n):
    class Need(dict):
        def __missing__(self, (lo, hi)):
            if lo >= hi:
                return 0
            ret = self[lo, hi] = min(x + max(self[lo, x-1], self[x+1, hi])
                                     for x in range(lo, hi))
            return ret
    return Need()[1, n]
-------------------------------------------------------------------    

import functools
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.lru_cache(maxsize=None)
        def get_amount(left: int, right: int) -> int:
            if left >= right: return 0
            return min(i + max(get_amount(left, i - 1), get_amount(i + 1, right)) for i in range(left, right + 1))
        return get_amount(1, n)
      
--------------------------------------------
def getMoneyAmount(self, n):
    need = [[0] * (n+1) for _ in range(n+1)]
    for lo in range(n, 0, -1):
        for hi in range(lo+1, n+1):
            need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])
                               for x in range(lo, hi))
    return need[1][n]

-----------------------------------------------------------------------------
class Solution:
    def solve(self, start, end):
        if start >= end:
            return 0
        if (start, end) in self.d:
            return self.d[(start, end)]
        self.d[(start, end)] = float("inf")
        for i in range(start, end+1):
            cost1 = self.solve(start, i-1) + i
            cost2 = self.solve(i+1, end) + i
            cost = max(cost1, cost2)
            self.d[(start, end)] = min(self.d[(start, end)], cost)
        return self.d[(start, end)]
    
    def getMoneyAmount(self, n: int) -> int:
        self.d = {}
        return self.solve(1, n)

    
----------------------------------------------------------------------------------------------------
from functools import lru_cache
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(maxsize=None) 
        def cost(arr):
            l = len(arr)
            if not l: return 0
            if l == 1: return 0
            if l == 2: return arr[0]
            if l == 3: return arr[1]
            minimum = float('inf')
            for i in range(len(arr)-2, -1, -2):
                left, right = cost(arr[:i]), cost(arr[i+1:])
                minimum = min(minimum, max(left + arr[i], arr[i] + right))
            return minimum
        return cost(tuple(range(1, n+1)))
    -----------------------------------------------------------------------------------------------------------------
    class Solution:
    def getMoneyAmount(self, n: int) -> int:
        ## RC ##
        ## APPROACH : DP - MERGE INTERVALS PATTERN ##
        ## LOGIC - BOTTOM UP ##
        ## consider numbers 1,2,3,4 (here i = 1, j = 4) ## 
        ## 1. we start by picking 2 or 3 ==> lets say we started by 2, player B says right side we pick 3 ==> so total = 5. or if player B says left side ? result will be 2 + 0 => 2. worst case scenarios is maximum of leftside and rightside. i.e for k=2 => max(5,2)
        ## 2. next if we start with 3 i.e k=3 ==> we can go left side or right side. for leftside ==> total = 3 + 1, for rightside total = 3 + 0. worst case is max(4,3) = 4
        ## In short, for start point k =2 in 1234, we need leftside [1,1] rightside[3,4] and pick worst
        ## for startpoint k = 3 in 1234, we need leftside [1,2] and rightside[4,4] and pick worst
        ## This is the reason why we need to have 2D DP matrix, to store left and right subproblems
        ## We need to return best of all worst cases, so res = minimum( worstcase( number + leftside sub problem, number + rightside subproblem ) ) 
        ## ```dp[i][j] = min( dp[i][j], max( dp[i][k-1] + k, dp[k+1][j] + k ) )``` for all startpoints of k ( k lies between i and j)
        
		## TIME COMPLEXITY : O(N^2) ##
		## SPACE COMPLEXITY : O(N^2) ##

        ## EXAMPLE : 1 2 3 4 5 6 7 ##
        # [
        #     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
        #     ['X', 0, 1, 2, 4, 6, 8, 10], 
        #     ['X', 'X', 0, 2, 3, 6, 8, 10], 
        #     ['X', 'X', 'X', 0, 3, 4, 8, 10], 
        #     ['X', 'X', 'X', 'X', 0, 4, 5, 10], 
        #     ['X', 'X', 'X', 'X', 'X', 0, 5, 6], 
        #     ['X', 'X', 'X', 'X', 'X', 'X', 0, 6], 
        #     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 0]
        # ]

        dp = [[ float('inf') ] * (n+1) for _ in range(n+1)]
        for i in range(n, 0, -1):
            for j in range(i,n+1):
                if i == j :
                    dp[i][j] = 0
                if j - i == 1:
                    dp[i][j] = i
                for k in range(i+1, j):
                    dp[i][j] = min( dp[i][j], max( dp[i][k-1] + k, dp[k+1][j] + k ) )
        # print(dp)
        return dp[1][-1]

