'''
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.
'''


class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack, res = [], 0
        for i in range(len(s)):
            if stack and s[i] == "a" and stack[-1] == "b":
                stack.pop()
                res += 1
            else:
                stack.append(s[i])
        return res
