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
