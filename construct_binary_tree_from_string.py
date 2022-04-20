'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

 
 '''


Iterative solution -

Accumulate all digits including - sign until a '(' is encountered. The accumulator here is number string.
On encountering '(', the number is used to create a node and put in the stack. After it, the number is made empty, so further processing can happen
')' has two cases -
a. when the number is being updated and the next item is a ')', here its parent which will be at top of stack has to be linked with it, either as a left or right child
b. when its encountered with the number as '', it means, the top node has all its possible child populated. Thereafter it has to be linked with its parent.
For empty and just root element cases, its handled explicity.
At the end of processing, stack will just have the root element

def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        stack,number=[],''
        for c in s:
            if c in '()':
                if c=='(' and number:
                    stack.append(TreeNode(number))
                    number=''
                elif c==')':
                    if number:
                        node,parent=TreeNode(number),stack[-1]
                        number=''
                    else:
                        node,parent=stack.pop(),stack[-1]
                    if parent.left:
                        parent.right=node
                    else:
                        parent.left=node
            else:
                number+=c
        if number:
            stack=[TreeNode(number)]
        return stack[0]
      
-----------------------------------------------------

In these types of problems where you need to build a finite-state machine, the challenging part is to accout for all the different states and transitions between them. A lot of simple-looking solutions are results of iterative optimizations/simplifications of the initial FSMs. It's very hard to come up with a simple solutions on the first try, and it's very easy to mishandle a transition between states properly.

def str2tree(self, s: str) -> TreeNode:
	if not s: return None
	root = TreeNode()
	stack = [root]
	sign = 1
	num = None

	i = 0
	while i < len(s):
		if s[i] in '()' and num is not None:
			stack[-1].val = sign * num
			sign = 1
			num = None
		if s[i] == '(':
			new_node = TreeNode()
			if stack[-1].left:
				stack[-1].right = new_node
			else:
				stack[-1].left = new_node
			stack.append(new_node)
		elif s[i] == ')':
			stack.pop()
		elif s[i] == '-':
			sign *= -1
		else:
			if not num: num = 0
			val = int(s[i])
			num = num * 10 + val
		i += 1

	if num is not None:
		stack[-1].val = sign * num
	return root
----------------------------------------------------------------------------------

Time: O(N), Space: O(N)

The number strings only exist within two adjacent parenthese. Given two adjacent parentheses at ith and jth positions in string s, s[i+1:j] can only be one of four cases: '(num)', '(num(', ')(', '))', where 'num' is a pure number string within parenthese. Here is my code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        # empty string
        if not s:
            return None
        
        # pure num
        if s[-1].isdigit():
            return TreeNode(int(s))
        
        # put the root in stack
        i = s.find('(')
        stack= [TreeNode(int(s[:i]))]
        
        j, PARS = i + 1, {'(', ')'}
        while j < len(s):
            # four cases: '(num)', '(num(', ')(', '))' need to be handled
            if s[j] in PARS:
                # When [s[i], s[j]] == ['(', '('] or [(', ')'], num string must exists between i, j
                if s[i] == '(':  # or if i + 1 < j
                    stack.append(TreeNode(int(s[i+1:j])))
                
                # When s[j] == ')', the node on the top of stack has been settled.
                if s[j] == ')':
                    node = stack.pop()
                    if stack[-1].left:
                        stack[-1].right = node
                    else:
                        stack[-1].left = node
                i = j
            j += 1
        return stack[0]
----------------------------------------------------------

Here are 2 alternative python solutions. One uses recursion and the other uses a stack. Both are equally fast in the top 95%

Solution 1:
uses recursion and makes use of the nonlocal keyword to synchronize an index pointer across function calls
It could just as easily use self.i or return a tuple of (TreeNode, int)
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        n = len(s)
        i = 0
        def build():
            nonlocal i
            start = i
            while i < n and s[i] not in '()':
                i += 1
            num = s[start:i]
            if num:
                node = TreeNode(int(num))
            else:
                node = None
            if i < n and s[i] == '(':
                i += 1
                node.left = build()
            if i < n and s[i] == '(':
                i += 1
                node.right = build()
            if i == n or s[i] == ')':
                i += 1
                return node
        return build()
Solution 2:
uses a stack to keep track of TreeNodes
uses a for loop to iterate through indexes
has a little more copy-pasta because iteration is less flexible than recursion
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        n = len(s)
        start = 0
        stack = [None]
        for i in range(n):
            if s[i] in '()':
                num = s[start:i]
                start = i+1
                if num and s[i] == '(':
                    stack.append(TreeNode(int(num)))
                elif s[i] == ')':
                    if num:
                        node = TreeNode(int(num))
                    else:
                        node = stack.pop()
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
        num = s[start:]
        if num:
            return TreeNode(int(num))
        return stack[-1]
------------------------------------------------------------------------
handle edge cases and let recursion function do the rest of job.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        # handle empty strings
        if not s:
            return None
        
        # handle pure nums
        if s[-1].isdigit():
            return TreeNode(int(s))
        
        # build the root node
        i = s.find('(')
        root = TreeNode(int(s[:i]))
        
        # divide string into left and right children
        stack, j = 1, i
        while stack > 0:
            j += 1
            if s[j] == '(':
                stack += 1
            elif s[j] == ')':
                stack -= 1
        
        # recursively handle the children nodes
        root.left = self.str2tree(s[i+1:j])
        root.right = self.str2tree(s[j+2:-1])
        
        return root
---------------------------------------------------------------

Approach 1 -- recursive solution

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s: return None # edge case 
        
        mp = {}
        stack = []
        for i, ch in enumerate(s): 
            if ch == "(": stack.append(i)
            elif ch == ")": mp[stack.pop()] = i 
                
        def fn(lo, hi): 
            """Return binary tree from s[lo:hi]."""
            ans = None
            k = lo
            while k < hi: 
                if s[k] == "(": 
                    if not ans: 
                        ans = TreeNode(int(s[lo:k]))
                        ans.left = fn(k+1, mp[k])
                    else: ans.right = fn(k+1, mp[k])
                    k = mp[k]
                k += 1
            if not ans: ans = TreeNode(int(s[lo:hi]))
            return ans 
        
        return fn(0, len(s))
Approach 2 -- iterative solution

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s: return None # edge case 
        stack = []
        val = ""
        for ch in s: 
            if ch == "(": 
                if val: 
                    node = TreeNode(int(val))
                    stack.append(node)
                    val = ""
            elif ch == ")": 
                if val: 
                    node = TreeNode(int(val))
                    val = ""
                else: node = stack.pop()
                if stack[-1].left is None: stack[-1].left = node 
                else: stack[-1].right = node
            else: val += ch
        return stack[-1] if stack else TreeNode(int(val))
      
      
      
      
      
