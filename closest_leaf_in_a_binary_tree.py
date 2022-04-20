'''
Given the root of a binary tree where every node has a unique value and a target integer k, return the value of the nearest leaf node to the target k in the tree.

Nearest to a leaf means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.
'''


General Idea: Recursively search from root on left and right subtrees which each recursive call returning the distance of the target to the current node if found, else returns -1 or NULL/None. Whereever the target is found, look for nearest leaf (distance from target + distance to the leaf) from:

Below the target node, and
On the opposite branch to which the target is found on the parent/ancestor nodes.
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.closestLeaf = [float("inf"), root.val]
        
        # Returns distance from the target node if found else returns None.
        def findTarget(node, target):
            if not node:
                return None
            
            if node.val == target:
                # find all leaves under the target node
                findClosestLeafBelow(node, 0)
                return 0
            
            # Look for the closest leaf in the opposite branch where the target node was found
            L, R = findTarget(node.left, target), findTarget(node.right, target)
            if L != None:
                findClosestLeafBelow(node.right, L+2)
                return L+1
            if R != None:
                findClosestLeafBelow(node.left, R+2)
                return R+1
            
            return None 
        
        def findClosestLeafBelow(node, distance):
            if not node:
                return
            
            # If we are already further than closest leaf found so far no point searching further
            if distance > self.closestLeaf[0]:
                return
        
            if node.left:
                findClosestLeafBelow(node.left, distance + 1)
            if node.right:
                findClosestLeafBelow(node.right, distance + 1)
            if not node.left and not node.right and distance < self.closestLeaf[0]:
                self.closestLeaf = [distance, node.val]
        
        targetDepth = findTarget(root, k)
        
        return self.closestLeaf[1]
      
-------------------------------------------------

Intuition
There are 3 branches that might lead to a closest leaf of node with value k
Left subtree, right subtree, parent_cloest_leaf + 1
We do it in 2 pass
First pass, we use post-order traversal to count only left subtree and right subtree; save each node closest leaf in a dictionary.
Second pass, we locate the node with value k, and at the same time, we use pre-order traversal to update the closest leaf with parent branch information.
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        def postorder(node):
            nonlocal d
            if not node: return d[node]
            elif node and not node.left and not node.right: d[node] = (1, node)
            else:
                l_step, l_node = postorder(node.left)
                r_step, r_node = postorder(node.right)
                d[node] = (l_step+1, l_node) if l_step < r_step else (r_step+1, r_node)
            return d[node]
        d = {None: (sys.maxsize, None)}
        postorder(root)
        ans = -1
        def preorder(node, parent):
            nonlocal ans
            if not node: return
            p_step, p_node = d[parent]
            n_step, n_node = d[node]
            if p_step + 1 < n_step: d[node] = d[parent]
            if node and node.val == k: ans = d[node][1].val; return
            preorder(node.left, node)
            preorder(node.right, node)
        preorder(root, None)    
        return ans
-------------------------------------------------

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        def getPath(node, n):
            if not node:
                return (False, [])
         
			if node.val == n:
                return (True, [n])
            
            right = getPath(node.right,n)
            left = getPath(node.left, n)
            if right[0]:
                return (True, [node.val] + right[1])
            elif left[0]:
                return (True, [node.val] + left[1])
            else:
                return (False, [])
        
        hashtable = {}
        pathToK = getPath(root,k)
        
        def getDistance(arr1, arr2):
            i = 0
            j = 0
            while(i < len(arr1) and j < len(arr2) and arr1[i] == arr2[j]):
                i+=1
                j+=1
            return len(arr1) - j + len(arr2) - i
        
        def leafDistance(node):
            if not node:
                return
            if not node.left and not node.right:
                pathToNode = getPath(root,node.val)
                distance = getDistance(pathToNode[1],pathToK[1])
                hashtable[node.val] = distance
            else:
                leafDistance(node.right)
                leafDistance(node.left)
                
        leafDistance(root)
        
        minDistance = float('inf')
        output = -1
        for key, value in hashtable.items():
            if value <= minDistance:
                output = key
                minDistance = value
        return output
        
-----------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        
        graph = defaultdict(list)
        
        stack = [root]
        
        while stack:
            
            item = stack.pop()
            if item.left:
                stack.append(item.left)
                graph[item.val].append(item.left.val)
                graph[item.left.val].append(item.val)
                
            if item.right:
                stack.append(item.right)
                graph[item.val].append(item.right.val)
                graph[item.right.val].append(item.val)
                
        def get_leafs(root):
            if not root: 
                return []
            if not root.left and not root.right: 
                return [root.val]
            leaves = get_leafs(root.left) + get_leafs(root.right)
            return leaves
        
        leafs = get_leafs(root)
        
        stack = deque([k])
        seen = set()
        seen.add(k)
        while stack:
            
            item = stack.popleft()
            if item in leafs:
                return item
            
            for nei in graph[item]:
                
                if nei not in seen:
                    stack.append(nei)
                    seen.add(nei)
----------------------------------------------------------------------

First, I submitted my solution using dfs + dfs and then by bfs + dfs. The approach calculated the distance in two steps:

Calculate the distance from root to k
Calculate every leaf node distance and parents. When you have all the nodes to a leave, do set operation to set from Step 1. The union - intersection between these two nodes, is the distance to the leaf from k.
After seeing other solutions, I also used the approach of using graphs with bfs + dfs and bfs + bfs

Of all these, I saw better runtime with last approach of graphs using BFS + BFS

# DFS + DFS
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if not node:
                return None
            if node.val == k:
                return [k]
            l = dfs(node.left)
            r = dfs(node.right)
            
            if not l and not r:
                return None
            if l:
                return [node.val] + l
            if r:
                return [node.val] + r
        k_path = set(dfs(root))
        k_l = len(k_path)
        
        def dfs_height(node, parents):
            if node.left is None and node.right is None:
                path_l = len(k_path.union(set(parents + [node.val]))) - len(k_path.intersection(set(parents + [node.val])))
                return (path_l, node.val)
            
            if node.left:
                l = dfs_height(node.left, parents + [node.val])
            else:
                l = (float('inf'), 0)
            if node.right:
                r = dfs_height(node.right, parents + [node.val])
            else:
                r = (float('inf'), 0)
            
            if l[0] < r[0]:
                return l
            else:
                return r
        return dfs_height(root, [])[1]
        
########**** BFS + DFS *****#######
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        
        from collections import deque
        que = deque([[root, []]])
        k_path = None
        while que:
            cur_node = que.popleft()
            cur_node, parents = cur_node[0], cur_node[1]
            if cur_node.val == k:
                k_path = set(parents + [cur_node.val])
                que = deque([])
            else:
                if cur_node.left:
                    que.append([cur_node.left, parents + [cur_node.val]])
                if cur_node.right:
                    que.append([cur_node.right, parents + [cur_node.val]])
        
        
        k_l = len(k_path)
        print(k_path, k_l)
        
        def dfs_height(node, parents):
            if node.left is None and node.right is None:
                path_l = len(k_path.union(set(parents + [node.val]))) - len(k_path.intersection(set(parents + [node.val])))
                return (path_l, node.val)
            
            if node.left:
                l = dfs_height(node.left, parents + [node.val])
            else:
                l = (float('inf'), 0)
            if node.right:
                r = dfs_height(node.right, parents + [node.val])
            else:
                r = (float('inf'), 0)
            
            if l[0] < r[0]:
                return l
            else:
                return r
        return dfs_height(root, [])[1]
		
#####*** Graph Approach DFS + BFS ****#####
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        
        from collections import defaultdict
        graph = defaultdict(dict)
        
        def dfs(node):
            if not node.left and not node.right:
                graph[node.val]["is_leave"] = True
            else:
                graph[node.val]["is_leave"] = False
            
            if node.left:
                graph[node.val][node.left.val] = 1
                l = dfs(node.left)
                graph[node.left.val][node.val] = 1
            if node.right:
                graph[node.val][node.right.val] = 1
                l = dfs(node.right)
                graph[node.right.val][node.val] = 1
        dfs(root)
        
        
        from collections import deque
        que = deque([k])
        while que:
            try:
                p = que.popleft()
                n = graph.get(p, {})
                # print("Debug ", p, n)
                if n and n["is_leave"]:
                    return p
                elif n:
                    del n["is_leave"]
                for i in n:
                    que.append(i)
                graph.pop(p)
                # print(que, graph)
            except KeyError as ke:
                pass
        
##### ***** Graph - BFS + BFS ****#####
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        
        from collections import defaultdict
        graph = defaultdict(dict)
        from collections import deque
        que = deque([root])
        
        while que:
            n = que.popleft()
            if n.left or n.right:
                if n.left:
                    graph[n.val][n.left.val] = 1
                    graph[n.left.val][n.val] = 1
                    que.append(n.left)
                if n.right:
                    graph[n.val][n.right.val] = 1
                    graph[n.right.val][n.val] = 1
                    que.append(n.right)
                graph[n.val]["is_leave"] = False
            else:
                graph[n.val]["is_leave"] = True

                
        que = deque([k])
        while que:
            try:
                p = que.popleft()
                n = graph[p]
                if n["is_leave"]:
                    return p
                del n["is_leave"]
                que.extend(graph.pop(p).keys())
                
            except KeyError as ke:
                pass
        
        
                    
        
        
      
