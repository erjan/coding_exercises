'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer 
that is the square of an integer; in other words, it is the product of some integer 
with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
'''


class Solution:
    def numSquares(self, n: int) -> int:
		# step 1
        dp = [i for i in range(n+1)]
        
		# step 2
        for i in range(n+1):
	        j = 1
			# step 3
	        while j*j <= i:
	            dp[i] = min(dp[i], dp[i-(j*j)] + 1)
	            j += 1
        
        return dp[-1]

--------------------------------------------------------


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,int(i ** 0.5) + 1):
                dp[i] = min(dp[i],dp[i-j*j]+1)
        return dp[n]
