'''
Given a string expression representing arbitrarily nested ternary expressions, evaluate the expression, and return the result of it.

You can always assume that the given expression is valid and only contains digits, '?', ':', 'T', and 'F' where 'T' is true and 'F' is false. All the numbers in the expression are one-digit numbers (i.e., in the range [0, 9]).

The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, 'T' or 'F'.
'''


Basic Idea
Base Case: for arguments 'T' 'F' '1' '2' ... N return input
Else: Evaluate left or right side of the expression based on T or F

How do we find inner expressions?
Same as validate parentheses problem
? is same as opening bracket
: is same as closing bracket
When question mark counter reaches 0 we have found the matching : for the current ?

class Solution:
    def parseTernary(self, expression: str) -> str:
        if expression.isnumeric() or expression in ('T', 'F'):
            return expression
        
        question_marks = 1
        is_true = expression[0] == 'T'
        
        for i in range(2, len(expression)):
            char = expression[i]
            if char == '?':
                question_marks += 1
            elif char == ':':
                question_marks -= 1
            if question_marks == 0:
                inner_expression = expression[2:i] if is_true else expression[i + 1:]
                return self.parseTernary(inner_expression)
        
        raise ValueError('Invalid Ternary Expression')
------------------------------------------------------------------------------------------
"""
class Solution(object):
def parseTernary(self, expression):
"""
:type expression: str
:rtype: str
"""

	stackmark=[]
    stacknumalpha=[]
    for i in expression[::-1]:
        if i.isalpha() and len(stackmark)>1 and stackmark[-1]=="?":
            first=stacknumalpha.pop()
            second=stacknumalpha.pop()
            stackmark.pop()
            stackmark.pop()
            if i == "T":
                stacknumalpha.append(first)
            elif i == "F":
                stacknumalpha.append(second)
        elif i.isalpha() or i.isdigit():
            stacknumalpha.append(i)
        elif i in ":?":
            stackmark.append(i)
    return stacknumalpha[0]
    
----------------------------------------------------------------------------------------------------------
Basically, we can see the given expression as values ("T" / "F" / "0"-"9") being separated by colon(":") or question mark("?"). Notice that "T" and "F" could be a pure value or a judgment sign. The latter happens when a question mark("?") followed.

Given each value is a single character, we can easily parse them between question marks ("?") and colons(":") and put them into the stack until we face a judgment sign, where a "T" or "F" shows with a followed question mark("?"). When we face them, we judge the top two values in the stack and remove the unneeded one.

Here is my code:

class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = [expression[-1]]
        for i in range(len(expression) - 3, -1, -2):
            if expression[i + 1] == '?':
                if expression[i] == 'T':
                    stack.pop(-2)
                else:
                    stack.pop(-1)
            else:
                stack.append(expression[i])
        return stack.pop()
    
        
