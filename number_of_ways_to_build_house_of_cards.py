'''
You are given an integer n representing the number of playing cards you have. A house of cards meets the following conditions:

A house of cards consists of one or more rows of triangles and horizontal cards.
Triangles are created by leaning two cards against each other.
One card must be placed horizontally between all adjacent triangles in a row.
Any triangle on a row higher than the first must be placed on a horizontal card from the previous row.
Each triangle is placed in the leftmost available spot in the row.
Return the number of distinct house of cards you can build using all n cards. Two houses of cards are considered distinct if there exists a row where the two houses contain a different number of cards.

 

Example 1:


Input: n = 16
Output: 2
Explanation: The two valid houses of cards are shown.
The third house of cards in the diagram is not valid because the rightmost triangle on the top row is not placed on top of a horizontal card.
Example 2:


Input: n = 2
Output: 1
Explanation: The one valid house of cards is shown.
Example 3:


Input: n = 4
Output: 0
Explanation: The three houses of cards in the diagram are not valid.
The first house of cards needs a horizontal card placed between the two triangles.
The second house of cards uses 5 cards.
The third house of cards uses 2 cards.
'''


Each row takes 3*n-1 cards (n is number of traingles)
Bottom up (number of traingles must be less than its adjacent down row)
Base conditions
0 or 2 cards remaining, count as one valid way to build
previous down row has only 2 triangles and left more than 2 cards, no way to build
class Solution:
    def houseOfCards(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(n, prev):
            if n <= 2:
                return int(n != 1)
            if prev < 2:
                return 0
            
            ans = 0
            for i in range(2, min(prev, (n+1)//3+1)):
                ans += dp(n - 3*i + 1, i)
            return ans
        
        
        return dp(n, 10**5)
      
--------------------------------------------------------------------------------------------------
Approach #1 - O(N^3) DP, Pre-calculation
n = 500
dp = [collections.Counter() for _ in range(n+1)]     # dp[total cards][horizontal cards at top_level] = frequency
for i in range(1, n+1):
    if (i-2) % 3 == 0:
        dp[i][(i-2)//3-1] += 1
    for j in range(i//2+1, i):
        for floor, cnt in dp[j].items():
            if (i - j - 2) % 3 == 0:
                tmp = (i - j - 2) // 3
                dp[i][tmp-1] += cnt if floor >= tmp else 0
class Solution:
    def houseOfCards(self, n: int) -> int:
        return sum(dp[n].values())
Approach #2 - O(N^2) DP
Below is a Python re-write of leafybillow's solution. O(N^2) solution, very nice.
class Solution:
    def houseOfCards(self, n: int) -> int:
        t_max = (n+3)//3;
        dp = [0] * (n+1);
        dp[0]=1; 
        for t in range(1, t_max+1):
            base = 3*t-1; 
            for i in range(n, base-1, -1):
                dp[i] += dp[i-base]
        return dp[n]    
      
---------------------------------------------------------------------------------------------------
class Solution:
    def houseOfCards(self, n: int) -> int:
        ways = [Counter() for _ in range(n + 1)]
        for cards in range(1, n + 1):
            for triangles_in_top_row in range(1, (cards + 1) // 3 + 1):
                remaining = cards - 3 * triangles_in_top_row + 1
                if remaining > 0:
                    for last_row_triangles, last_row_ways in ways[remaining].items():
                        if last_row_triangles > triangles_in_top_row:
                            ways[cards][triangles_in_top_row] += last_row_ways
                elif remaining == 0:
                    ways[cards][triangles_in_top_row] = 1
        return ways[n].total()
      
Explanation:
ways[i] is a Counter indicating the number of ways to use all of i cards
when the top row has various number of triangles. For example, ways[2] = {1: 1} means there is one way 
to use 2 cards and the top row has just one triangle. Another example: ways[16] = {1: 1, 2: 1}.
      
      
