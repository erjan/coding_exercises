'''
Given a string s consisting only of "1"s and "0"s, you can delete any two adjacent letters if they are different.

Return the length of the smallest string that you can make if you're able to perform this operation as many times as you want.
'''


class Solution:
    def solve(self, s):
        
        stack = list()
        if len(s) == 0:
            return 0
        if len(s) == 1:
            print(1)
            return 1

        for i in range(len(s)):

            if len(stack) == 0:
                stack += s[i]

            elif stack[-1] == s[i]:
                stack += s[i]
            elif stack[-1] != s[i]:
                stack += s[i]
                stack.pop()
                stack.pop()

        return len(stack)
            
