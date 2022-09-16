'''
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.
'''

Intuition
Greedily paint nodes one by one.
Because there is no node that has more than 3 neighbors,
always one possible color to choose.

   def gardenNoAdj(self, N, paths):
        res = [0] * N
        G = [[] for i in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res
      
---------------------------------------------------------------------------
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        for path in paths:
            G[path[0]].append(path[1])
            G[path[1]].append((path[0]))
        colored = defaultdict()

        def dfs(G, V, colored):
            colors = [1, 2, 3, 4]
            for neighbour in G[V]:
                if neighbour in colored:
                    if colored[neighbour] in colors:
                        colors.remove(colored[neighbour])
            colored[V] = colors[0]

        for V in range(1, N + 1):
            dfs(G, V, colored)

        ans = []
        for V in range(len(colored)):
            ans.append(colored[V + 1])

        return ans
