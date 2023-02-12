'''
There exists an undirected and initially unrooted tree with n nodes indexed from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Each node has an associated price. You are given an integer array price, where price[i] is the price of the ith node.

The price sum of a given path is the sum of the prices of all nodes lying on that path.

The tree can be rooted at any node root of your choice. The incurred cost after choosing root is the difference between the maximum and minimum price sum amongst all paths starting at root.

Return the maximum possible cost amongst all possible root choices.
'''





'''
My original submission was weak, and with the recently added test case, it went TLE. The comment below (thank you @user7784J) included a 
link from which I got the idea for a better way to approach the problem.

We assign a three-uplestateto each node. the root and each leaf gets (0,price,0), and each other link'sstate is 
determined by the recurence relation indfs. The figure below is for Example 1 in the problem's description.

Best way to figure it out is to trace it from the recurence relation. The correct answer is24, which is 
state[0] for node 1. BTW, if you start from a root other than0, the state for some nodes may change, but the answer doesn't.

'''




class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:

        g = defaultdict(list)
        for a, b in edges: g[a].append(b) ;  g[b].append(a)

        def dfs(node1, node2 =-1):
            p = price[node1]
            state = (0, p, 0)

            for n in g[node1]:
                if n == node2: continue

                (a1, a2, a3), (b1, b2, b3) = state, dfs(n, node1)
                
                state = (max(a1, b1, a2 + b3, a3 + b2),
                         max(a2, b2 + p),
                         max(a3, b3 + p))

            return state

        if n <= 2: return sum(price) - min(price)

        for node in range(n):
            if len(g[node]) > 1:
                return dfs(node)[0]
