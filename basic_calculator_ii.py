'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''


class Solution:
    def calculate(self, s: str) -> int:
        num, ope, stack = 0, '+', []
        
        for cnt, i in enumerate(s):
            if i.isnumeric():
                num = num * 10 + int(i)
            if i in '+-*/' or cnt == len(s) - 1:
                if ope == '+':
                    stack.append(num)
                elif ope == '-':
                    stack.append(-num)
                elif ope == '*':
                    j = stack.pop() * num
                    stack.append(j)
                elif ope == '/':
                    j = int(stack.pop() / num)
                    stack.append(j)
            
                ope = i
                num = 0
       
        return sum(stack)
