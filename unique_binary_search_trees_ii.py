'''
Given an integer n, return all the structurally 
unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
'''


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def rec(start, end):
		
            if start > end:
                return [None]
				
            if start == end:
                return [TreeNode(start)]
            ret_list = []
			
            for i in range(start, end+1):
                left = rec(start, i-1)
                right = rec(i+1, end)
                for pair in product(left, right):
                    ret_list.append(TreeNode(i, pair[0], pair[1]))
        
            return ret_list
        
        res = rec(1,n)
        return res
