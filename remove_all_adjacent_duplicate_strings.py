'''
You are given a string s consisting of lowercase English letters. A duplicate 
removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        stack = []

        for c in s:

            # if the prev charac is same as before, we need to pop it, the current same char is iterated over as usual
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        res = ''.join(stack)
        print(res)
        return res
