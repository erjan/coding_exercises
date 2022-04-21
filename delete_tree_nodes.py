'''
A tree rooted at node 0 is given as follows:

The number of nodes is nodes;
The value of the ith node is value[i];
The parent of the ith node is parent[i].
Remove every subtree whose sum of values of nodes is zero.

Return the number of the remaining nodes in the tree.
'''


def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        children = collections.defaultdict(list)
        for i, j in enumerate(parent):
            children[j].append(i)

        def dfs(node):
            total_nodes = 1
            total_sum = value[node]
            for child in children[node]:
                child_as_root_sum, child_as_root_nodes = dfs(child)
                total_sum += child_as_root_sum
                total_nodes += child_as_root_nodes

            if total_sum == 0:
                return 0, 0
            else:
                return total_sum, total_nodes
            
        return dfs(0)[1]
      
----------------------------------------------------------------------------------------------


from functools import lru_cache
class Solution:
    def deleteTreeNodes(self, n: int, parent: List[int], value: List[int]) -> int:
        G=collections.defaultdict(list)
        for i in range(n):
            if parent[i]==-1:
                root=i
            else:
                G[parent[i]].append(i)
                   
        @lru_cache(None)
        def dfs(i):
            out = value[i]
            for j in G[i]:
                out+=dfs(j)
            return out
        
        subtreeSum = [dfs(i) for i in range(n)]
        
        def countNode(i):
            if subtreeSum[i]==0:
                return 0
            out = 1
            for j in G[i]:
                out+=countNode(j)
            return out
        return countNode(root)
--------------------------------------------------------

Algo
Build the tree as adjacency list from parent array. Post-order traverse the tree and at each node compute its sum and count of the sub-tree.

Implementation

class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        tree = {} # tree as adjacency list 
        for i, x in enumerate(parent): 
            tree.setdefault(x, []).append(i)
        
        def fn(n): 
            """Return sum and count of sub-tree rooted at n."""
            s, c = value[n], 1
            for nn in tree.get(n, []): 
                ss, cc = fn(nn)
                s += ss
                c += cc 
            return (s, c) if s != 0 else (0, 0)
        
        return fn(0)[1]
-------------------------------------------------

please upvote if you find the solutions helpful, and let me know if you have any questions

This problem seems pretty odd as it is a Tree problem, but the node pointer points to the parent, not children, so the first thing I did is to rebuild the Tree with pointer to the children such that the problem at least becomes more similar to a common Tree problem.

Iterative Method:
This iteration is a fix for the method posted in the link: https://leetcode.com/problems/delete-tree-nodes/discuss/440829/JavaC%2B%2BPython-One-pass

from collections import defaultdict
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:

        ########################
		# I need to build a dic for fast find
        # build a new arr store the # of node in the subtree
		########################
		
		# a simple boundary case, if the sum of the whole arr is 0, the root node can be deleted
        if sum(value) == 0: 
            return 0
        
		# build the arr that store the number of subtrees
        arr = [1 for i in range(nodes)]
		
		# reconstructe the Tree structure using a dictionary; key is parent, value is children
        dic = defaultdict(list) 
        for i in range(nodes):
            dic[parent[i]].append(i)
		
		# iterate the tree (note since the parent node index may be larger then the children nodes, this iteration may not iteratre from bottom to top of the tree)
        for i in range(len(parent)-1, -1, -1):
            if i not in dic:
                if value[i] == 0:
                    dic[parent[i]].remove(i) # this is important, we are virtually deleted the node in the Tree constructed in the dic, and it will avoid counting the node again
                    arr[parent[i]] -= 1
            else:
                children = dic[i]
                count = 0
                value_sum = 0
                for j in children:
                    value_sum += value[j]
                    count += arr[j]
                arr[i] = count + 1
                if value[i] + value_sum == 0:
                    value[i] = 0
                    arr[i] = 0
                else:
                    value[i] = value[i] + value_sum

        return arr[0]
Recursive Method:

class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:

        dic = defaultdict(list) # key is parent, value is children
        for i in range(nodes):
            dic[parent[i]].append(i)
        
        @lru_cache	
	# p represent the parent node idx, will return a tuple, tuple[0] is the sum_value of the tree; tuple[1] is the # of the tree
	
        def helper(p: int): 
            nonlocal dic
            if p not in dic: # indicate the p is a leaf
                if value[p] == 0:
                    return (0, 0)
                else:
                    return (value[p], 1)
            children = dic[p]
            value_sum = 0
            num = 0
            for i in children:
                A, B = helper(i)
                value_sum += A
                num += B
            if value_sum + value[p] == 0:
                return (0, 0)
            else:
                return (value_sum + value[p], num+1)
        
        return helper(0)[1]
--------------------------------------------------------------

def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        
        # build a tree {node : [list of children]}
        tree = defaultdict(list)
        for i in range(nodes):
            tree[parent[i]].append(i)
            
        # at each level, return a tuple of two elements:
        #   sum of values in subtree
        #   number of remaining nodes in subtree
        def dfs(node=0):
            if not tree[node]:
                return (value[node], value[node]!=0)
            value_sum, count = map(sum, zip(*[dfs(i) for i in tree[node]]))
            return (0, 0) if value_sum+value[node]==0 else (value_sum+value[node], count+1)
        
        return dfs()[1]
      
      
      
      
