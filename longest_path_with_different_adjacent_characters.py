'''
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.
'''

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = collections.defaultdict(list)
        for i, p in enumerate(parent):
            children[p].append(i)

        max_length = 1
        def dfs(idx):
            nonlocal max_length
            if idx not in children: return 1
            
            first, second = 0, 0
            for child in children[idx]:
                curr = dfs(child)
                if s[idx]!=s[child]:
                    if curr > first:
                        second = first
                        first = curr
                    elif curr > second:
                        second = curr

            max_length = max(max_length, first+second+1)
            return first+1

        dfs(0)
        return max_length
      
--------------------------------------      
