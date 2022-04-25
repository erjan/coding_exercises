'''
Given a string s representing characters typed into an editor, with "<-" representing a backspace, return the current state of the editor.

Constraints

n ≤ 100,000 where n is the length of s
'''


class Solution:
    def solve(self, s):

        i = 0
        stack = []

        while i < len(s):

            if s[i] == '<' and i < len(s)-1 and s[i+1] == '-':
                if len(stack) != 0:
                    stack.pop()
                i += 2
            else:
                stack.append(s[i])
                i += 1
        stack = ''.join(stack)
        print(stack)
        return stack
            
        
----------------------------------------------------------------
class Solution:
    def solve(self, s):
        text = s.split("<-")
        ans = text[0]
        for i in range(1, len(text)):
            ans = ans[:-1]  # removing last character
            ans += text[i]
        return ans
