'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        bracket_stack = list()
        star_stack = list()
        for i in range(len(s)):
            if s[i] == '*':
                star_stack.append(i)
            elif s[i] == '(':
                bracket_stack.append(i)
            elif s[i] == ')':
                if len(bracket_stack) == 0 and len(star_stack)==0:
                    return False
                if len(bracket_stack) ==0 and len(star_stack)!=0:
                    star_stack.pop()
                elif len(bracket_stack) > 0:
                    bracket_stack.pop()

        #check stacks now
        if len(bracket_stack)==0:
            return True

        if len(bracket_stack)!= 0 and len(star_stack) == 0:
            return False
        while bracket_stack:
            if star_stack == None:
                return False
            elif len(bracket_stack) > 0 and len(star_stack)> 0 and bracket_stack[-1] < star_stack[-1]:
                bracket_stack.pop()
                star_stack.pop()
            else:
                return False
        return True
