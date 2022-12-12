'''
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:

Get the XOR of all the values of the nodes for each of the three components respectively.
The difference between the largest XOR value and the smallest XOR value is the score of the pair.
For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
Return the minimum score of any possible pair of edge removals on the given tree.
'''

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        s,n=0,len(nums)
        for x in nums:
            s^=x
        es=[[] for _ in range(n)]
        for a,b in edges:
            es[a].append(b)
            es[b].append(a)
        def f(a,b,c):
            return max(a,b,c)-min(a,b,c)
        def dfs(x,par=-1):
            S,m,p=[],10**9,nums[x]
            for y in es[x]:
                if y!=par:
                    t,u,v=dfs(y,x)
                    m=min(m,u,min(f(s^v,v^k,k) for k in t) if t else u)
                    t.add(v)
                    S.append(t)
                    p^=v
            r=set()
            for t in S:
                r|=t
            for i in range(len(S)):
                for j in range(i+1,len(S)):
                    m=min(m,min(f(s^k^l,k,l) for k in S[i] for l in S[j]))
            return r,m,p
        return dfs(0)[1]
            
        
-------------------------------------------------------------------------------------------
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        tree = [set() for _ in range(n)]
        for e in edges:
            tree[e[0]].add(e[1])
            tree[e[1]].add(e[0])

        def make_tree(i, parent):
            ancestors[i].add(parent)
            for j in ancestors[parent]:
                ancestors[i].add(j)
            tree[i].remove(parent)
            for child in tree[i]:
                make_tree(child, i)
                xor[i] ^= xor[child]

        xor = [nums[i] for i in range(n)]
        ancestors = [set() for _ in range(n)]
        for child in tree[0]:
            make_tree(child, 0)
            xor[0] ^= xor[child]

        ans = 2 ** 31 - 1
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if i in ancestors[j]:
                    parts = [xor[0] ^ xor[i], xor[i] ^ xor[j], xor[j]]
                elif j in ancestors[i]:
                    parts = [xor[0] ^ xor[j], xor[i], xor[i] ^ xor[j]]
                else:
                    parts = [xor[0] ^ xor[i] ^ xor[j], xor[i], xor[j]]
                ans = min(ans, max(parts) - min(parts))
        return ans
