'''
Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression.

Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. For example, the postfix tokens of the expression 4*(5-(7+2)) are represented in the array postfix = ["4","5","7","2","+","-","*"].

The class Node is an interface you should use to implement the binary expression tree. The returned tree will be tested using the evaluate function, which is supposed to evaluate the tree's value. You should not remove the Node class; however, you can modify it as you wish, and you can define other classes to implement it if needed.

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with two children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

It's guaranteed that no subtree will yield a value that exceeds 109 in absolute value, and all the operations are valid (i.e., no division by zero).

Follow up: Could you design the expression tree such that it is more modular? For example, is your design able to support additional operators without making changes to your existing evaluate implementation?
'''

NOTE: It's not so difficult as it looks like. Once you understand what the question is asking, it's fairly easy.

Explanation
evaluate is basically a DFS process, all digits are at leaf nodes; otherwise we will calculate the result recursively
Building tree based on postfix list can be easy with help of stack
Implementation
import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        elif self.val == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == '-':
            return self.left.evaluate() - self.right.evaluate()
        else:    
            return self.left.evaluate() // self.right.evaluate()
            
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        cur, stack = None, []
        for c in postfix:
            cur = TreeNode(c)
            if not c.isdigit():
                cur.right = stack.pop()
                cur.left = stack.pop()
            stack.append(cur)
        return cur           
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
----------------------------------------------------------------------------

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class NumericNode(Node):
    def __init__(self, val):
        self.val = val
    def evaluate(self):
        return self.val
    
class OperatorNode(Node):
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left 
        self.right = right
    
    def evaluate(self):
        leftVal = self.left.evaluate()
        rightVal = self.right.evaluate()
        return self.operators[self.operator](leftVal, rightVal)  


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for char in postfix:
            if char.isdigit():
                stack.append(NumericNode(int(char)))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(OperatorNode(char, left, right))
        return stack.pop()
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
----------------------------------------------------------------------------------------

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  @abstractmethod
  # define your fields here
  def evaluate(self) -> int:
    pass
    

class Operand(Node):
  def __init__(self, val):
    super().__init__(val)
    
  def evaluate(self):
    return int(self.val)
  
class PlusOperator(Node):
  def __init__(self):
    super().__init__('+')
  
  def evaluate(self):
    return int(self.left.evaluate() + self.right.evaluate())
    
class MinusOperator(Node):
  def __init__(self):
    super().__init__('-')
    
  def evaluate(self):
    return int(self.left.evaluate() - self.right.evaluate())

class MultiplyOperator(Node):
  def __init__(self):
    super().__init__('*')
    
  def evaluate(self):
    return int(self.left.evaluate() * self.right.evaluate())
    
class DivideOperator(Node):
  def __init__(self):
    super().__init__('/')
    
  def evaluate(self):
    return int(self.left.evaluate() / self.right.evaluate())

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
  def buildTree(self, postfix: List[str]) -> 'Node':
    stack = []
    for char in postfix:
      if char.isdigit():
        stack.append(Operand(char))
      else:
        rhs = stack.pop()
        lhs = stack.pop()
        if char == '+':
          node = PlusOperator()
        elif char == '-':
          node = MinusOperator()
        elif char == '*':
          node = MultiplyOperator()
        elif char == '/':
          node = DivideOperator()
        node.left = lhs
        node.right = rhs
        stack.append(node)
    return node
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

--------------------------------------------------------------------------------------------------------
import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class OperatorNode(Node):
    
    def __init__(self, val):
        super().__init__(val)
    
    def evaluate(self):
        if self.val == "+":
            return self.left.evaluate() + self.right.evaluate()
        if self.val == "-":
            return self.left.evaluate() - self.right.evaluate()
        if self.val == "*":
            return self.left.evaluate() * self.right.evaluate()
        if self.val == "/":
            return self.left.evaluate() // self.right.evaluate()

class NumericNode(Node):
    
    def __init__(self, val):
        super().__init__(val)
    
    def evaluate(self):
        return int(self.val)
        
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        n = len(postfix)
        index = n - 1
        
        def build():
            nonlocal index
            if index < 0:
                return None
            
            val = postfix[index]
            index -= 1
            if val.isnumeric():
                return NumericNode(val)
            else:
                operator_node = OperatorNode(val)
                operator_node.right = build()
                operator_node.left = build()
                return operator_node
        
        return build()
                
                
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""



-----------------------------------------------------------------------------
import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

    
class TreeNode(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)
        elif self.val == "+":
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == "-":
            return self.left.evaluate() - self.right.evaluate()
        elif self.val == "*":
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == "/":
            return self.left.evaluate() // self.right.evaluate()
        else:
            pass

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for token in postfix:
            t = TreeNode(token)
            if not token.isdigit():
                t.right = stack.pop()
                t.left = stack.pop()
            stack.append(t)
        return stack.pop()
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

------------------------------------------------------------------------------
import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node): 
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
    
    def evaluate(self): 
        if self.val not in "+-*/": return int(self.val)
        left = self.left.evaluate()
        right = self.right.evaluate()
        if self.val == "+": return left + right
        elif self.val == "-": return left - right
        elif self.val == "*": return left * right 
        return left // right

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for x in postfix: 
            node = TreeNode(x)
            if x in "+-*/": 
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        return stack.pop()
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""


