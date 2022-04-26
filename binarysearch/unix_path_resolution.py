'''
Given a Unix path, represented as a list of strings, return its resolved version.

In Unix, ".." means to go to the previous directory and "." means to stay 
on the current directory. By resolving, we mean to evaluate the two symbols so that we get the final directory we're currently in.
'''


class Solution:
    def solve(self, path):
        
        stack = []

        for s in path:
            if s == "..":
                if len(stack)> 0:
                    stack.pop()
            elif s == ".":
                continue
            else:
                stack.append(s)
        print(stack)
        return stack


        
