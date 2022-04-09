'''

If the depth of a tree is smaller than 5, then this tree can be represented by an array of three-digit integers. For each integer in this array:

The hundreds digit represents the depth d of this node where 1 <= d <= 4.
The tens digit represents the position p of this node in the level it belongs to where 1 <= p <= 8. The position is the same as that in a full binary tree.
The units digit represents the value v of this node where 0 <= v <= 9.
Given an array of ascending three-digit integers nums representing a binary tree with a depth smaller than 5, return the sum of all paths from the root towards the leaves.

It is guaranteed that the given array represents a valid connected binary tree.

'''


def pathSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1. Build the graph
    # create a default dictionary for graph representation
    from collections import defaultdict
    graph = defaultdict(int)
    for num in nums:
        depth, pos, val = num//100, (num//10)%10, num%10
        graph[depth, pos] = val
        
    # 2. Do DFS
    # let's create a stack for DFS
    stack = []
    
    # let's put the root as the starting point of DFS in the stack
    cur_depth, cur_pos = 1,1
    cur_path_sum = graph[cur_depth, cur_pos]
    stack.append((cur_path_sum, (cur_depth, cur_pos)))
    returned_all_paths_sum = 0

    while stack:

        cur_path_sum, (cur_depth, cur_pos) = stack.pop()
        
        # next depth based on the current depth (cur_depth)
        left_depth = right_depth = 1 + cur_depth
        # next positions (left and right) based on the current position (cur_pos)
        left_pos, right_pos = 2*cur_pos-1, 2*cur_pos

        # if it's a leaf node, DFS terminates, we add the 'cur_path_sum' to 'returned_all_paths_sum'
        if (left_depth, left_pos) not in graph and (right_depth, right_pos) not in graph:
            returned_all_paths_sum += cur_path_sum
        else:
            # otherwise the DFS keeps going and we add the next nodes to the stack
            # left node
            if (left_depth, left_pos) in graph:
                left_path_sum = cur_path_sum + graph[left_depth, left_pos]
                stack.append((left_path_sum, (left_depth, left_pos)))
            # right node
            if (right_depth, right_pos) in graph:
                right_path_sum = cur_path_sum + graph[right_depth, right_pos]
                stack.append((right_path_sum, (right_depth, right_pos)))

    return returned_all_paths_sum
  
  
  ------------------------------------------
  
  class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x:x//100) # takes O(1) 
        tree = {}
        
        for num in nums:
         
            d, p, v = num//100, num//10 % 10, num % 10 
            node = TreeNode(v)
            tree[(d, p)] = node
            if d == 1:
                root = node
              
            else:
                parent = tree[(d-1, (p+1)//2)]
               
                if p % 2 == 1:
                    parent.left = node
                else: # p % 2 == 0
                    parent.right = node
          
                    
        res = 0 
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += val
                if node.left:
                    stack.append((node.left, val + node.left.val))
                if node.right:
                    stack.append((node.right, val + node.right.val))
        
        return res
