'''
There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. However, there could be obstacles along the way.

You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.

For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.
The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.

For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.
Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.

Note: There will be no obstacles on points 0 and n.
'''

class Solution:
    def minSideJumps(self, obs):
        n = len(obs)
        dp = [0] * 4
        for i in range(n - 2, 0, -1):
            if obs[i] == 0 or obs[i] == obs[i - 1]: continue    # this line can be ignored
            dp[obs[i]] = min(dp[j] for j in range(1, 4) if obs[i] != j and obs[i-1] != j) + 1
        return dp[2]
      
----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minSideJumps(self, A: List[int]) -> int:
        
        # 1
        N = len(A) - 1        
        dp = [1, 0, 1]
        
        # 2
        for i in range(1, N):
            for j in range(3):
                
                # 3
                if j+1 == A[i]:
                    dp[j] = float('inf')
                else:
                    dp[j] = min(
                        dp[0] + (1 if j != 0 else 0) + (float('inf') if A[i] == 1 else 0),
                        dp[1] + (1 if j != 1 else 0) + (float('inf') if A[i] == 2 else 0),
                        dp[2] + (1 if j != 2 else 0) + (float('inf') if A[i] == 3 else 0),
                    )
                    
        # 4
        return min(dp)
      
-----------------------------------------------------------------------------------------------------------------------

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[sys.maxsize] * n for _ in range(3)]
        dp[0][0]= 1
        dp[1][0]= 0
        dp[2][0]= 1
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] if obstacles[i] != 1 else sys.maxsize
            dp[1][i] = dp[1][i-1] if obstacles[i] != 2 else sys.maxsize
            dp[2][i] = dp[2][i-1] if obstacles[i] != 3 else sys.maxsize
            if obstacles[i] != 1:
                for j in [1, 2]:
                    dp[0][i] = min(dp[0][i], dp[j][i] + 1 if obstacles[i] != j+1 else sys.maxsize)
            if obstacles[i] != 2:
                for j in [0, 2]:
                    dp[1][i] = min(dp[1][i], dp[j][i] + 1 if obstacles[i] != j+1 else sys.maxsize)
            if obstacles[i] != 3:
                for j in [0, 1]:
                    dp[2][i] = min(dp[2][i], dp[j][i] + 1 if obstacles[i] != j+1 else sys.maxsize)
        return min(dp[0][-1], dp[1][-1], dp[2][-1])
      
-------------------------------------------------------------------------------------------------------------------------------------------
