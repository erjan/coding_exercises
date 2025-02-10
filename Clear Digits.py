You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.


  -------------------------------------------------------
  my solution:

class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []

        for i in range(len(s)):
            if not s[i].isdigit():
                stack.append(s[i])
            elif s[i].isdigit and not stack[-1].isdigit():
                stack.pop()
        stack = ''.join(stack)
        return stack


----------------------------------------------------------------------------------------
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
