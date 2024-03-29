'''
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
'''


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = bal = 0
        for i in s:
            if i == '(':
                bal+=1
            else:
                bal-=1
            if bal == -1:
                ans+=1
                bal+=1
        return ans+bal

-------------------------------------------------

    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for ch in S:
            if ch == '(': stack.append(ch)
            else:
                if len(stack) and stack[-1] == '(': stack.pop()
                else: stack.append(ch)
        return len(stack)

    
-----------------------------------------------------------
#my own solution

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = list()
                
        for elem in s:
            
            if elem == '(':
                stack.append(elem)
                
            else:
                if elem == ')' and len(stack)!= 0  and stack[-1] == '('  :
                    stack.pop()
                else:
                    stack.append(elem)
        return len(stack)
        
        
