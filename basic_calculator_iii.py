'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''


It is much easier to implement the solution if you build the BNF grammar.

inspired by https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/discuss/864596/Python-Standard-parser-implementation

class Solution:
    def calculate(self, s: str) -> int:
        """
        s := expr 
        expr = term  | term [+ -] term
        term = factor | factor [* /] factor 
        factor = digit | '(' expr ')'
        digit = [0..9]
        """
        def parse_factor(dq):
            if dq[0].isdigit():
                curr = 0
                while dq and dq[0].isdigit():
                    curr = curr* 10 + int(dq[0])
                    dq.popleft()
                return curr
            else:
                dq.popleft()
                tmp = parse_expr(dq)
                dq.popleft()
                return tmp
            
        def parse_term(dq):
            lhs = parse_factor(dq)
            while dq and dq[0] in ['*', '/']:
                op = dq.popleft()
                rhs = parse_factor(dq)
                lhs = lhs * rhs if op == '*' else int(lhs/rhs) # for this case "(0-3)/4"
            return lhs
        
        def parse_expr(dq):
            lhs = parse_term(dq)
            while dq and dq[0] in ['+', '-']:
                op = dq.popleft()
                rhs = parse_term(dq)
                lhs = lhs + rhs if op == '+' else lhs - rhs
            return lhs
    
        dq = deque(list(s))
        return parse_expr(dq)
      
----------------------------------------------------------------------------------------------
class Solution:
    def calculate(self, s):
		# this is to split the input into tokens
        s = filter(None, re.split(r'([+\-*/()\$])', (s + '$').replace(' ', '')))
        return self.do_calculate(s)
    
    def do_calculate(self, s):
        stack = []
        num, sign = 0, '+'
        
        def calculate_top():
            if sign == '+':
                stack.append(num)
            if sign == '-':
                stack.append(-num)
            if sign == '*':
                stack[-1] *= num
            if sign == '/':
                stack[-1] = int(stack[-1] / num)
                
        while c := next(s):
            if c.isdigit():
                num = int(c)
            elif c == '(':
                num = self.do_calculate(s)
            elif c in ')$':
                calculate_top()
                return sum(stack)
            elif c in '+-*/':
                calculate_top()
                sign = c
                
------------------------------------------------------------------
class Solution(object):
    def getSubExpr(self, s):
        left = 1
        x = []
        while left != 0:
            x.append(next(s))
            if x[-1] == '(':
                left += 1
            elif x[-1] == ')':
                left -= 1
        # print(x[:-1])
        return ''.join(x[:-1])
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = iter(re.findall('\d+|\S', s))
        operand, sign = 0, 1
        total = 0
        for token in s:
            # print(token, operand, sign, total)
            if token in '+-':
                total += sign * operand
                sign = [1, -1][token == '-']
            elif token in '/*':
                n = next(s)
                n = self.calculate(self.getSubExpr(s)) if n == '(' else int(n)
                operand = operand*n if token == '*' else operand/n
            else:
                operand = self.calculate(self.getSubExpr(s)) if token == '(' else int(token)
        return total + sign * operand
      
------------------------------------------------------------------
"""
This is some kind of combination of 2 solutions of these tasks:

https://leetcode.com/problems/basic-calculator-ii/
https://leetcode.com/problems/decode-string/
"""
class Solution:
    def calculate(self, s: str) -> int:
        operators = {'+', '-', '*', '/'}
        current_number = 0
        operator = '+'
        stack = []
        res = 0
        for i, c in enumerate(s):
            if c.isnumeric():
                current_number = current_number * 10 + int(c)
            if c == '(':
                stack.append(operator)
                operator = '+'
            elif c == ')':
                self.append_result_to_stack(stack, current_number, operator)
                current_number = 0
                # Calculating expression between parentheses
                while stack and stack[-1] not in operators:
                    current_number += stack.pop()
                operator = stack.pop()
            if c in operators or i == len(s) - 1:
                self.append_result_to_stack(stack, current_number, operator)
                operator = c
                current_number = 0
        while stack:
            res += stack.pop()
        return res

    def append_result_to_stack(self, stack, current_number, operator):
        if operator == "+":
            stack.append(current_number)
        elif operator == "-":
            stack.append(-current_number)
        elif operator == "*":
            stack.append(stack.pop() * current_number)
        else:
            div_result = stack.pop() / current_number
            if div_result < 0:
                stack.append(math.ceil(div_result))
            else:
                stack.append(math.floor(div_result))
                
                
-----------------------------------------------
class Solution:
    
    def calculate(self, s: str) -> int:
        
        # Strip and replace all the spaces
        s = s.strip().replace(" ","")
        
        # Evaluate
        def update(stack: List, curr: str, operator: str):
            if curr:
                if operator == "-":
                    stack.append(-1 * int(curr))
                elif operator == "*":
                    n = stack.pop()
                    m = int(curr)
                    stack.append(n*m)
                elif operator == "/":
                    n = stack.pop()
                    m = int(curr)
                    stack.append(int(n/m))
                else:
                    stack.append(int(curr))
            return
        
        # Function to evaluate current
        def evaluate(s: str, idx: int = 0):
            
            stack = []
            operator = ""
            curr = ""
            
            while idx < len(s):
               
                # next char
                char = s[idx]
                
                # End of current expression
                if char == ")":
                    break
                
                # If new expression, evaluate it first
                elif char == "(":
                    v, idx = evaluate(s,idx+1)
                    update(stack, str(v), operator)
                
                # If digit keep on appending
                elif char.isdigit():
                    curr = curr + char
                    
                else: # update stack
                    update(stack, curr, operator)
                    operator = char
                    curr = ""
                
                # increment index
                idx = idx + 1
                
            # Update stack for last operation
            update(stack, curr, operator)
            
            return (sum(stack), idx)
        
        return evaluate(s)[0] 
------------------------------------------------------------------
Python3 has a built-in ast standard library which you can parse it into an Abstract-Syntax-Tree and walk through the tree and evaluate.

It might not be the fastest, but it is properly the correct way of solving this. It works for any expression syntax too.

import ast
class Solution:
    def ast_recurse(self, node):
        if (isinstance(node, ast.Num)):
            return node.n
        
        if (isinstance(node, ast.UnaryOp)):  # case: (-1)
            if (isinstance(node.op, ast.USub)):
                return -1 * self.ast_recurse(node.operand)
        
        if (isinstance(node, ast.BinOp)):
            left = self.ast_recurse(node.left)      # DFS walk left
            right =self.ast_recurse(node.right)   # DFS walk right

            if (isinstance(node.op, ast.Add)):
                return left + right
            elif (isinstance(node.op, ast.Sub)):
                return left - right
            elif (isinstance(node.op, ast.Mult)):
                return left * right
            elif (isinstance(node.op, ast.Div)):
                return left // right

    def search_expr(self, ast_node):
        returns = []
		# converts all the AST expressions into a list of children
        for child in ast.iter_child_nodes(ast_node):
            if isinstance(child, ast.Expr):
                return child
            returns.append(self.search_expr(child))
        for ret in returns:
            if isinstance(ret, ast.Expr):
                return ret
        return None

    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0

        s = "".join(s.split())  # removes all the white spaces
        results = []

        # use built-in AST to builds the AST
        tree = ast.parse(s)
        expr = self.search_expr(tree)   # finds all the expression
        if expr is not None:
            for child in ast.iter_child_nodes(expr):
                results.append(self.ast_recurse(child))

        return sum(results)
      
                
      
