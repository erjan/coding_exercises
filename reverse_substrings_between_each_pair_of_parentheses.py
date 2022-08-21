'''
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 
 '''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = list()
        res = ''
        for i in range(len(s)):
            if s[i] == ')':
                tmp = ""
                while stack[-1] != '(':
                    t = stack.pop()
                    print(t)
                    tmp += t

                stack.pop()
                for j in tmp:
                    stack.append(j)
            else:
                stack.append(s[i])

        return "".join(stack)

       
-----------------------------------------------------------------------------
class Solution:
    def reverseParentheses(self, s: str) -> str:
        i, n, stack = 0, len(s), []
        
        while i < n:
            if  s[i] == '(':  # if its opening parentheses, just append
                stack.append(s[i])
            elif s[i] == ')': # if its closing parentheses
                st = ''
                while stack!=[] and stack[-1]!='(': #while stack is not empty and stack's top is NOT an opening parentheses
                    st += stack.pop() #pop the element and append to a temporary string
                stack.pop() #pop the last remaining ( in some cases
                stack += list(st) #append the popped elements to stack
            else:
                stack.append(s[i]) #pushing all letters into stack
            i += 1
        return ''.join(stack)
