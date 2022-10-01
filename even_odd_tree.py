'''
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
'''

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q= [root]
        level = 0
        while q:
            if level%2 ==0 :
                if q[0].val%2==0: return False
                for i in range(1, len(q)):
                    if q[i].val%2==0 or q[i-1].val>=q[i].val: return False
            else:
                if q[0].val%2!=0: return False
                for i in range(1, len(q)):
                    if q[i].val%2!=0 or q[i-1].val<=q[i].val: return False
            nodes =[]
            while q:
                i = q.pop(0)
                if i.left: nodes.append(i.left)
                if i.right: nodes.append(i.right)
            q = nodes
            level+=1
        return True
