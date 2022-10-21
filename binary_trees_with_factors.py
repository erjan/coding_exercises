'''
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.
'''


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        
        arr.sort()
        MOD = 10**9 + 7
        
        # create a dictionary and initialize
        dp = {}
        for n in arr:
            dp[n] = 1
            
        # loop through each number
        for i, n in enumerate(arr):
            for j in range(i):
                if not(n % arr[j]) and n // arr[j] in dp:
                    dp[n] += dp[arr[j]] * dp[n//arr[j]]
                    dp[n] %= MOD
        
        return sum(dp.values()) % MOD
        
        
---------------------------------------------------------------------------------------------------------------------------
Let dp(num) be the answer to the question: how many binary trees exists such that their root equal to num and they follow the problem statement. We can calculate this number of trees, if we look at the left subtree and at the right subtree. So, first of all we create s_arr: set of possible values, and then for each cand in s_arr, we check:

If num % cand == 0, that is number is divisible.
If num//cand in s_arr, that is if the second children also in set of admissible values.
We add dp(cand)*dp(num//cand) to ans, total number of trees we found. Note that we define ans = 1, because we can always have tree with one node.
Complexity: time complexity is O(n^2), because we have n different states and from each state we make at most O(n) steps. Space complexity is O(n).

class Solution:
    def numFactoredBinaryTrees(self, arr):
        s_arr, N = set(arr), 10**9 + 7
        
        @lru_cache(None)
        def dp(num):
            ans = 1
            for cand in s_arr:
                if num % cand == 0 and num//cand in s_arr:
                    ans += dp(cand)*dp(num//cand)
            return ans
        
        return sum(dp(num) for num in s_arr) % N
        
        
        
