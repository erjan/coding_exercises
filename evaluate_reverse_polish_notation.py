'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            token = tokens[i]

            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                if token == '+':
                    top = stack.pop()
                    top2 = stack.pop()

                    res = top + top2
                    stack.append(res)
                    
                elif token == '-':
                    top = stack.pop()
                    top2 = stack.pop()

                    res = top2 - top
                    stack.append(res)

                elif token == '*':

                    top = stack.pop()  
                    top2 = stack.pop()

                    res = top * top2

                    stack.append(res)

                elif token == '/':

                    top = stack.pop()
                    top2 = stack.pop()
                    stack.append(int(top2/top))                   

        return stack[-1]
