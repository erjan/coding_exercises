'''
Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

Every song is played at least once.
A song can only be played again only if k other songs have been played.
Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.
'''

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        prev_p, cur_p = [0] * (n+1), [0] * (n+1)
        
        for i in range(k+1, goal+1):
            if i == k+1:
                prev_p[i] = math.factorial(n) // math.factorial(n-i)
            else:
                for j in range(k+1, min(i, n)+1):
                    cur_p[j] = prev_p[j-1] * (n - j + 1) + prev_p[j] * (j-k)
                prev_p, cur_p = cur_p, [0] * (n+1)
        return prev_p[n] % (10**9 + 7)
      
------------------------------------------------------------------------------------------------
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp=[[0]*(n+1) for _ in range(goal+1)]  
        mod=10**9+7
        ans=0
        dp[1][1]=n
        for idx in range(2,goal+1):
            for num in range(1,n+1):
                dp[idx][num]+=dp[idx-1][num]*(max(0,num-k))
                if num>1: dp[idx][num]+=dp[idx-1][num-1]*(n-num+1)
                dp[idx][num]%=mod
        return dp[goal][n]
