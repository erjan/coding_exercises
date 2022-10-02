'''
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even 
numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.
'''

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        while(label != 1):
            par1 = label//2
            x = int(log(par1, 2))
            diff = par1 - 2**x
            label = 2**(x+1)-1 - diff
            ans.append(label)
        return ans[::-1]
