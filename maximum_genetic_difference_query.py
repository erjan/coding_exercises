'''
There is a rooted tree consisting of n nodes numbered 0 to n - 1. Each node's number denotes its unique genetic value (i.e. the genetic value of node x is x). The genetic difference between two genetic values is defined as the bitwise-XOR of their values. You are given the integer array parents, where parents[i] is the parent for node i. If node x is the root of the tree, then parents[x] == -1.

You are also given the array queries where queries[i] = [nodei, vali]. For each query i, find the maximum genetic difference between vali and pi, where pi is the genetic value of any node that is on the path between nodei and the root (including nodei and the root). More formally, you want to maximize vali XOR pi.

Return an array ans where ans[i] is the answer to the ith query.
'''

class Trie: 
    # dict() will TLE
    # [kid0, kid1, freq, val] # this is the structure of Trie
    def __init__(self):
        self.root = [False, False, 0, False]
        # store pointer to next, and frequency in 'f'
        
    def add(self, x):
        # print('add',x)
        cur = self.root
        for pwr in range(17,-1,-1):
            mask = 2**pwr # mask = 1<<pwr
            bit = 1 if mask & x else 0
            if not cur[bit]:
                cur[bit] = [False, False, 0, False]
            
            cur = cur[bit]
            cur[2] += 1 # increase the frequency :)
        
        cur[3] = x
        
    def remove(self, x):
        # print('rem',x)
        cur = self.root
        for pwr in range(17,-1,-1):
            mask = 2**pwr # mask = 1<<pwr
            bit = 1 if mask & x else 0
            cur = cur[bit]
            cur[2] -= 1 # increase the frequency :)
        
        
    def search(self, x):
        cur = self.root
        res = 0
        for pwr in range(17,-1,-1):
            mask = 2**pwr # mask = 1<<pwr
            bit = 1 - (1 if mask & x else 0) # searching for opposite
            
            if not cur[bit] or cur[bit][2] == 0:
                # cannot find opposite..
                cur = cur[1-bit]
            else:
                cur = cur[bit]
        # print('max', x,'->',cur['val'])
        return cur[3] ^ x
    
class Solution:
    def getAdj(self, parents):
        adj = defaultdict(list)
        for i, p in enumerate(parents):
            adj[p].append(i)
        return adj
    
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        # every node should have a set of all parents i.e. it's `path`
        # inside a trie, so it is a 'DFS' which will have the entire path
        # and while going backtrack in DFS we pop from trie..
        root = [i for i,v in enumerate(parents) if v == -1][0]
        adj = self.getAdj(parents) # pointers to the kids 
        
        trie = Trie()

        ans = [0]*len(queries)        
        queryForNode = defaultdict(list)
        for i, (node, val) in enumerate(queries):
            queryForNode[node].append((val,i))
        
        self.seen = 0
        
        def dfs(node):
            nonlocal queryForNode, trie, ans
            # at current node, trie contains everyone in my path :)
            trie.add(node)
            
            
            for val,idx in queryForNode[node]:
                ans[idx] = trie.search(val)
                self.seen += 1
                
            for kid in adj[node]:
                dfs(kid)
            
            # now backtrack..
            if self.seen < len(ans): # TLE without this
                trie.remove(node)
            
        dfs(root)
        return ans
