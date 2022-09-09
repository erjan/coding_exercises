'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        
        res = 0
        
        stack = list()
        stack.append(-1)
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                
                else:
                    res = max(res, i - stack[-1])
        return res
