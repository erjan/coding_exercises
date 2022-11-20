'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''

class Solution:
    def calculate(self, s: str) -> int:

        cur = 0
        res = 0
        sign = 1

        stack = []

        for ch in s:

            if ch.isdigit():
                
                cur = cur*10 + int(ch)
               

            elif ch == ' ':
                continue 

            elif ch in ['+', '-']:
                res += sign*cur
                sign = 1 if ch == '+' else -1
                cur = 0
            
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0

            
            elif ch == ')':
                res += sign * cur
                res *= stack.pop()
                res += stack.pop()

                cur = 0
        

        return res + sign*cur
