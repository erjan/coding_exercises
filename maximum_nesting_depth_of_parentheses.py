'''
A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.
'''

#my own solution

class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxi = float('-inf')
        for i in range(len(s)):

            char = s[i]
            print('current bracket count ', count)
            if char == '(':
                count += 1
            if char == ')':
                count -= 1

            if count > maxi:
                print('new max found ',  count)
                maxi = count
        print(maxi)
        return maxi
      
#stack solution

def maxDepth(self, s):

    stack, res = [], 0
	
    for c in s:
        if c == "(":
            stack.append(c)
            res = max(res, len(stack))
        elif c == ")":
            stack.pop()			
    return res
