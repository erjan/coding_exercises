

'''
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.
'''

class Solution(object):
    def canBeValid(self, s, locked):
        if len(s) % 2:  # Intuitively, odd-length s cannot be valid.
            return False

        # traverse each parenthesis forward, treat all unlocked Parentheses as'(' and check if there is ')'
        # that cannot be eliminated by previous '(', if it exists, then the input s can't be valid.
        balance = 0
        for i in range(len(s)):
            balance += 1 if s[i] == '(' or locked[i] == '0' else -1
            if balance < 0:
                return False

        # traverse each parenthesis backward, treat all unlocked Parentheses as')' and check if there is '('
        # that cannot be eliminated by previous ')', if it exists, then the input s can't be valid.
        balance = 0
        for i in range(len(s) - 1, -1, -1):
            balance += 1 if s[i] == ')' or locked[i] == '0' else -1
            if balance < 0:
                return False

        return True
