Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

def verifyPreorder(self, preorder):
    stack = []
    lower = -1 << 31
    for x in preorder:
        if x < lower:
            return False
        while stack and x > stack[-1]:
            lower = stack.pop()
        stack.append(x)
    return True


# 59 / 59 test cases passed.
# Status: Accepted
# Runtime: 100 ms
# 95.31%
Then we realize that the preorder array can be reused as the stack thus achieve O(1) extra space, since the scanned items of preorder array is always more than or equal to the length of the stack.

def verifyPreorder(self, preorder):
    # stack = preorder[:i], reuse preorder as stack
    lower = -1 << 31
    i = 0
    for x in preorder:
        if x < lower:
            return False
        while i > 0 and x > preorder[i - 1]:
            lower = preorder[i - 1]
            i -= 1
        preorder[i] = x
        i += 1
    return True
  
  
------------------------------------------------------------------------------
Using stack for storing the current node as a check point for the next element.
Once the current is larger than the last element in the stack, we know we should take it as the right node.
The last element poping out from the stack will be also a checking point. We will use it to validate the BST property of the current element/node.

time complexity: O(n)
space complexity: O(n)

chk, stack = None, []
for n in preorder:
    while stack and n > stack[-1]:
        chk = stack.pop()
    if chk != None and n < chk:
        return False
    stack.append(n)
return True
Example 1: [5, 2, 6, 1, 3]
n = 5, stack = [5]
no checking point

Tree: 5
n = 2, 2 < 5, stack = [5, 2]
no checking point

Tree:   5
       /
	  2
n = 6, 6 > 2, 6 > 5, stack = [6]
checking point = 5

Tree:   5
       / \
	  2   6
n = 1, 1 < 5, it's NOT a valid BST...

Tree:   5
       / \
	  2   6
         /
		1
Example 2: [5, 2, 1, 3, 6]
n = 5, stack = [5]
no checking point

Tree: 5
n = 2, 2 < 5, stack = [5, 2]
no checking point, and we are on the left branch

Tree:   5
       /
	  2
n = 1, stack = [5, 2, 1]
no checking point, and we are on the left branch

Tree:   5
       / 
	  2 
	 /
    1
n = 3, 3 > 1, 3 > 2. checking point = 2
we are on the right branch
stack = [5, 3]

Tree:   5
       /
	  2
     / \
    1   3
n = 6, 6 > 3, 6 > 5. checking point = 5
we are on the right branch
stack = [6]
We are at the end of the list. It's a valid BST!

Tree:   5
       / \
	  2   6
     / \
    1   3
      
--------------------------------------------------------------------------
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        ## RC ##
        ## APPROACH : MONOTONOUS DECREASING STACK ##
        ## Similar to Leetcode: 94 Binary tree inorder traversal ##
        ## Similar to leetcode : 98 Validate Binary Search Tree #
        
        ## LOGIC ##
        ## 1. First we push all elements less than TOS (left childs)
        ## 2. If we encounter any big number than TOS, (indicates start of right childs), we pop all less elements and update lower value. In all such cases x should be more than its parent(lower) else we return False.
        ## 3. And append the big number to stack (right child) then (go for its left child & repeat process)
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        stack = []
        lower = -1 << 31
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True
        
        # Then we realize that the preorder array can be reused as the stack thus achieve O(1) extra space, since the scanned items of preorder array is always more than or equal to the length of the stack.
        
        ## STACK TRACE ##
        ## [5,2,1,3,6] ##
        # [5, 2, 1, 3, 6]
        # [5, 2, 1, 3, 6]
        # [5, 2, 1, 3, 6]
        # [5, 3, 1, 3, 6]
        # [6, 3, 1, 3, 6]

		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

        lower = -1 << 31
        i = 0
        for x in preorder:
            if x < lower:
                return False
            while i > 0 and x > preorder[i - 1]:
                lower = preorder[i - 1]
                i -= 1
            preorder[i] = x
            i += 1
            # print(preorder)
        return True
------------------------------------------------------------
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lower = -float('inf')
        stack = []
        
        for curr in preorder:
            if curr <= lower: # break BST rule
                return False
            if not stack or curr < stack[-1]:
                stack.append(curr)
                continue
            while stack and curr >= stack[-1]:
                lower = stack.pop()
            stack.append(curr)
            
        return True
-----------------------------------
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lo = -inf
        stack = []
        
        for val in preorder:
            if val <= lo:
                return False
            
            while stack and stack[-1] < val:
                lo = stack.pop()
            
            stack.append(val)
        
        return True
      
      
      
