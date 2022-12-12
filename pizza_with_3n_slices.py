'''
There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:

You will pick any pizza slice.
Your friend Alice will pick the next slice in the anti-clockwise direction of your pick.
Your friend Bob will pick the next slice in the clockwise direction of your pick.
Repeat until there are no more slices of pizzas.
Given an integer array slices that represent the sizes of the pizza slices in a clockwise direction, return the maximum possible sum of slice sizes that you can pick.
'''

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        m=len(slices)//3
        def solve(slices,m):
            n=len(slices)
            dp=[[0 for i in range(m+1)] for j in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if i==1:
                        dp[i][j]=slices[0]
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i-2][j-1]+slices[i-1])
            return dp[n][m]
        return max(solve(slices[:-1],m),solve(slices[1:],m))
      
--------------------------------------------------------------------------------------------------------------
class Solution:
    @cache
    def dp(self, l, r, c):
        if c == 0 or l >= r:
            return 0
		return max(self.slices[l] + self.dp(l+2, r, c-1), self.dp(l+1, r, c)) # To select or not to select the current slice
		
    def maxSizeSlices(self, slices: List[int]) -> int:
        self.slices = slices + slices
        return max(self.slices[i] + self.dp(i + 2, i - 1 + len(slices), len(slices) // 3 - 1) for i in range(-3, 3)) # Handling the circular condition
