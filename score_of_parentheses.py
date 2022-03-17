'''
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

'''

class Solution:
    def scoreOfParentheses(self, s: str) -> int:               
        stack=[]
        score=0
        
        for ch in s:
            if ch=="(":
                stack.append(score)
                score=0
            else:
                score=stack.pop()+max(2*score,1)
        
        return score
