'''
There is a rooted tree consisting of n nodes numbered 0 to n - 1. Each node's number denotes its unique genetic value (i.e. the genetic value of node x is x). The genetic difference between two genetic values is defined as the bitwise-XOR of their values. You are given the integer array parents, where parents[i] is the parent for node i. If node x is the root of the tree, then parents[x] == -1.

You are also given the array queries where queries[i] = [nodei, vali]. For each query i, find the maximum genetic difference between vali and pi, where pi is the genetic value of any node that is on the path between nodei and the root (including nodei and the root). More formally, you want to maximize vali XOR pi.

Return an array ans where ans[i] is the answer to the ith query.
'''

class Trie: 
    def __init__(self): 
        self.root = {}
    
    def insert(self, x): 
        node = self.root
        for i in range(18, -1, -1): 
            bit = (x >> i) & 1
            node = node.setdefault(bit, {})
            node["mult"] = 1 + node.get("mult", 0)
        node["#"] = x # sentinel 
        
    def search(self, x): 
        node = self.root
        for i in range(18, -1, -1): 
            bit = (x >> i) & 1
            if 1^bit in node: node = node[1^bit]
            else: node = node[bit]
        return x ^ node["#"]
    
    def remove(self, x): 
        node = self.root
        for i in range(18, -1, -1): 
            bit = (x >> i) & 1
            node[bit]["mult"] -= 1
            if node[bit]["mult"] == 0: 
                node.pop(bit)
                break 
            node = node[bit]
        

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        mp = {}
        for i, (node, val) in enumerate(queries): 
            mp.setdefault(node, []).append([val, i])
        
        tree, root = {}, -1
        for i, x in enumerate(parents): 
            if x == -1: root = i
            else: tree.setdefault(x, []).append(i)
        
        ans = [0]*len(queries)
        trie = Trie()
        
        def fn(x): 
            """Collect query results while traversing the tree."""
            trie.insert(x)
            for v, i in mp.get(x, []): ans[i] = trie.search(v)
            for xx in tree.get(x, []): fn(xx)
            trie.remove(x)
        
        fn(root)
        return ans 
      
---------------------------------------------------------------------------------------------------------
class Trie:
    def __init__(self):
        self.root = dict()
        # store pointer to next, and frequency in 'f'
        
    def add(self, x):
        # print('add',x)
        cur = self.root
        for pwr in range(18,-1,-1):
            mask = 2**pwr # mask = 1<<pwr
            bit = 1 if mask & x else 0
            if bit not in cur:
                cur[bit] = dict()
            
            cur = cur[bit]
            cur['f'] = cur.get('f',0) + 1 # increase the frequency :)
        
        cur['val'] = x
        
    def remove(self, x):
        # print('rem',x)
        cur = self.root
        for pwr in range(18,-1,-1):
            mask = 2**pwr # mask = 1<<pwr
            bit = 1 if mask & x else 0
            cur = cur[bit]
            cur['f'] = cur.get('f',0) - 1 # increase the frequency :)
        
        cur['val'] = x
        
    def search(self, x):
        cur = self.root
        res = 0
        for pwr in range(18,-1,-1):
            mask = 2**pwr # mask = 1<<pwr
            bit = 1 - (1 if mask & x else 0) # searching for opposite
            
            if bit not in cur or cur[bit]['f'] == 0:
                # cannot find opposite..
                cur = cur[1-bit]
            else:
                cur = cur[bit]
        # print('max', x,'->',cur['val'])
        return cur['val'] ^ x
    
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
        
        def dfs(node):
            nonlocal queryForNode, trie, ans
            # at current node, trie contains everyone in my path :)
            trie.add(node)
            
            
            for val,idx in queryForNode[node]:
                ans[idx] = trie.search(val)
            
            for kid in adj[node]:
                dfs(kid)
            
            # now backtrack..
            trie.remove(node)
            
        dfs(root)
        return ans
      
-------------------------------------------------------------------------------------------------------------
