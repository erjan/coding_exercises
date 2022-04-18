'''
You are given an integer array coins (1-indexed) of length n and an integer maxJump. You can jump to any index i of the array coins if coins[i] != -1 and you have to pay coins[i] when you visit index i. In addition to that, if you are currently at index i, you can only jump to any index i + k where i + k <= n and k is a value in the range [1, maxJump].

You are initially positioned at index 1 (coins[1] is not -1). You want to find the path that reaches index n with the minimum cost.

Return an integer array of the indices that you will visit in order so that you can reach index n with the minimum cost. If there are multiple paths with the same cost, return the lexicographically smallest such path. If it is not possible to reach index n, return an empty array.

A path p1 = [Pa1, Pa2, ..., Pax] of length x is lexicographically smaller than p2 = [Pb1, Pb2, ..., Pbx] of length y, if and only if at the first j where Paj and Pbj differ, Paj < Pbj; when no such j exists, then x < y.
'''


Continue processing if path to current has lower distance (overall distance improves) or path length is longer (lexicographic order).
Slower because top down, starting from src

from heapq import *

class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if not A or A[0] == -1:
            return []
        q = [(0, 0, -1, 1)]  # cost, idx, parent, path_len
        n = len(A)
        last = n-1 
        parent = dict()
        p_lens = [float('inf') for _ in range(n)]
        dists = [float('inf') for _ in range(n)]
        res = []
        while q:
            dist, idx, p_idx, path_len = heappop(q)
            shorter_dist = dist < dists[idx]
            longer_path = dist == dists[idx] and path_len > p_lens[idx]
            if shorter_dist or longer_path:
                dists[idx] = dist
                parent[idx] = p_idx
                p_lens[idx] = path_len
            else:
                continue
            
            if idx == last:
                curr = idx
                path = [curr]
                while parent[curr] != -1:
                    path.insert(0, parent[curr])
                    curr = parent[curr]
                res = list(map(lambda x: x+1, path))

            # append neighbour
            for nex in range(idx+1, min(n, idx+B+1)):
                if A[nex] == -1:
                    continue
                new_dist = dist + A[nex]
                if new_dist < dists[nex]:
                    heappush(q, (new_dist, nex, idx, path_len+1))
        return res
------------------------------------------------------------------------------
class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        @cache
        def min_cost_path(start):
            if coins[start] == -1:
                return math.inf, []
            
            if start == len(coins) - 1:
                return (coins[start], [start])
            
            min_cost, min_path = math.inf, []
            end = min(start + maxJump + 1, len(coins))
            
            for i in range(end - 1, start, -1):
                cost, path = min_cost_path(i)
                if (cost, path) < (min_cost, min_path):
                    min_cost, min_path = cost, path
            return coins[start] + min_cost, [start] + min_path
        
        _, path = min_cost_path(0)
        if path[-1] != len(coins) - 1:
            return []
        return [i + 1 for i in path]
      
-----------------------------------------------------------------
I used DP. dp[i] represent the best path found to get to the place indexed i + 1 and dp[i][0] is the cost of the path.
dp[0] is initialized as [A[0], 1] and the others are initialized as [infinity].

def cheapestJump(self, A, B):
        if not A or A[0] == -1: return []
        dp = [[float('inf')] for _ in A]
        dp[0] = [A[0], 1]
        for j in range(1, len(A)):
            if A[j] == -1: continue
            dp[j] = min([dp[i][0] + A[j]] + dp[i][1:] + [j + 1] for i in range(max(0, j - B), j))
        return dp[-1][1:] if dp[-1][0] < float('inf') else []
---------------------------------------------------------------------------

def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if A[-1] == -1: return []
        dp = [None] * len(A)
        dp[-1] = (A[-1], len(A))
        window = collections.deque()
        window.append((A[-1], len(A)-1))
        i = len(A) - 2
        while i >= 0:
            if not window: break
            if A[i] != -1:
                cost = A[i] + window[-1][0]
                to = window[-1][1]
                dp[i] = (cost, to)
                while window and window[0][0] >= cost:
                    window.popleft()
                window.appendleft((cost, i))
            if i + B == window[-1][1]:
                window.pop()
            i -= 1
        if not dp[0]:
            return []
        i = 0
        result = []
        while i != len(A):
            result.append(i + 1)
            i = dp[i][1]
        return result
      
----------------------------------------------------------------
   def cheapestJump(self, A: List[int], B: int) -> List[int]:
        n = len(A)
        dp = [10**9 for _ in range(n)]
        paths = [[] for _ in range(n)]
        
        dp[0], paths[0] = A[0], [1]
        for i in range(n):
            for b in range(1, B+1):
                nb = i + b
                if nb < n and A[nb] != -1:
                    nxt = dp[i] + A[nb]
                    if dp[nb] > nxt or (dp[nb] == nxt and tuple(paths[nb]) > tuple(paths[i] + [nb+1])):
                        dp[nb] = nxt
                        paths[nb] = paths[i] + [nb+1]
       
        return [] if dp[n - 1] == 10**9  else paths[n - 1]
      
      
      
      
