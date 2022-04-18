'''
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with 2 children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression that it represents is (A o B), where A is the expression the left subtree represents and B is the expression the right subtree represents.

You are given a string s, an infix expression containing operands, the operators described above, and parentheses '(' and ')'.

Return any valid binary expression tree, which its in-order traversal reproduces s after omitting the parenthesis from it (see examples below).

Please note that order of operations applies in s. That is, expressions in parentheses are evaluated first, and multiplication and division happen before addition and subtraction.

Operands must also appear in the same order in both s and the in-order traversal of the tree.
'''



Base case:

If it is just a number: return a node
If it is nothing, return None(might be optional?)
Loop through the expression once to find all the + and -(ignore anything between parentheses)
Loop through the expression once to find all the * and /(ignore anything between parentheses)
If we find nothing, everything is in parenthesis, so reduce a layer and continue.

Comment on any questions

# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        if s.isnumeric():
            return Node(s)
        if len(s) == 0:
            return None


        plus = s.find('+')
        paren = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                paren +=1
            elif s[i] == '(':
                paren -=1
            if paren > 0:
                continue
            if s[i] == '+':
                return Node('+', self.expTree(s[:i]), self.expTree(s[i+1:]))
            if s[i] == '-':
                return Node('-', self.expTree(s[:i]), self.expTree(s[i+1:]))
            
        paren = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                paren +=1
            elif s[i] == '(':
                paren -=1
            if paren > 0:
                continue
            if s[i] == '*':
                return Node('*', self.expTree(s[:i]), self.expTree(s[i+1:]))
            if s[i] == '/':
                return Node('/', self.expTree(s[:i]), self.expTree(s[i+1:]))
            
                
        if s[0] == '(' and s[-1] == ')':
            return self.expTree(s[1:-1])
            
            
--------------------------------------------------------------------------------------------
class Solution:
    def expTree(self, s: str) -> 'Node':
        operandStack = []
        operatorStack = []
        # CONSIDERATION: HIGHER THE OPERATION HIGHER IS THE PRECEDENCE
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
        prevScore = 0
        
        def buildSubTree():
            right = operandStack.pop()
            left = operandStack.pop()
            operandStack.append(Node(operatorStack.pop(), left, right))
        
        for ch in s:
            if ch == ')':
                while operatorStack[-1] != '(':
                    buildSubTree()
                
                # POP OUT '('
                operatorStack.pop()
                prevScore = precedence[operatorStack[-1]] if operatorStack else 0
                    
            elif ch in precedence:
                if ch == '(':
                    prevScore = 0
                    
                elif prevScore < precedence[ch]:
                    prevScore = precedence[ch]
                    
                else:
                    while operatorStack and operatorStack[-1] != '(' and prevScore >= precedence[ch]:
                        buildSubTree()
                        
                        if operatorStack:
                            prevScore = precedence[operatorStack[-1]]
                    
                    prevScore = precedence[ch]
                operatorStack.append(ch)
                
            else:
                operandStack.append(Node(ch))
        
        while operatorStack and operatorStack[-1] != '(':
            buildSubTree()
        
        return operandStack[0]
        
        
--------------------------------------------------------------------------
class Solution:
    def expTree(self, s: str) -> 'Node':
        
        if len(s) <= 1:
            return None if not s else Node(s[0])
    
        n = len(s)
        
        # find the last '-' or '+' sign, which has the lowest priority
        sign = None
        i = n - 1
        sign_pos = n
        while i > 0:
            if not s[i].isdigit():
                if s[i] == ')':
                    # traverse to the matching '('
                    j = i-1
                    nbracket = 1
                    while j >= 0:
                        if s[j] == ')':
                            nbracket += 1
                        elif s[j] == '(':
                            nbracket -= 1
                        if nbracket == 0:
                            break
                        j -= 1
                    i = j - 1
                    continue
                elif not sign:
                    sign = s[i]
                    sign_pos = i
                # the right-most + or - (if any) will be the condition to stop and do a recursive call
                elif s[i] in ('+' ,'-') and sign in ('*', '/'):
                    sign = s[i]
                    sign_pos = i
                    break
            i -= 1
        
        # bracket case
        if not sign:
            return self.expTree(s[1:-1])
        
        node = Node(sign)
        node.left = self.expTree(s[:sign_pos])
        node.right = self.expTree(s[sign_pos+1:])

        return node
        
