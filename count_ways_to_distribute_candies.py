'''
There are n unique candies (labeled 1 through n) and k bags. You are asked to distribute all the candies into the bags such that every bag has at least one candy.

There can be multiple ways to distribute the candies. Two ways are considered different if the candies in one bag in the first way are not all in the same bag in the second way. The order of the bags and the order of the candies within each bag do not matter.

For example, (1), (2,3) and (2), (1,3) are considered different because candies 2 and 3 in the bag (2,3) in the first way are not in the same bag in the second way (they are split between the bags (2) and (1,3)). However, (1), (2,3) and (3,2), (1) are considered the same because the candies in each bag are all in the same bags in both ways.

Given two integers, n and k, return the number of different ways to distribute the candies. As the answer may be too large, return it modulo 109 + 7.
'''



Current state of nth candy and kth bag relies on the state of previous candy(n-1) as per k-1th bag and kth bag.
1.1. k-1th bag state will help to determine the condition of adding a new bag(k)
1.2. kth bag state will help to determine the possible ways of adding to any of the k bags
Use the above property to solve for each combination of candy and bag
     Bags ->      0        1        2
	   
Candies
   |     0        1        0        0
   V
         1        0        1        0

         2        0        1        1

         3        0        1        3 (bag * same_bag_previous_candy_state + previous_bag_previous_candy_state)

         4        0        1        7 (same as above for every cell)
Python

    threshold = 10 ** 9 + 7
Brute Force Approach - Top Down - TLE
    def top_down(candies: int, bags: int) -> int:
        if candies == 0:
            return 0
        if bags == 1:
            return 1
        return ((top_down(candies - 1, bags) * bags) % threshold + top_down(candies - 1, bags - 1)) % threshold
Memoize - Top Down - TLE
    def top_down_memoize(candies: int, bags: int, cache: dict) -> int:
        if candies == 0:
            return 0
        if bags == 1:
            return 1
        key = str(candies) + "." + str(bags)
        if key in cache:
            return cache[key]
        cache[key] = ((top_down_memoize(candies - 1, bags, cache) * bags) % threshold
                      + top_down_memoize(candies - 1, bags - 1, cache)) % threshold
        return cache[key]
Bottom Up - candies * bags space
    def bottom_up_bags_candies_space(candies: int, bags: int) -> int:
        cache = [[0 for _ in range(bags + 1)] for _ in range(candies + 1)]
        cache[0][0] = 1
        for candy in range(1, candies + 1):
            for bag in range(1, bags + 1):
                cache[candy][bag] = ((bag * cache[candy - 1][bag]) % threshold + cache[candy - 1][bag - 1]) % threshold
        return cache[candies][bags]
Bottom Up - bags linear space
    def bottom_up_bags_space(candies: int, bags: int) -> int:
        cache = [0 for _ in range(bags + 1)]
        cache[0] = 1  # 0 bag 0 candy
        for candy in range(1, candies + 1):
            diagonal = cache[0]  # previous bag previous candy
            for bag in range(1, bags + 1):
                diagonal, cache[bag] = cache[bag], ((bag * cache[bag]) % threshold + diagonal) % threshold
            cache[0] = 0  # 0 bag (with non zero candies)
        return cache[bags]
      
      
-------------------------------------------------------------------------------------
Suppose dp[n][k] is the number of ways to distribute n candies for k bags, we can come up with the recursion:

dp[n][k] = k*dp[n-1][k] + dp[n-1][k-1]
As we can either put nth candy to any of existed k bags, or put it to a new bag which is the kth bag.
Base cases are dp[i][1] = dp[i][i] = 1.

Notice (n,k) only depend on (n-1,k) and (n-1,k-1), we use dp rolling to reduce it to 1D.

def waysToDistribute(n, k):
    M = 10**9+7
    dp = [1] * (k+1)
    for i in range(1,n):
        for j in range(min(i,k), 1, -1):
            dp[j] = (j*dp[j] + dp[j-1]) % M
    return dp[k]
The ith outer iteration calculates dp[i'+1][j] in 2D scenario. We don't need the iteration i=0 as dp[1] has been manually set as 1.
We don't need to worry about dp[i][j] when i < k so we always iterate j from min(i,k).
C++

int waysToDistribute(int n, int k) {
    int M = 1e9+7;
    vector<long long> dp(k+1, 1);
    for(int i = 1; i < n; i++)
        for(int j = min(i,k); j > 1; j--)
            dp[j] = (j*dp[j] + dp[j-1]) % M;
    return dp[k];
}
                                      ---------------------------------------------------------------------------------
                                      
                                      The steps for dp is to find the dp state, list the state transfer function, and identify the base cases.

It is very intuitive to write top-down dp, but it will result in MLE. The space complexity is O(n * k) because there are n * k possible states.

class Solution:
	def waysToDistribute(self, n: int, k: int) -> int:
		mem = {}
		def dp(n, k):
			if k < 0 or n < k: return 0 # no bag or not enough candies for each bag
			if n == k: return 1
			if (n, k) not in mem:
				mem[(n, k)] = (dp(n-1, k-1) + k * dp(n-1, k)) % (10**9+7)
			return mem[(n, k)]
		
		return dp(n, k)
Therefore, we should proceed to bottom-up dp for better space-complexity.
If we use 2-D array, the space complexity is still O(n * k), but it will be accepted.

class Solution:
	def waysToDistribute(self, n: int, k: int) -> int:
		dp = [[0]*(n+1) for _ in range(k+1)]
		
		for i in range(k):
			dp[i][i] = 1
		
		for i in range(1, k+1):
			for j in range(n):
				dp[i][j+1] = (dp[i-1][j] + i * dp[i][j]) % (10**9+7)

		return dp[k][n]
Notice that we only focus on two rows each time instead of the whole dp array, make the following optimization.
Now the space complexity becomes O(n), as we only need two 1d array with length n+1.

class Solution:
	def waysToDistribute(self, n: int, k: int) -> int:
		dp = [1] + [0]*n
		
		for i in range(1, k+1):
			# initiate the basecase
			# for k bags and n candies, there is 1 way to distribute
			dp1 = [0]*(n+1)
			dp1[i] = 1
			
			# use dp1 and dp to keep track of current row and next row
			for j in range(n):
				dp1[j+1] = (dp[j] + i * dp1[j]) % (10**9+7)
			dp = dp1
			
		return dp[-1]
