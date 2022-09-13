'''
There is a country of n cities numbered from 0 to n - 1. In this country, there is a road connecting every pair of cities.

There are m friends numbered from 0 to m - 1 who are traveling through the country. Each one of them will take a path consisting of some cities. Each path is represented by an integer array that contains the visited cities in order. The path may contain a city more than once, but the same city will not be listed consecutively.

Given an integer n and a 2D integer array paths where paths[i] is an integer array representing the path of the ith friend, return the length of the longest common subpath that is shared by every friend's path, or 0 if there is no common subpath at all.

A subpath of a path is a contiguous sequence of cities within that path.
'''

class Solution(object):
    def longestCommonSubpath(self, n, paths):
        BASE = 2 ** 46 - 1
        N = n + 2 if n % 2 == 1 else n + 1
        POWER = [1] * (max(len(path) for path in paths) + 1)
        for i in range(1, len(POWER)):
            POWER[i] = POWER[i - 1] * N % BASE
            
        prefix_hash = []
        for path in paths:
            ph = [0] * (len(path) + 1)
            for i in range(len(path)):
                ph[i + 1] = (ph[i] * N + path[i]) % BASE
            prefix_hash.append(ph)

        def find(k):  # whether there is a common sub-path of length k
            first = True
            intersection = set()
            for i in range(len(paths)):
                s = set()
                for j in range(k, len(paths[i]) + 1):
                    s.add((prefix_hash[i][j] - prefix_hash[i][j - k] * POWER[k]) % BASE)
                intersection = s if first else intersection & s
                first = False
                if not intersection: return False
            return True

        low, high = 0, min([len(path) for path in paths])
        while low <= high:
            mid = (low + high) // 2
            if find(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
