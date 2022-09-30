'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

'''


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root,val):
            if root:
                k = solve(root.left, max(val,root.val)) + solve(root.right, max(val,root.val))
                if root.val >= val:
                    k+=1
                return k
            return 0
        return solve(root,root.val)
      
---------------------------------------------------------------------------------------------------
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
	
		ans = 0
        q = deque()
		
        q.append((root,-inf))
        '''perform bfs  with track of maxval till perant node'''	

        while q:
            node,maxval = q.popleft()
			 '''if curr node has max or eqvalue till current max'''
            if node.val >= maxval:  
                ans += 1
				
            if node.left:    #new max update
                q.append((node.left,max(maxval,node.val)))
            
            if node.right:
                q.append((node.right,max(maxval,node.val)))
                
        return ans
      
-------------------------------------------------------------------------
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
			#if there is no node then there is no good nodes so return 0
            if not node:
                return 0
			
			#if current node is good then 1 otherwise 0
            good = 1 if node.val>=max_so_far else 0
			
			#Checking if current node is greater than max_so_far , if yes then update max_so_far to current node's value
            max_so_far = max(max_so_far, node.val)
            
			#returning total of current good , no. of good nodes in left and right
            return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
        
        return dfs(root, -int(1e5))#Since constraints are [-10^4, 10^4] so we take -10^5 as maximum
