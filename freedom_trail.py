'''
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
'''


import sys
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m = len(key)
        n = len(ring)
        dp = [[sys.maxsize for i in range(n)] for j in range(m)]
        for i, c in enumerate(ring):
            if c == key[0]:
                dp[0][i] = min(i, n - i)
        
        for i in range(1, m):
            for j in range(n):
                if key[i] == ring[j]:
                    for k in range(n):
                        if key[i - 1] == ring[k]:
                            dp[i][j] = min(dp[i][j], dp[i - 1][k] + min(abs(j - k), n - abs(j - k)))
        
        return min(dp[m - 1]) + m
      
--------------------------------------------------------------------------------------------------------------
from collections import defaultdict
from functools import cache
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def distance(i, j):
            if j < i: i, j = j, i
            return min(j-i, i+len(ring)-j)  # try going left or right in ring
        opts = defaultdict(list)
        for i, c in enumerate(ring):
            opts[c].append(i)
        @cache
        def dfs(k, i):
            if k == len(key): return 0
            return min(distance(i, j) + 1 + dfs(k+1, j) for j in opts[key[k]])
        return dfs(0, 0)
