'''
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.
'''


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> list:
        self.res = 0  
        
        def dfs(node) -> list:
            if not node: return []
            if not node.left and not node.right: return [1]

            left_list = dfs(node.left)
            right_list = dfs(node.right)
            self.res += sum(l+r <= distance for l in left_list for r in right_list)
            return [1+item for item in left_list+right_list]
        
        dfs(root)
        return self.res 
        
------------------------------------------------------------------------------------------------
class Solution:
	def countPairs(self, root: TreeNode, distance: int) -> int:

		res = [0] 
		def dfs(node):
			if not node:return []
			if not node.left and not node.right:return [0]
			left,right = dfs(node.left),dfs(node.right)
			m,n = len(left),len(right)
			for i in range(m):
				left[i]+=1
			for j in range(n):
				right[j]+=1

			for l in left:
				for r in right:
					if l + r <= distance:
						res[0] += 1
			return left+right
		dfs(root)
		return res[0]
