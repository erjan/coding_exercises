'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in range(len(s)):
            if s[i]== '(':
                stack.append(s[i])
            elif s[i]=='[':
                stack.append(s[i])
            elif s[i]=='{':
                stack.append(s[i])
                
            elif s[i] ==')':
                if len(stack)!=0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])
            elif s[i] == '}':
                if len(stack)!=0 and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(s[i])
            elif s[i] == ']':
                if len(stack)!=0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[i])
        
        if len(stack) == 0:
            return True
        return False
                           
            
        
