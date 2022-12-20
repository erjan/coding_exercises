'''
You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:

You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.
'''

i=index
h=max element till index i
k=number of searches left
class Solution:
   def numOfArrays(self, n: int, m: int, k: int) -> int:
        @lru_cache(None)
        def dp(i,h,k):      
            if i==n and k==0: return 1
            if i==n or k<0: return 0
            return sum(dp(i+1,max(h,j),k-(j>h)) for j in range(1,m+1))%1000000007
        return dp(0,-1,k)
