'''
You are given a 2D array of strings equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] means that Ai / Bi = values[i].

Determine if there exists a contradiction in the equations. Return true if there is a contradiction, or false otherwise.

Note:

When checking if two numbers are equal, check that their absolute difference is less than 10-5.
The testcases are generated such that there are no cases targeting precision, i.e. using double is enough to solve the problem.
'''

class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        
        m = defaultdict(lambda: defaultdict(int))
        letter_num = set()
        for u, v in equations:
            letter_num |= {u, v}
        letter_num_map = {v: k for k, v in enumerate(list(letter_num))}
        
        loc = list(range(len(letter_num_map)))
        
        def find(x):
            if loc[x] != x:
                loc[x] = find(loc[x])
            return loc[x]
        
        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                loc[a] = b
                return True
            return False
               
        def dfs(node, par, val):
            if node == b:
                return abs(val - v) < pow(10, -6)
            for nei in m[node]:
                if nei == par: continue
                if not dfs(nei, node, val * m[node][nei]):
                    return False
            return True
        
        for (a, b), v in zip(equations, values):
            a, b = letter_num_map[a], letter_num_map[b]
            if union(a, b):
                m[a][b] = v
                m[b][a] = 1/v
            else:
                if not dfs(a, None, 1): return True
        return False
