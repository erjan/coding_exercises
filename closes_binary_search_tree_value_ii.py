'''
Given the root of a binary search tree, a target value, and an integer k, return the 
k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target
'''


class Solution(object):

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def dfs(root, target, heap):
            if root is None:
                return

            dfs(root.left, target, heap)
            heapq.heappush(heap, (abs(root.val - target), root.val))
            dfs(root.right, target, heap)
        
        heap = []
        dfs(root, target, heap)
      
        output = []
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])
        return output
      
      
-------------------------------------------------------------------------------------------
I didn't get a O(klogn) solution until I drew a figure today. If you didn't get a O(klogn) solution yet, try drawing a bst on paper and track the change of the two stacks manually. You will find it. (I drew a bst with 15 nodes, 1 to 15, and target = 6.5, search for nearest 8 nodes)

def closestKValues(self, root, target, k):
    """
    :type root: TreeNode
    :type target: float
    :type k: int
    :rtype: List[int]
    """
    res = []
    smallers, largers = [], []  # two stacks tracking smaller and larger nodes
    while root:
        if root.val > target:
            largers.append(root)
            root = root.left
        else:
            smallers.append(root)
            root = root.right
    for _ in range(k):
        if smallers and (not largers or largers and target - smallers[-1].val <= largers[-1].val - target):
            res.append(self._predecessor(smallers))
        else:
            res.append(self._successor(largers))
    return res

def _predecessor(self, smallers):
    curr = smallers.pop()
    node = curr.left
    while node:
        smallers.append(node)
        node = node.right
    return curr.val
    
def _successor(self, largers):
    curr = largers.pop()
    node = curr.right
    while node:
        largers.append(node)
        node = node.left
    return curr.val
  
  
------------------------------------------------------------------------
Do an inorder traversing to a BST, we will encounter values from small to large, like SSSSSSSTLLLLLLL, where T is the closest num to the target, and S is smaller than T, and the L is larger than T.

We know the result should be some ...SSSTLLL... with the length of k. If we move a queue with a max length of k and slide it from left to right, the sliding can be stopped and the answer was found when it meets an L and (L - target) > (target - S), where S is the smallest number on the top of the queue. Here is my code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        queue = collections.deque()
        def dfs(node):
            if node:
                dfs(node.left)
                if len(queue) == k:
                    if node.val - target > target - queue[0]:
                        return
                    queue.popleft()
                queue.append(node.val)
                dfs(node.right)
        dfs(root)
        return list(queue)
      
      
-----------------------------------------------------------------------------------------------
Use helper function to find predecessor and successor. Find the closest value and expand to the two sides.

from collections import deque
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def get_successor(cur_val):
            suc = None
            node = root
            while node:
                if cur_val < node.val:
                    suc = node
                    node = node.left
                else:
                    node = node.right
            return suc

        def get_predecessor(cur_val):
            pre = None
            stack = []
            node = root
            while node and node.val != cur_val:
                stack.append(node)
                if node.val > cur_val:
                    node = node.left
                else:
                    node = node.right
            if node.left: # if node has left child, find the rightmost in left subtree
                tmp = node.left
                while tmp.right:
                    tmp = tmp.right
                pre = tmp
            elif stack and node == stack[-1].right: # if node is the right child
                pre = stack[-1]
            else:
                while stack and node == stack[-1].left: # if node is left child, retrieve up
                    node = stack.pop()
                if stack:
                    pre = stack[-1]
            return pre

        if k == 0:
            return []

        node = root
        min_diff = float("inf")
        minimum = None

        while node:
            if abs(node.val - target) < min_diff:
                min_diff = abs(node.val - target)
                minimum = node.val
            if node.val > target:
                node = node.left
            elif node.val < target:
                node = node.right
            else:
                break

        k -= 1
        ans = deque([minimum])
        while k > 0:
            left = get_predecessor(ans[0])
            right = get_successor(ans[-1])
            if not left:
                ans.append(right.val)
            elif not right:
                ans.appendleft(left.val)
            else:
                if abs(left.val - target) < abs(right.val - target):
                    ans.appendleft(left.val)
                else:
                    ans.append(right.val)
            k -= 1
        return list(ans)
      
      
-------------------------------------------------------------------------------------------
Time Complexity - O(N)
Breakdown - O(N) for Inorder traversal, O(logN) for finding closest index (binary search), O(N) worst case for 2-Pointers

Space Complexity - O(N)
Breakdown - O(N) for inorder list + O(H) (height of tree) for recursive stack, In the worst case our result list has N items O(N)

Don't forget to upvote, if you find it useful!! :)
Happy Coding!!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        
        inorder = []
        
        def traverse(node):
            nonlocal inorder
            if not node:
                return None
            
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)
        
        traverse(root)
        s, e = 0, len(inorder) - 1
        while s <= e:                             # search for target and get closest points to the target
            m = s+(e-s)//2
            if inorder[m] > target:
                e = m-1
            elif inorder[m] < target:
                s = m+1
            else:
                s = m
                break
        
        res = []
		
		# initialize two pointers, from the start and start - 1 and append values in res which is closer to target
		
        e = s
        s = s-1
        while (s >= 0 or e < len(inorder)) and len(res) < k:
            if s >= 0 and e < len(inorder):
                if abs(target - inorder[s]) < abs(target - inorder[e]):
                    res.append(inorder[s])
                    s -= 1
                else:
                    res.append(inorder[e])
                    e += 1
            elif s >= 0:
                res.append(inorder[s])
                s -= 1
            else:
                res.append(inorder[e])
                e += 1
        
        return res
-----------------------------------------------------------------------------------------------
use a min heap with the index being the distance: abs(nums[a] - target)
do an inorder traversal, add tuples to the result with (distance, number)
heapify the result and pop k elements off
overall runtime 2*o(n) + o(k)
import heapq
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        nums = self.dfs(root, target)
        heapq.heapify(nums) 
        result = []
        for _ in range(k):
            elem = heapq.heappop(nums)
            result.append(elem[1])
        return result
        
    def dfs(self, root, target):
        if root is None:
            return []
        return self.dfs(root.left, target) + [(abs(root.val - target), root.val)] + self.dfs(root.right, target)
      
      
-----------------------------------------------------------------
def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        distances = []  # (distance, value)
        
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if node:
                distances.append((abs(target - node.val), node.val))

                q.append(node.left)
                q.append(node.right)
            
        distances.sort()

        output = []
        for distance, value in distances[:k]:
            output.append(value)
        return output
