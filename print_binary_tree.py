'''
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.
'''

class Solution:
    # 28 ms, 92.33%. Time: O(N). Space: O(H)
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_depth(node):
            if not node: return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1
        
        def insert_value(node, lo, hi, depth=0):
            if not node: return
            mid = (lo + hi) // 2
            output[depth][mid] = str(node.val)
            insert_value(node.left, lo, mid, depth + 1)
            insert_value(node.right, mid, hi, depth + 1)

        depth = get_depth(root)
        output = [[""] * (2**depth - 1) for _ in range(depth)]
        
        insert_value(root, 0, 2**depth - 1)
        return output
      
-------------------------------------------

def printTree(self, root: TreeNode) -> List[List[str]]:
        
        def getHeight(node=root):
            return 1+max(getHeight(node.left), getHeight(node.right)) if node else 0
        
        height = getHeight()-1
        columns = 2**(height+1)-1
        res = [[""]*columns for _ in range(height+1)]
        
        queue = deque([(root, (columns-1)//2)])
        r = 0
        
        while queue:
            for _ in range(len(queue)):
                node, c = queue.popleft()
                res[r][c] = str(node.val)
                if node.left:
                    queue.append((node.left, c-2**(height-r-1)))
                if node.right:
                    queue.append((node.right, c+2**(height-r-1)))
            r += 1
             
        return res
-----------------------------------------------------------------------------------------------
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.getHeight(root)
        width = 2**height-1
        
        self.result = [["" for i in range(width)] for j in range(height)]
        
        self.dfs(root,0,0,width-1)
        return self.result
         
    def dfs(self,root,level,left,right):
        if root is None:
            return
        
        mid = (left+right)//2
        self.result[level][mid] = str(root.val)
        self.dfs(root.left,level+1,left,mid-1)
        self.dfs(root.right,level+1,mid+1,right)
        
    
    def getHeight(self,root):
        if root is None:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return max(left,right)+1
