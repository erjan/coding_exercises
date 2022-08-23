'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''


class Solution:

    def f(self, n):
        stack = []
        res = []

        def backtrack(open,close):
            if open == close == n:
                res.append(stack)
                return
            if open < n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()
            
            if close < n:
                stack.append(')')
                backtrack(open,close+1)
                stack.pop()
        backtrack(0,0)
        return res
    
------------------------------------------------------------
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(left, right, ans, curstring):
            if right < left:
                return
            if not left and not right:
                ans.append(curstring)
                return
            if left:
                backtrack(left-1, right, ans, curstring + "(")
            if right:
                backtrack(left, right-1, ans, curstring + ")")

        res = list()
        backtrack(n, n, res, "")
        print(res)
        return res
            
