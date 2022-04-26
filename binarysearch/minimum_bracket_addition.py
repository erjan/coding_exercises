'''
Given a string s containing brackets ( and ), return the minimum 
number of brackets that can be inserted so that the brackets are balanced.
'''

class Solution:
    def solve(self, s):
        stack = []

        for bracket in s:

            if bracket == '(':
                stack.append(bracket)
            elif bracket == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(bracket)
        return len(stack)
      
      
-----------------------------------------------------------------------------------------
class Solution:
    def solve(self, s):
        num_open_brackets = 0
        num_need_brackets = 0
        for bracket in s:
            if bracket == "(":
                num_open_brackets += 1
            elif num_open_brackets:
                num_open_brackets -= 1
            else:
                num_need_brackets += 1
        num_need_brackets += num_open_brackets
        return num_need_brackets
