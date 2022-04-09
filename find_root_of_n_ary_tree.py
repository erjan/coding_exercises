'''
You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value.

Return the root of the N-ary tree.

Custom testing:

An N-ary tree can be serialized as represented in its level order traversal where each group of children is separated by the null value (see examples).
'''

def findRoot(self, tree):

    seen = set()

    @functools.lru_cache(None)
    def dfs(node):
        if not node: return
        for i in node.children:
            seen.add(i)
            dfs(i)

    for i in tree:
        dfs(i)

    return list((set(tree) - seen))[0]
  
  
  ---------------------
  class Solution:
    def findRoot(self, tree, val = 0):
                        
        for i in tree:
            val ^= i.val
            for j in i.children:
                val ^= j.val
        
        return [node for node in tree if node.val == val][0]            
