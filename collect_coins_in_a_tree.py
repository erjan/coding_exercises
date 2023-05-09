'''
There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given an integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an array coins of size n where coins[i] can be either 0 or 1, where 1 indicates the presence of a coin in the vertex i.

Initially, you choose to start at any vertex in the tree. Then, you can perform the following operations any number of times: 

Collect all the coins that are at a distance of at most 2 from the current vertex, or
Move to any adjacent vertex in the tree.
Find the minimum number of edges you need to go through to collect all the coins and go back to the initial vertex.

Note that if you pass an edge several times, you need to count it into the answer several times.
'''

def collectTheCoins(coins: List[int], edges: List[List[int]]) -> int:
    n = len(coins)
    tree = [set() for _ in range(n)]
    
    # Build the tree from the edges
    for e in edges:
        tree[e[0]].add(e[1])
        tree[e[1]].add(e[0])
    
    # Find the leaves with zero coins
    leaf = []
    for i in range(n):
        u = i
        while len(tree[u]) == 1 and coins[u] == 0:
            v = tree[u].pop()
            tree[v].remove(u)
            u = v
        if len(tree[u]) == 1:
            leaf.append(u)
    
    # Remove the leaves one by one
    for sz in range(2, 0, -1):
        temp = []
        for u in leaf:
            if len(tree[u]) == 1:
                v = tree[u].pop()
                tree[v].remove(u)
                if len(tree[v]) == 1:
                    temp.append(v)
        leaf = temp
    
    # Count the remaining edges in the tree
    ans = 0
    for i in range(n):
        ans += len(tree[i])
    
    return ans
  
---------------------------------------------------------------------------------------------------------
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        ans = n - 1
        
        adj = [set() for i in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
                
        l = [i for i in range(n) if len(adj[i]) == 1 and coins[i] == 0]
        while l:
            nextlayer = []
            for i in l:
                # Prune leaf i
                ans -= 1
                if adj[i]:
                    j = list(adj[i])[0]
                    adj[j].remove(i)
                    adj[i].remove(j)
                    if len(adj[j]) == 1 and coins[j] == 0:
                        nextlayer.append(j)
            l = nextlayer[:]
        
        l = [i for i in range(n) if len(adj[i]) == 1]
        
        for _ in range(2):
            nextlayer = []
            for i in l:
                ans -= 1
                if adj[i]:
                    j = list(adj[i])[0]
                    adj[j].remove(i)
                    if len(adj[j]) == 1:
                        nextlayer.append(j)
            l = nextlayer[:]
            
        return 2 * max(0, ans)
