'''
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.
'''

from collections import Counter


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n = len(target), len(words[0])
		# I did some space imporvements:
		# 1. I only use 2 instead m arrays, since num_ways[i] only depend on num_ways[i-1]
		# 2. I save a sum_num_ways to record summation. Instead, I use num_ways to record it. 
		# If this is a big jump for you, you can start from not applying any space imporvement as I did first. 
        num_ways = [[0]*n for _ in range(2)]
        chars_count = [Counter([word[idx] for word in words]) for idx in range(n)]
        num_ways[0][0] = chars_count[0][target[0]]
        for j in range(1, n):
            num_ways[0][j] = chars_count[j][target[0]]
            num_ways[0][j] += num_ways[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                num = num_ways[0][j-1]
                num_ways[1][j] = num*chars_count[j][target[i]]
                num_ways[1][j] += num_ways[1][j-1]
            for j in range(n):
                num_ways[0][j] = num_ways[1][j]
        return num_ways[1][n-1]%(10**9+7)
========================================================================================================================
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        @lru_cache(None)
		# dfs(i, j) is number of ways to construct taget[:i+1] using chars with index at most j in the word in the words dictionary. 
        def dfs(i, j):
            if i < 0:
                return 1
            if j < 0:
                return 0
            # 
            ans = dfs(i, j-1)
            if chars_count[j][target[i]] > 0:
                ans += dfs(i-1, j-1)*chars_count[j][target[i]]
                ans %= 10**9+7
            return ans
            
        
        m, n = len(target), len(words[0])
        chars_count = [Counter([word[idx] for word in words]) for idx in range(n)]
        return dfs(m-1, n-1)

