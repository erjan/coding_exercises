'''
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.
'''

import re

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        # filter removes empty strings
        tokens = filter(lambda x: x != "", re.split(r"([(),&!|ft])", expression))
    
        def compute(tokens):
            stack = []
            oper = None

            def process_stack(vals):
                if oper == "&":
                    return "t" if all([e == "t" for e in vals]) else "f"
                elif oper == "|":
                    return "t" if any([e == "t" for e in vals]) else "f"
                elif oper == "!":
                    return "t" if vals[0] == "f" else "f"

            while c := next(tokens, None):
                if c in "&|!":
                    oper = c
                elif c == "(":
                    vals = compute(tokens)
                    stack.append(process_stack(vals))
                elif c == ")":
                    return stack
                elif c in "ft":
                    stack.append(c)
            return stack[0]
        
        return True if compute(tokens) == "t" else False

----------------------------------------------------------------------------------------------------------------
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        string = ""
        e = [] #stack for expressions
        for i in expression:
            if i == "!":
                string += " not "
                e.append("not") #this should be never added to the string, since there would be no commas in !()
            elif i=="&":
                e.append("and")
            elif i=="|":
                e.append("or")
            elif i=="(":
                string += i
            elif i==")":
                string += i
                e.pop()
            elif i=="t":
                string += "True"
            elif i=="f":
                string += "False"
            elif i==",":
                string += (" "+e[-1]+" ")
        return eval(string)
      
--------------------------------------------------------------------------------------------------------------------------------- 

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
		# eval function would treat f and t as variables. Assign False and True to them.
        f = False
        t = True
        
		# convert | into an OR function
        def or_op(*args):
            return reduce(lambda x,y:x or y, args)
        
		# convert & into an AND function
        def and_op(*args):
            return reduce(lambda x,y : x and y, args)
        
		# no need to create a not function as ! only takes one argument anyway
		# replace & and | with the function names. And run eval
        return eval(expression.replace('|','or_op').replace('&', 'and_op').replace('!', 'not'))
