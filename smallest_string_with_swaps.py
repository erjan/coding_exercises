'''
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
'''

class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        d = defaultdict(list)
        for a,b in pairs:
            d[a].append(b)
            d[b].append(a)
        #
        def dfs(x,A):
            if x in d:
                A.append(x)
                for y in d.pop(x):
                    dfs(y,A)
        #
        s    = list(s)
        while d:
            x = next(iter(d))
            A = []
            dfs(x,A)
            A = sorted(A)
            B = sorted([ s[i] for i in A ])
            for i,b in enumerate(B):
                s[A[i]] = b
        return ''.join(s)
      
-------------------------------------------------------------------------------------------------------------
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Start of Union Find Data Structure
        p = list(range(len(s)))  # parent
        # each element in the pairs == node
        # used to store each node's parent based on its index
        # eg. pairs = [[0,3],[1,2]], p = [0, 1, 1, 0]
        # element 3 in pairs == p index 3 == 0 (because parent node of 3 is 0)

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                p[py] = px
                
        # End of Union Find Data Structure

        # Grouping
        for x, y in pairs:
            union(x, y)

        dic = defaultdict(list)
        for idx, el in enumerate(p):
            dic[find(el)].append(idx)
        
        # eg. pairs = [[0,3],[1,2]], dic = {0: [0, 3], 1: [1, 2]}

        # Sorting
        res = list(s)
        for key in dic.keys():
            idx_list = dic[key]
            char_list = [s[i] for i in idx_list]
            char_list.sort()

            # eg. idx_list = [0, 3], char_list = [b, d]
            # for loop below, idx = [0, b], char = [3, d]
            for idx, char in zip(idx_list, char_list):
                res[idx] = char

        return "".join(res)
---------------------------------------------------------------------------------------------------------      
      
