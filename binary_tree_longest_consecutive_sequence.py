
'''

Given the root of a binary tree, return the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).

 
 '''


def longestConsecutive(self, root: TreeNode) -> int:
        max_ = 1
        def dfs(node=root):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            left = left+1 if (node.left and node.left.val == node.val+1) else 1
            right = right+1 if (node.right and node.right.val == node.val+1) else 1
            nonlocal max_
            max_ = max(left, right, max_)
            return max(left, right)
        dfs()
        return max_
      
----------------------------------------------------------

Algo
Traverse the tree dfs and keep track of longest consecutive sequence.

Implementation

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0 # edge case 
        
        ans = 0
        stack = [(root, 1)]
        while stack: 
            node, val = stack.pop()
            ans = max(ans, val)
            if node.left: stack.append((node.left, val+1 if node.left.val == node.val+1 else 1))
            if node.right: stack.append((node.right, val+1 if node.right.val == node.val+1 else 1))
        return ans 
Analysis
Time complexity O(N)
Space complexity O(N)
------------------------------------------------------

A good thing for this solution is if you uncomment the print(output), you can see your traverse route, and you can see which sequence brings you the longest solution(Thats why I use Backtracking, and I believe there will be some followup questions like 'return the longest sequence'), enjoy!

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        cur = root
        output = []
        ans = 1
        
        def bt(n=root, path=[]):
            nonlocal ans
            
            if path and path[-1] != n.val - 1:
                output.append(path[:])  
                ans = max(ans, len(path))
                bt(n, [])
            
            else:
                path.append(n.val)
                
                if n.left:
                    bt(n.left, path)

                if n.right:
                    bt(n.right, path)
                
                if not n.left and not n.right:
                    output.append(path[:])
                    ans = max(ans, len(path))
                
                path.pop()

                
        
        bt()
        # display results
        # print(output)          
        return ans
------------------------------------------

class Solution:
    
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_len = 1
        self.helper(root, float('-inf'), 1)
        return self.max_len
    
    def helper(self, node, prev, cum):
        if node:
            if node.val == prev + 1:
                self.max_len = max(self.max_len, cum+1)
                self.helper(node.left, node.val, cum+1)
                self.helper(node.right, node.val, cum+1)
            else:
                self.helper(node.left, node.val, 1)
                self.helper(node.right, node.val, 1)
------------------------------------------

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        result = 0
        stack = [(root, [], 1)]
        while stack:
            node, path, seq_count = stack.pop()
            if node is None:
                continue
            if path and node.val-1 == path[-1]:
                seq_count += 1
            else:
                seq_count = 1
            stack.append([node.right, path + [node.val], seq_count])
            stack.append([node.left, path + [node.val], seq_count])
            result = max(result, seq_count)
        return result
      
                
      
